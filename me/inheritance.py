# Inheritance allow one class (child) to take properties and methods

class Car:
    def __init__(self, make, model, year):
        self.make= make
        self.model= model
        self.year= year
    def start_engine(self):
        return f"{self.make} {self.model} engine has started"
    
    def stop_engine(self):
        return f"{self.make} {self.model} engine has stoped"
    
class ElectricCar(Car):
    def __init__(self, make, model, year, bettery_capacity):
        super().__init__(make, model, year,)
        self.bettery_capacity = bettery_capacity

    def charge(self):
        return f"charging {self.make} {self.model} with a {self.bettery_capacity} kwh bettery"
    
    if __init__ == "__main__":
        my_car = Car("Toyota","Corrala", 2020)
        print(my_car.start_engine())
        print(my_car.stop_engine())

my_electric_car = ElectricCar("Tesla", "model", 2020, 75)
print(my_electric_car.charge())
print(my_electric_car.start_engine())
print(my_electric_car.stop_engine())
