from Vehicle import Vehicle

class Car(Vehicle):
    def __str__(self):
        base = super().__str__()
        return f"""I'm a car 
{base}
        """
        


car = Car()
car.name = "First Car"
car.mass = -100
print(car.mass)
car.mass = 50
print(car.mass)

car.drive()
car.turn_left()
car.drive()
print(car)

car2 = Car()
car2.name = "Second Car"
print(car)

v1 = Vehicle()
print(v1)