class Taxi:
    taxiId = 0
    
    def __init__(self):
        Taxi.taxiId += 1
        self.taxi_id = Taxi.taxiId
        self._pickup_time = 0
        self._total = 0
        self._point = "A"
        self._trip = []
        
    def is_available(self, pick_time):
        return self._pickup_time < pick_time
        
    def add_trip(self, trip: Trip):
        self._trip.append(trip)
        self._pickup_time = trip.drop_time
        self._point = trip.drop
        self._total += trip.amount
        
class Trip:
    
    def __init__(self, booking_id: str,
                 customer_id: str,
                 pick: str,
                 drop: str,
                 pick_time: int,
                 drop_time: int,
                 amount: float
                 ):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.pick = pick
        self.drop = drop
        self.pick_time = pick_time
        self.drop_time = drop_time
        self.amount = amount
        
class BookingEngine:
    POINTS = ['A', 'B', 'C', 'D', 'E', 'F']
    KM = 15
    HR = 1
    bookingId = 0
    cusotmerId = 0
    
    def __init__(self, no_of_taxi):
        BookingEngine.bookingId += 1
        BookingEngine.cusotmerId += 1
        self.taxies = [Taxi() for _ in range(no_of_taxi)]
        self.booking_id = BookingEngine.bookingId
        self.customer_id = BookingEngine.cusotmerId
        
    @classmethod
    def calculate_distance(cls, sta1, sta2) -> int:
        idx1 = cls.POINTS.index(sta1)
        idx2 = cls.POINTS.index(sta2)
        return abs(idx1-idx2) * cls.KM
    
    @classmethod
    def calculate_amount(cls, distance) -> int:
        if distance <= 5:
            return 100
        return 100 + ((distance-5)*10)
        
    def bookTaxi(self, pick, drop, pick_time):
        
        available_taxies = [taxi for taxi in self.taxies if taxi.is_available(pick_time)]
        
        if not available_taxies:
            return None
        
        pick_taxies = min(available_taxies, key=lambda x: (abs(self.POINTS.index(x._point) - self.POINTS.index(pick)), 
                                                           x._total, 
                                                           x.taxiId))
        
        distance = BookingEngine.calculate_distance(pick, drop)
        new_amount = BookingEngine.calculate_amount(distance)
        
        new_trip = Trip(
            booking_id=self.booking_id,
            customer_id=self.customer_id,
            pick=pick,
            drop=drop,
            pick_time=pick_time,
            drop_time=pick_time+abs(self.POINTS.index(pick_taxies._point) - self.POINTS.index(drop)),
            amount=new_amount
        )
        pick_taxies.add_trip(new_trip)
        
        print(pick_taxies.__dict__)
        
if __name__ == "__main__":
    be = BookingEngine(4)
    be.bookTaxi("A", "B", 9)
        
        
    
        
        
            
            
            
        
        
    