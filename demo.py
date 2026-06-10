import enum
from typing import List, Dict, Optional


class TicketStatus(enum.Enum):
    CONFIRMED = "CONFIRMED"
    RAC = "RAC"
    WAITING_LIST = "WAITING_LIST"
    CANCELLED = "CANCELLED"


class Passenger:
    def __init__(self, name: str, age: int, preferred_berth: str):
        self.name = name
        self.age = age
        self.preferred_berth = preferred_berth  # 'L', 'M', 'U'
        self.allocated_seat: Optional[int] = None
        self.allocated_berth_type: Optional[str] = None


class Ticket:
    _pnr_counter = 1000

    def __init__(self, source: str, destination: str, passengers: List[Passenger]):
        Ticket._pnr_counter += 1
        self.pnr: int = Ticket._pnr_counter
        self.source: str = source
        self.destination: str = destination
        self.passengers: List[Passenger] = passengers
        self.status: TicketStatus = TicketStatus.WAITING_LIST


class TrainRoute:
    """Manages the chronological sequence of stations."""

    def __init__(self, stations: List[str]):
        self.stations = stations
        self.station_index = {station: idx for idx, station in enumerate(stations)}

    def get_segments(self, source: str, dest: str) -> List[int]:
        """Returns the indices of the segments spanned by the journey."""
        start_idx = self.station_index[source]
        end_idx = self.station_index[dest]
        return list(range(start_idx, end_idx))


class BookingEngine:
    def __init__(self, stations: List[str], total_berths: int, total_rac: int):
        self.route = TrainRoute(stations)
        self.num_segments = len(stations) - 1

        # Segment-based inventory management
        # Map: segment_index -> List of available physical seat numbers
        self.berth_inventory: Dict[int, List[int]] = {
            i: list(range(1, total_berths + 1)) for i in range(self.num_segments)
        }
        print(f"Berth Inventory {self.berth_inventory}")
        self.rac_inventory: Dict[int, List[int]] = {
            i: list(range(total_berths + 1, total_berths + total_rac + 1))
            for i in range(self.num_segments)
        }
        print(f"RAC Inventory {self.rac_inventory}")

        self.waiting_list_queue: List[Ticket] = []
        self.active_tickets: Dict[int, Ticket] = {}

    def _get_available_seat_for_journey(
        self, inventory: Dict[int, List[int]], segments: List[int]
    ) -> Optional[int]:
        """Finds a physical seat number that is mutually free across ALL required segments."""
        if not segments:
            return None

        # Intersect available seats across all targeted segments
        common_seats = set(inventory[segments[0]])
        for seg in segments[1:]:
            common_seats.intersection_update(inventory[seg])

        if common_seats:
            return min(
                common_seats
            )  # Return lowest available seat number for consistency
        return None

    def _occupy_seat_for_journey(
        self, inventory: Dict[int, List[int]], segments: List[int], seat_no: int
    ):
        """Removes the seat from the inventory maps of the specified segments."""
        for seg in segments:
            inventory[seg].remove(seat_no)

    def _release_seat_for_journey(
        self, inventory: Dict[int, List[int]], segments: List[int], seat_no: int
    ):
        """Restores the seat to the inventory maps of the specified segments."""
        for seg in segments:
            if seat_no not in inventory[seg]:
                inventory[seg].append(seat_no)
                inventory[seg].sort()

    def book_ticket(
        self, source: str, destination: str, passengers: List[Passenger]
    ) -> Ticket:
        """Core booking transactional pipeline handling segmented checks."""
        ticket = Ticket(source, destination, passengers)
        segments = self.route.get_segments(source, destination)

        # Step 1: Try booking Confirmed Berths
        all_confirmed = True
        allocated_seats = []

        # Temporary transaction track to verify if ALL passengers can be accommodated together
        for passenger in passengers:
            seat_no = self._get_available_seat_for_journey(
                self.berth_inventory, segments
            )
            if seat_no:
                allocated_seats.append((passenger, seat_no, "CONFIRMED"))
                # Speculatively remove to ensure subsequent passengers in same ticket don't grab it
                self._occupy_seat_for_journey(self.berth_inventory, segments, seat_no)
            else:
                all_confirmed = False
                break

        if all_confirmed:
            for passenger, seat_no, status_type in allocated_seats:
                passenger.allocated_seat = seat_no
                passenger.allocated_berth_type = passenger.preferred_berth
            ticket.status = TicketStatus.CONFIRMED
            self.active_tickets[ticket.pnr] = ticket
            return ticket

        # Rollback speculative allocations if confirmed failed
        for passenger, seat_no, _ in allocated_seats:
            self._release_seat_for_journey(self.berth_inventory, segments, seat_no)

        # Step 2: Try booking RAC Seats
        all_rac = True
        allocated_rac_seats = []
        for passenger in passengers:
            seat_no = self._get_available_seat_for_journey(self.rac_inventory, segments)
            if seat_no:
                allocated_rac_seats.append((passenger, seat_no))
                self._occupy_seat_for_journey(self.rac_inventory, segments, seat_no)
            else:
                all_rac = False
                break

        if all_rac:
            for passenger, seat_no in allocated_rac_seats:
                passenger.allocated_seat = seat_no
                passenger.allocated_berth_type = "RAC_SIDE"
            ticket.status = TicketStatus.RAC
            self.active_tickets[ticket.pnr] = ticket
            return ticket

        # Rollback RAC if it fails
        for passenger, seat_no in allocated_rac_seats:
            self._release_seat_for_journey(self.rac_inventory, segments, seat_no)

        # Step 3: Fallback to Waiting List
        ticket.status = TicketStatus.WAITING_LIST
        self.waiting_list_queue.append(ticket)
        self.active_tickets[ticket.pnr] = ticket
        return ticket

    def cancel_ticket(self, pnr: int):
        """Cancels a ticket and triggers an explicit, segmented queue promotion."""
        if pnr not in self.active_tickets:
            print(f"Error: Ticket with PNR {pnr} not found.")
            return

        ticket = self.active_tickets[pnr]
        if ticket.status == TicketStatus.CANCELLED:
            return

        segments = self.route.get_segments(ticket.source, ticket.destination)
        old_status = ticket.status
        ticket.status = TicketStatus.CANCELLED

        print(f"\n--- Processed Cancellation for PNR: {pnr} ---")

        if old_status == TicketStatus.CONFIRMED:
            for passenger in ticket.passengers:
                self._release_seat_for_journey(
                    self.berth_inventory, segments, passenger.allocated_seat
                )
                passenger.allocated_seat = None
            self._process_queue_promotions()

        elif old_status == TicketStatus.RAC:
            for passenger in ticket.passengers:
                self._release_seat_for_journey(
                    self.rac_inventory, segments, passenger.allocated_seat
                )
                passenger.allocated_seat = None
            self._process_queue_promotions()

        elif old_status == TicketStatus.WAITING_LIST:
            self.waiting_list_queue.remove(ticket)

    def _process_queue_promotions(self):
        """Scans waiting list or RAC entries to fill freshly opened segment slots."""
        # Process waiting list sequentially to see if anyone fits the new vacant segments
        for wl_ticket in list(self.waiting_list_queue):
            wl_segments = self.route.get_segments(
                wl_ticket.source, wl_ticket.destination
            )

            # Can we upgrade this entire WL ticket to Confirmed now?
            all_confirmed = True
            allocated = []
            for passenger in wl_ticket.passengers:
                seat_no = self._get_available_seat_for_journey(
                    self.berth_inventory, wl_segments
                )
                if seat_no:
                    allocated.append((passenger, seat_no))
                    self._occupy_seat_for_journey(
                        self.berth_inventory, wl_segments, seat_no
                    )
                else:
                    all_confirmed = False
                    break

            if all_confirmed:
                for passenger, seat_no in allocated:
                    passenger.allocated_seat = seat_no
                    passenger.allocated_berth_type = passenger.preferred_berth
                wl_ticket.status = TicketStatus.CONFIRMED
                self.waiting_list_queue.remove(wl_ticket)
                print(
                    f" Ticket PNR {wl_ticket.pnr} promoted from Waiting List to CONFIRMED."
                )
            else:
                # Rollback speculative allocations for this ticket optimization scan
                for passenger, seat_no in allocated:
                    self._release_seat_for_journey(
                        self.berth_inventory, wl_segments, seat_no
                    )


