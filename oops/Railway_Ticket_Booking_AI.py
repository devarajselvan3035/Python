from abc import ABC, abstractmethod
from collections import deque
from enum import Enum
from typing import List, Dict, Optional, Deque


# ==============================================================================
# 1. ENUMS & VALUE OBJECTS (Domain Model)
# ==============================================================================


class BerthType(Enum):
    LOWER = "Lower"
    MIDDLE = "Middle"
    UPPER = "Upper"
    SIDE_LOWER = "Side Lower"  # Shared for RAC
    NONE = "None"  # For Waiting List


class TicketStatus(Enum):
    CONFIRMED = "CONFIRMED"
    RAC = "RAC"
    WAITING_LIST = "WAITING_LIST"
    CANCELLED = "CANCELLED"


class Passenger:
    """Encapsulates individual passenger data and physical seat assignments."""

    def __init__(self, name: str, age: int, preferred_berth: BerthType):
        self.name: str = name
        self.age: int = age
        self.preferred_berth: BerthType = preferred_berth

        # State variables managed by the allocation engine
        self.allocated_berth: BerthType = BerthType.NONE
        self.seat_number: int = -1
        self.status: TicketStatus = TicketStatus.WAITING_LIST


# ==============================================================================
# 2. CORE TICKET CLASS (Encapsulation)
# ==============================================================================


class Ticket:
    """Acts as the domain aggregate tying a unique ID to a Passenger instance."""

    def __init__(self, ticket_id: int, passenger: Passenger):
        self.ticket_id: int = ticket_id
        self.passenger: Passenger = passenger

    def display_details(self) -> str:
        p = self.passenger
        seat_info = (
            f"Seat {p.seat_number} ({p.allocated_berth.value})"
            if p.seat_number != -1
            else "No Seat Assigned"
        )
        return (
            f"ID: {self.ticket_id} | Name: {p.name:<12} | Age: {p.age:<3} | "
            f"Status: {p.status.value:<12} | Allocation: {seat_info}"
        )


# ==============================================================================
# 3. COMPOSITION & INVENTORY MANAGEMENT (The Train Inventory)
# ==============================================================================


