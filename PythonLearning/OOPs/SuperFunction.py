class Vehicle:  # defining the parent class
    fuelCap = 90

    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def display(self):  # defining diplay method in the parent class
        print("I am from the Vehicle Class")


class Car(Vehicle):  # defining the child class
    fuelCap = 50

    def __init__(self, make, color, model,doors):
        # calling parent's class init method to initialize its public variables
        # self variable not required
        super().__init__(make, color, model)

        # This can also be done using class name
        # self variable is required
        Vehicle.__init__(self, make, color, model)
        
        self.doors = doors

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap)
        # access display method of parent class
        super().display()

        # accessing fuelCap from the Vehicle class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()