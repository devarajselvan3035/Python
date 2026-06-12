from enum import Enum

class SheetType(Enum):
    SLEEPER="sleeper"
    LOWER="lower"
    REGULAR="regular"
    NONE="None"

class Passanger:
    passangerId = 100
    
    def __init__(self, name, age):
        Passanger.passangerId += 1
        self.passanger_id = Passanger.passangerId
        self.name = name
        self.age = age
        self.seat: str | None = None
        self.booking_id: int | None = None
        
    def _check_above_60(self) -> bool:
        if self.age >= 60:
            return True
        return False
        
class Booking:
    bookingId = 0
    
    def __init__(self):
        Booking.bookingId += 1
        self.booking_id = Booking.bookingId
        self._passanger_list: list[Passanger] = []
        
    def _view_booking(self):
        print(f"{self.booking_id}")
        for val in self._passanger_list:
            print(f"{val.name=}, {val.booking_id}, {val.seat}")
        
class Inventory:
    
    def __init__(self):
        self._passanger_list: dict[int, Passanger] = {}
        self._booking_list : dict[int, Booking] = {}
        
class BusBookingSystem:
    SLEEPER = {'S' + str(i):None for i in range(1, 11)}
    LOWER = {'L' + str(i): None for i in range(11, 21)}
    REGULAR = {'R' + str(i): None for i in range(21, 31)}

    def __init__(self):
        self.invetory = Inventory()
        self._passanger_list = self.invetory._passanger_list  
        self._booking_list = self.invetory._booking_list      
        
        
    def bookTicket(self, no_of_pass:int, name:str, age:int, seat_type:str):
        type_dict = {'sleeper':self.SLEEPER, 
                     'lower':self.LOWER,
                     'regular': self.REGULAR}
        
        booking = Booking()
        for _ in range(no_of_pass):
            passanger = Passanger(name, age)
            if passanger._check_above_60() and seat_type.lower() != "sleeper":
                self._bookSeat(passanger, type_dict['lower'])
            else:
                self._bookSeat(passanger, type_dict[seat_type.lower()])
            passanger.booking_id = booking.booking_id
            booking._passanger_list.append(passanger)
        self._booking_list[booking.booking_id] = booking
        
        booking._view_booking()
                
    def _bookSeat(self, passanger: Passanger, seat_dict:dict):
        for key, val in seat_dict.items():
            if not val:
                passanger.seat = key
                seat_dict[key] = passanger
        
            
    
    
    
if __name__ == "__main__":
    bb = BusBookingSystem()
    bb.bookTicket(2, 'dev', 35, 'sleeper')
    
    