import random
def calculate():
    return a*b*c

def f(a,b,c):
    for i in range(10):
        x=random.randint (1,10)
        y=random.randint (1,10)
        z=random.randint (1,10)
        yield calculate(x,y,z)

a=f(1,2,3)
