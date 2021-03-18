from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self,side):
        pass

    @abstractmethod
    def parameter(self,side):
        pass


class Square(Shape):
    def area(self,side):
        return side*side

    def parameter(self,side):
        return 4*side

shape = Square()
print(shape.area(4))