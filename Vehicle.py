class Vehicle:
        
    def __init__(self):
        self.coords = (0, 0)
        self.v = (1, 0)
        self.__m = 100
        self.name = "Untitled"
        print("Vehicle created")
    
    @property
    def mass(self):
        return self.__m
    
    @mass.setter
    def mass(self, mass):
        if mass > 0:
            self.__m = mass
    
    
    def drive(self):
        self.coords = (self.coords[0]+self.v[0],self.coords[1]+self.v[1]) 
        print(f"i'm {self.name} driving")

    def turn_left(self):
        self.v = (-self.v[1], self.v[0])
        print(f"i'm {self.name} turning left")

    def turn_right(self):
        self.v = (self.v[1], -self.v[0])
        print(f"i'm {self.name} turning right")

    def __str__(self):
        return f"V={self.v} coords={self.coords} name={self.name}"
    