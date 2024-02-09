"""Write the definition of a Point class. Objects from this class should have a
a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points """

class Point:

    def __init__(self,corx,cory):
        self.corx=corx
        self.cory=cory

    def show(self):
        print(f'{self.corx} {self.cory}')

    def move(self):
        a=list(map(int,input().split()))
        self.corx=a[0]
        self.cory=a[1]

    def dist(self):
        s=list(map(int,input().split()))
        print(((self.corx-s[0])**2+(self.cory-s[1])**2)**0.5)

b=list(map(int,input().split()))

r=Point(b[0],b[1])

r.dist()