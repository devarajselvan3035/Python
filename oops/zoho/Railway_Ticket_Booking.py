from enum import Enum


class BerthType(Enum):
    LOWER = "L"
    MIDDLE = "M"
    UPPER = "U"
    
class Status(Enum):
    CONFIRMED="Confirmed"
    RAC="rac"
    WAITING="Waiting"
    
    
class Passenger:
    passengerId = 0
    def __init__(self, name: str, age: int, berth_type: BerthType) -> None:
        Passenger.passengerId += 1
        self.passenger = Passenger.passengerId
        self.name = name
        self.age = age
        self.berth_type = berth_type
        
        self._status = Status.WAITING
        
class Ticket:
    ticketId = 1000
    
    def __int__(self, passenger: Passenger):
        Ticket.ticketId += 1
        self.ticket_id = Ticket.ticketId
        self.passenger = passenger
        
    def ticketDetails(self) -> str:
        return f"{self.ticket_id} {self.passenger.name} | {self.passenger.age} | {self.passenger.berth_type}"
    
class TrainDetails:
    def __init__(self, lower: int, middle: int, 
                 upper: int, rac: int, waiting: int):
        self.upper = upper
        self.middle = middle
        self.lower = lower
        self.max_rac = rac
        self.max_wait = waiting
        
    def _available_lower_berth(self) -> str:
        

    
