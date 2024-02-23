from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Trianlge(Shape):
    def __init__(self,length,base):
        self.length=length
        self.base=base
    def area(self):
        return 0.5 * self.base *self.length
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length ** 2
class Pentagon(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.length ** 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
T1=Trianlge(23,45)
S1=Square(2)
P1=Pentagon(4)
C1=Circle(2)
print(f"Area of Triangle :{T1.area()}")
print(f"Area of Square :{S1.area()}")
print(f"Area of Pentagon :{P1.area()}")
print(f"Area of Circle :{C1.area()}")