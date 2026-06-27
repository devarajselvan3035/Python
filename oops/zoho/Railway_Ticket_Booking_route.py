from enum import Enum

class StatusType(Enum):
    COMPLETED='Completed'
    CANCEL='Cancel'
    WL='Waiting List'
    NONE='None'
    
class TrouteInventory:
    
    def __init__(self, route: list[str], no_seats: int, wl_seats):
        self.route = route
        self.max_seats = no_seats
        self.max_wl_seats = wl_seats
        
        self.route_idx: dict[str, int] = {stop:idx  for idx, stop in enumerate(route)}
        self.route_seats: dict[int, list] = {idx:list(range(1, no_seats+1)) for idx, stop in enumerate(route)}

        self.wl_queue: list[Booking] = []
        
        self._passanger_list: dict[int, Passanger] = {}
        self._booking_list: dict[int, Booking] = {}
        
        
    def get_segment(self, source: str, target: str) -> list[int]:
        source_idx = self.route_idx[source]
        target_idx = self.route_idx[target]
        return list(range(source_idx, target_idx))
    
    def _get_available_seats(self, segment: list[int]) -> list[int]:
        result = set(self.route_seats[segment[0]])
        for idx in segment[1:]:
            result = result | set(self.route_seats[idx])
        return result
    
    def _refere_seat(self, segment: list[int]) -> int:
        available_seat = self._get_available_seats(segment)
        return min(available_seat)
            
        
class Passanger:
    passangerId = 0
    
    def __init__(self, name: str, source: str, target: str):
        Passanger.passangerId += 1
        self.passanger_id = Passanger.passangerId
        self.name = name
        self.source = source
        self.target = target
        
        self._seat_no: int | None = None
        self._status = StatusType.NONE
        
class Booking:
    bookingId = 0
    
    def __init__(self, passanger):
        Booking.bookingId += 1
        self.booking_id = Booking.bookingId
        self.passanger: Passanger = passanger
        
class BookingEngine:
    
    def __init__(self, inventory: TrouteInventory):
        self.inventory = inventory
        self._passanger_list = self.inventory._passanger_list
        self._booking_list = self.inventory._booking_list
        
    def bookTicket(self, name: str, source: str, target: str):
        passanger = Passanger(name, source, target)
        booking = Booking(passanger)
        segment = self.inventory.get_segment(source, target)
        self._booking_list[booking.booking_id] = booking
        self._passanger_list[passanger.passanger_id] = passanger
        
        if len(self.inventory._get_available_seats(segment)) > 0:
            self._add_confirmed(booking, passanger, segment)
        
        elif len(self.inventory.wl_queue) < self.inventory.max_wl_seats:
            self._add_wl(booking, passanger)
        
        else:
            print("seats are out of state")
        
    def cancelTicket(self, booking_id: int):
        booking = self._booking_list[booking_id]
        passanger = booking.passanger
        segment = self.inventory.get_segment(passanger.source, passanger.target)
        
        passanger._status = StatusType.CANCEL
        
        for idx in segment:
            self.inventory.route_seats[idx].append(passanger._seat_no)
        
        for bwl in self.inventory.wl_queue:
            wl = bwl.passanger
            inner_segment = self.inventory.get_segment(wl.source, wl.target)
            if len(self.inventory._get_available_seats(segment)) > 0:
                self._add_confirmed(bwl, wl, inner_segment)
                self.inventory.wl_queue.remove(bwl)
                return
            
            
    def _add_confirmed(self, booking: Booking, passanger: Passanger, segment: list[int]):
        seat = self.inventory._refere_seat(segment)
        
        passanger._status = StatusType.COMPLETED
        passanger._seat_no = seat
        
        for idx in segment:
            self.inventory.route_seats[idx].remove(seat)
            
        self._print_ticket(booking, passanger)
        
    def _add_wl(self, booking: Booking, passanger: Passanger):
        
        passanger._status = StatusType.WL
        self.inventory.wl_queue.append(booking)
        self._print_ticket(booking, passanger)
        
            
    def _print_ticket(self, booking: Booking, passanger: Passanger):
            
        print(self.inventory.route_seats)
        print("___ BOOKING CONFIRMED ___")
        print(f"Ticket No : {booking.booking_id}")
        print(f"Passanger: {passanger.name}")
        print(f"Seat Assigned : {passanger._seat_no}")
        print(f"Staus: {passanger._status}")
            
        
if __name__ == "__main__":
    inv = TrouteInventory(['a', 'b', 'c', 'd'], 1, 1)
    bt = BookingEngine(inv)
    
    while True:
        option = int(input("""
                           1. Book Ticket
                           2. Cancel Ticket
                           3. Display Chart Status
                           4. Display Waiting List
                           Enter Your Choice (1-5) : """))

        if option == 1:
            name = input("Enter Passanger Name : ")
            source = input("Enter Source Station : ")
            target = input("Enter Target Station : ")

            if source in bt.inventory.route and target in bt.inventory.route:
                bt.bookTicket(name, source, target)
            else:
                print("Given source or target is invalid")
                
        elif option == 2:
            booking_id = int(input("Enter Booking Id : "))
            if booking_id in bt._booking_list:
                bt.cancelTicket(booking_id)
                
        else:
            break
                

        
        
        
    