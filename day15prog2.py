#create a bus child class that inherits from the vehicle class
class Vehicle:
    def __init__(self, name,max_speed, mileage,):
        self.name = name
        self.max_speed=max_speed
        self.mileage=mileage

    
class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo",180,12)
print("vehicle name:", School_bus.name,"speed:",
      School_bus.max_speed,"mileage:",School_bus.mileage)
