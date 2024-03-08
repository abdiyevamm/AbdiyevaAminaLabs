import math
import time
def square(n, b):
    n = int(n)
    x = float(math.sqrt(n))
    time.sleep(int(b)/1000)
    print(f'Square root of {n} after {b} milliseconds is {x}')



n = input("Enter number ro find root:")
b = input("Enter milliseconds:")
square(n, b)