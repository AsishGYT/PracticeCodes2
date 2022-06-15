#OOPS - Python
#Create a Class with instance attributes

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle("bus", 240, 18)
#print(modelX.max_speed, modelX.mileage)


#Create a Vehicle class without any variables and methods

class VehicleNill:
    pass

#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Bus(Vehicle):
    pass

School_bus = Bus("Volvo", 180, 12)
#print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

#Class Inheritance

class Vehicle2:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle2):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("Volvo", 180, 12)
#print(School_bus.seating_capacity())



#Define a property that must have the same value for every class instance (object)

class Vehicle3:

    color = "Royal Blue"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle3):
    pass

class Car(Vehicle3):
    pass

School_bus = Bus(" Volvo", 180, 12)
print("color:", School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print("color:", car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)


#Class Inheritance

class Vehicle4:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle4):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus(" Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

print(type(School_bus))
print(isinstance(School_bus, Vehicle4))
