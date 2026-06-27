from enum import Enum
class BerthType(Enum):
    LOWER="Lower"
    MIDDLE="Middle"
    UPPER="Upper"
    NONE="None"
    
class StatusType(Enum):
    CONFIRMED="Confirmed"
    RAC="Rac"
    WL="Wl"
    NONE="None"

class Passanger:
    passangerId = 100
    
    def __init__(self, name: str, age: int, gender:str, berth: str):
        Passanger.passangerId += 1
        self.passanger_id = Passanger.passangerId
        self.name = name
        self.age = age
        self.gender = gender
        self.berth: BerthType = berth
        
        self._pre_berth: BerthType = BerthType.NONE
        self.seat_no: str|None = None
        self.status: StatusType = StatusType.NONE
        
    def _above_60(self):
        if self.age >= 60:
            return True
        return False
    
    def _below_2(self):
        if self.age <= 2:
            return True
        return False
    
    
class Ticket:
    ticketId = 1000
    
    def __init__(self):
        Ticket.ticketId += 1
        self.ticket_id = Ticket.ticketId
        self.passanger_list: dict[int, Passanger] = {}
        
    def _check_have_child(self):
        for val in self.passanger_list.values():
            if val._below_2():
                return True
        return False
    
class Inventory:
    
    def __init__(self, lower: int=1, middle: int=1, upper: int=1):
        
        self.berth_count = {
            BerthType.LOWER: lower,
            BerthType.MIDDLE : middle,
            BerthType.UPPER : upper
        }
        
        self.berth_seats = {
            BerthType.LOWER : list(i for i in range(1, lower+1)),
            BerthType.MIDDLE : list(i for i in range(1, middle+1)),
            BerthType.UPPER: list(i for i in range(1, upper+1))
        }
        
        self.rac_queue = []
        self.wl_queue=  []
        
        self._tikcet_list: dict[int, Ticket] = {}
        self._passanger_list: dict[int, Passanger] = {}
        
    def berth_available_seat(self, berth_type):
        return len(self.berth_seats[berth_type])
    
    def all_available_seat(self):
        return sum(len(seats) for seats in self.berth_seats.values())
        
        
class RailwayTicketBooking:
    
    def __init__(self):
        self.inventory = Inventory()
        self._ticket_list = self.inventory._tikcet_list
        self._passanger_list = self.inventory._passanger_list
        
    def _print_tickets(self):
        for key, val in self._ticket_list.items():
            print(f"Ticket ID {val.ticket_id}")
            for pas in val.passanger_list.values():
                print(pas.__dict__)
                
        
    def createTicket(self) -> Ticket:
        ticket = Ticket()
        self._ticket_list[ticket.ticket_id] = ticket
        return ticket
        
    def bookTicket(self, name: str, age: int, gender: str, berth: str, ticket: Ticket):

        berth_type_dict = {'L': BerthType.LOWER, 'M': BerthType.MIDDLE, 'U': BerthType.UPPER}
        
        passanger = Passanger(name, age, gender, berth)
        ticket.passanger_list[passanger.passanger_id] = passanger
        
        berth_type = berth_type_dict.get(berth, BerthType.LOWER)
        
        if passanger._above_60():
            berth_type = BerthType.LOWER
            
        if self.inventory.berth_available_seat(berth_type) > 0:
            self._allocated_confirmed(ticket, passanger, berth_type)
            return 
        
        allocated = False
        if self.inventory.all_available_seat() > 0:
            for berth in [BerthType.LOWER, BerthType.MIDDLE, BerthType.UPPER]:
                if self.inventory.berth_available_seat(berth) > 0:
                    self._allocated_confirmed(ticket, passanger, berth)
                    return
        
        
            
    def _allocated_confirmed(self, ticket: Ticket, passanger: Passanger, berth_type: BerthType):
        p = passanger
        seat_number = self.inventory.berth_seats[berth_type].pop(0)
        
        p._pre_berth = berth_type
        p.seat_no = seat_number
        p.status = StatusType.CONFIRMED
        return 
    
if __name__ == "__main__":
    rts = RailwayTicketBooking()
    ticket = rts.createTicket()
    rts.bookTicket('dev', 25, 'male', 'lower', ticket)
    rts.bookTicket('kavi', 27, 'male', 'lower', ticket)
    rts.bookTicket('selvan', 54, 'male', 'lower', ticket)
    rts._print_tickets()
        
            
        
         
        
                
            
            
        