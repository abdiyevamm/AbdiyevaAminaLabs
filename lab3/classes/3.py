"""Define a class named Rectangle which inherits from Shape class from task 2.
Class instance can be constructed by a length and width.
The Rectangle class has a method which can compute the area."""

class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width
        super().__init__()

    def area(self):
        return self.length*self.width

a=list(map(int,input().split()))

s=Rectangle(a[0],a[1])

print(s.area())