# --- Verification Execution ---
if __name__ == "__main__":
    # Initialize a route: Chennai -> Katpadi -> Jolarpettai -> Bangalore
    engine = BookingEngine(
        stations=["Chennai", "Katpadi", "Jolarpettai", "Bangalore"],
        total_berths=2,
        total_rac=1,
    )

    # 1. Book fully across the entire route to take up all regular berths (size=2)
    p1 = Passenger("Alice", 30, "L")
    p2 = Passenger("Bob", 28, "U")
    t1 = engine.book_ticket("Chennai", "Bangalore", [p1, p2])
    print(
        f"Ticket 1 Status (Chennai -> Bangalore): {t1.status.value} | Seats: {[p.allocated_seat for p in t1.passengers]}"
    )

    # 2. Book a partial journey segment. Regular berths are full, should hit RAC
    p3 = Passenger("Charlie", 45, "L")
    t2 = engine.book_ticket("Chennai", "Katpadi", [p3])
    print(
        f"Ticket 2 Status (Chennai -> Katpadi): {t2.status.value} | Seat: {t2.passengers[0].allocated_seat}"
    )

    # 3. Next booking should fall back to the Waiting List
    p4 = Passenger("David", 50, "U")
    t3 = engine.book_ticket("Katpadi", "Bangalore", [p4])
    print(f"Ticket 3 Status (Katpadi -> Bangalore): {t3.status.value}")

    # 4. Cancel Ticket 1. This should automatically pull David out of the Waiting List
    # because his segment (Katpadi -> Bangalore) is now open!
    engine.cancel_ticket(t1.pnr)
