from abc import ABC, abstractmethod

# Methods with @abstractmethod decorators must be defined either in the parent class or the child class.
class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Abstract methods must be defined in child classes for proper implementation of inheritance.
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


shape = Shape()
# this will code will not compile since Shape has abstract methods without
# method definitions in it

square = Square(4)
# this code will not generate an error since abastract methods have been
# defined in the child class, Square