class TrainInventory:
    """
    Manages the physical hardware layouts and seat state boundaries.
    Demonstrates Encapsulation by shielding raw counters from direct external mutation.
    """

    def __init__(
        self,
        lower: int = 1,
        middle: int = 1,
        upper: int = 1,
        rac_slots: int = 2,
        wl_slots: int = 2,
    ):
        # Master capacity boundaries
        self.berth_counts: Dict[BerthType, int] = {
            BerthType.LOWER: lower,
            BerthType.MIDDLE: middle,
            BerthType.UPPER: upper,
        }
        self.max_rac: int = rac_slots
        self.max_wl: int = wl_slots

        # Tracking exact numbers of real-time map allocations
        self.confirmed_seats_map: Dict[BerthType, List[int]] = {
            BerthType.LOWER: list(range(1, lower + 1)),
            BerthType.MIDDLE: list(range(1, middle + 1)),
            BerthType.UPPER: list(range(1, upper + 1)),
        }

        # RAC uses side-lower berths. 2 passengers per side-lower seat.
        # If max_rac is 2, it means we have 1 physical side-lower seat (Seat #1).
        self.rac_seats_pool: List[int] = list(range(1, (rac_slots // 2) + 1))
        self.rac_assignments: Dict[int, List[Passenger]] = {
            seat: [] for seat in self.rac_seats_pool
        }

        # Queues for waitlists and partial allocations
        self.rac_queue: Deque[Ticket] = deque()
        self.wl_queue: Deque[Ticket] = deque()

        # Global database mapping for direct $O(1)$ lookups during cancellations
        self.active_tickets: Dict[int, Ticket] = {}

    def get_available_berth_count(self, berth: BerthType) -> int:
        return len(self.confirmed_seats_map.get(berth, []))

    def get_total_confirmed_available(self) -> int:
        return sum(len(seats) for seats in self.confirmed_seats_map.values())

    def get_available_rac_count(self) -> int:
        return self.max_rac - len(self.rac_queue)

    def get_available_wl_count(self) -> int:
        return self.max_wl - len(self.wl_queue)


# ==============================================================================
# 4. BUSINESS LOGIC ENGINE (Facade Pattern)
# ==============================================================================


class RailwayBookingSystem:
    """
    The central system orchestrating the ticketing workflows.
    Hides structural lookup details and promotion chains behind simple APIs.
    """

    def __init__(self, inventory: TrainInventory):
        self._inventory: TrainInventory = inventory
        self._ticket_id_counter: int = 1

    def book_ticket(self, name: str, age: int, preferred_berth_str: str) -> None:
        # Convert raw string inputs cleanly to Enums
        pref_map = {"L": BerthType.LOWER, "M": BerthType.MIDDLE, "U": BerthType.UPPER}
        pref_berth = pref_map.get(preferred_berth_str.upper(), BerthType.LOWER)

        passenger = Passenger(name, age, pref_berth)
        ticket = Ticket(self._ticket_id_counter, passenger)

        # Senior citizen optimization constraint rule (Zoho validation favorite)
        if age > 60 and self._inventory.get_available_berth_count(BerthType.LOWER) > 0:
            passenger.preferred_berth = BerthType.LOWER
            pref_berth = BerthType.LOWER

        # Step 1: Attempt allocation on Preferred Choice
        if self._inventory.get_available_berth_count(pref_berth) > 0:
            self._allocate_confirmed(ticket, pref_berth)
            return

        # Step 2: Preferred full -> Check alternative remaining confirmed berths
        allocated = False
        for berth_type in [BerthType.LOWER, BerthType.MIDDLE, BerthType.UPPER]:
            if self._inventory.get_available_berth_count(berth_type) > 0:
                print(
                    f"[System Notice] Preferred {pref_berth.value} full. Allocating available {berth_type.value}."
                )
                self._allocate_confirmed(ticket, berth_type)
                allocated = True
                break

        if allocated:
            return

        # Step 3: Confirmed completely full -> Try RAC queue
        if self._inventory.get_available_rac_count() > 0:
            self._allocate_rac(ticket)
            return

        # Step 4: RAC full -> Try Waiting List queue
        if self._inventory.get_available_wl_count() > 0:
            self._allocate_wl(ticket)
            return

        # Step 5: Everything is full -> Ticket Rejected
        print(
            f"Booking Rejected: No berths, RAC, or Waiting List slots available for {name}."
        )

    def cancel_ticket(self, ticket_id: int) -> None:
        if ticket_id not in self._inventory.active_tickets:
            print(f"Error: Ticket ID {ticket_id} not found or active.")
            return

        cancelled_ticket = self._inventory.active_tickets[ticket_id]
        passenger = cancelled_ticket.passenger
        status = passenger.status

        print(
            f"\n[Processing Cancellation] Voiding Ticket {ticket_id} ({passenger.name})..."
        )

        if status == TicketStatus.CONFIRMED:
            # Free up the specific physical seat
            self._inventory.confirmed_seats_map[passenger.allocated_berth].append(
                passenger.seat_number
            )
            del self._inventory.active_tickets[ticket_id]
            passenger.status = TicketStatus.CANCELLED

            # Cascade: Promote from RAC to Confirmed
            self._promote_rac_to_confirmed(
                passenger.allocated_berth, passenger.seat_number
            )

        elif status == TicketStatus.RAC:
            # Remove from RAC records
            self._inventory.rac_queue.remove(cancelled_ticket)
            self._inventory.rac_assignments[passenger.seat_number].remove(passenger)
            del self._inventory.active_tickets[ticket_id]
            passenger.status = TicketStatus.CANCELLED

            # Cascade: Promote from WL into RAC slot
            self._promote_wl_to_rac()

        elif status == TicketStatus.WAITING_LIST:
            # Simple removal from waitlist queue boundaries
            self._inventory.wl_queue.remove(cancelled_ticket)
            del self._inventory.active_tickets[ticket_id]
            passenger.status = TicketStatus.CANCELLED
            print("Waiting list ticket dropped safely.")

    # ==============================================================================
    # INTERNAL HELPER ALLOCATION MECHANISMS
    # ==============================================================================

    def _allocate_confirmed(self, ticket: Ticket, berth_type: BerthType) -> None:
        p = ticket.passenger
        p.allocated_berth = berth_type
        p.seat_number = self._inventory.confirmed_seats_map[berth_type].pop(0)
        p.status = TicketStatus.CONFIRMED

        self._inventory.active_tickets[self._ticket_id_counter] = ticket
        print(
            f"Booking Confirmed! Ticket ID: {self._ticket_id_counter} | Seat: {p.seat_number} ({berth_type.value})"
        )
        self._ticket_id_counter += 1

    def _allocate_rac(self, ticket: Ticket) -> None:
        p = ticket.passenger
        p.allocated_berth = BerthType.SIDE_LOWER
        p.status = TicketStatus.RAC

        # Find a side-lower seat with room for a passenger sharing it
        for seat_num in self._inventory.rac_seats_pool:
            if len(self._inventory.rac_assignments[seat_num]) < 2:
                p.seat_number = seat_num
                self._inventory.rac_assignments[seat_num].append(p)
                break

        self._inventory.rac_queue.append(ticket)
        self._inventory.active_tickets[self._ticket_id_counter] = ticket
        print(
            f"Confirmed Full! Allocated RAC Layout. Ticket ID: {self._ticket_id_counter} | Side-Lower Seat: {p.seat_number}"
        )
        self._ticket_id_counter += 1

    def _allocate_wl(self, ticket: Ticket) -> None:
        p = ticket.passenger
        p.allocated_berth = BerthType.NONE
        p.seat_number = -1
        p.status = TicketStatus.WAITING_LIST

        self._inventory.wl_queue.append(ticket)
        self._inventory.active_tickets[self._ticket_id_counter] = ticket
        print(
            f"RAC Full! Added to Waiting List. Ticket ID: {self._ticket_id_counter} | Position: {len(self._inventory.wl_queue)}"
        )
        self._ticket_id_counter += 1

    # ==============================================================================
    # ADVANCED STATE CASCADE PROMOTIONS
    # ==============================================================================

    def _promote_rac_to_confirmed(self, free_berth: BerthType, free_seat: int) -> None:
        if not self._inventory.rac_queue:
            return  # No RAC passengers available to fill the slot

        # Pop the first passenger from the RAC queue
        promoted_ticket = self._inventory.rac_queue.popleft()
        p = promoted_ticket.passenger

        # Remove them from their shared RAC side-lower seat assignment
        self._inventory.rac_assignments[p.seat_number].remove(p)

        # Assign them to the newly freed confirmed seat
        p.allocated_berth = free_berth
        p.seat_number = free_seat
        p.status = TicketStatus.CONFIRMED
        self._inventory.confirmed_seats_map[free_berth].remove(
            free_seat
        )  # Keep inventory accurate

        print(
            f"[Promotion Cascade] RAC Passenger '{p.name}' promoted to Confirmed Seat {free_seat} ({free_berth.value})."
        )

        # Now pull the next passenger from the Waiting List up to RAC
        self._promote_wl_to_rac()

    def _promote_wl_to_rac(self) -> None:
        if not self._inventory.wl_queue:
            return  # No one waiting on the waitlist

        # Pop the first passenger from the Waiting List queue
        promoted_ticket = self._inventory.wl_queue.popleft()
        p = promoted_ticket.passenger

        # Set their status to RAC
        p.allocated_berth = BerthType.SIDE_LOWER
        p.status = TicketStatus.RAC

        # Add them to the open RAC side-lower seat slot
        for seat_num in self._inventory.rac_seats_pool:
            if len(self._inventory.rac_assignments[seat_num]) < 2:
                p.seat_number = seat_num
                self._inventory.rac_assignments[seat_num].append(p)
                break

        # Move the ticket into the RAC queue
        self._inventory.rac_queue.append(promoted_ticket)
        print(
            f"[Promotion Cascade] WL Passenger '{p.name}' promoted to RAC Side-Lower Seat {p.seat_number}."
        )

    # ==============================================================================
    # REPORTING & DISPLAY METHODS
    # ==============================================================================

    def print_booked_tickets(self) -> None:
        print("\n======================= ACTIVE BOOKED TICKETS =======================")
        if not self._inventory.active_tickets:
            print("No active tickets found in system memory.")
        else:
            for ticket in self._inventory.active_tickets.values():
                print(ticket.display_details())
        print("=====================================================================")

    def print_available_tickets(self) -> None:
        inv = self._inventory
        print("\n===================== CURRENT LIVE INVENTORY =====================")
        print(
            f" Confirmed LOWER Berths Available : {inv.get_available_berth_count(BerthType.LOWER)}"
        )
        print(
            f" Confirmed MIDDLE Berths Available: {inv.get_available_berth_count(BerthType.MIDDLE)}"
        )
        print(
            f" Confirmed UPPER Berths Available : {inv.get_available_berth_count(BerthType.UPPER)}"
        )
        print(
            f" RAC Slots Available              : {inv.get_available_rac_count()} / {inv.max_rac}"
        )
        print(
            f" Waiting List Slots Available     : {inv.get_available_wl_count()} / {inv.max_wl}"
        )
        print("====================================================================")


# ==============================================================================
# 5. INTERACTIVE TERMINAL LOOP RUNTIME (Zoho Interview Execution Interface)
# ==============================================================================

if __name__ == "__main__":
    # Initialize the system with a small layout to make testing transitions easy
    # 1 Lower, 1 Middle, 1 Upper, 2 RAC slots (1 seat), and 2 Waiting List slots.
    train_layout = TrainInventory(lower=1, middle=1, upper=1, rac_slots=2, wl_slots=2)
    system = RailwayBookingSystem(train_layout)

    print("=================================================================")
    print("      WELCOME TO THE ZOHO RAILWAY SYSTEM CENTRAL DASHBOARD       ")
    print("=================================================================")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Print Booked Tickets")
        print("4. Print Available Inventory")
        print("5. Exit System")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            print("\n--- Passenger Booking Wizard ---")
            name = input("Enter Passenger Name: ").strip()
            try:
                age = int(input("Enter Passenger Age: ").strip())
            except ValueError:
                print("Invalid input. Age must be a whole number.")
                continue
            pref = (
                input("Enter Berth Preference (L = Lower, M = Middle, U = Upper): ")
                .strip()
                .upper()
            )

            if pref not in ["L", "M", "U"]:
                print("Invalid preference selected. Defaulting allocation choices.")

            system.book_ticket(name, age, pref)

        elif choice == "2":
            print("\n--- Passenger Cancellation Wizard ---")
            try:
                t_id = int(input("Enter Ticket ID to cancel: ").strip())
                system.cancel_ticket(t_id)
            except ValueError:
                print("Invalid input. Ticket ID must be an integer sequence.")

        elif choice == "3":
            system.print_booked_tickets()

        elif choice == "4":
            system.print_available_tickets()

        elif choice == "5":
            print(
                "\nShutting down terminal connection. System state cleared from memory."
            )
            break
        else:
            print("Invalid command. Please input a selection from 1 to 5.")
