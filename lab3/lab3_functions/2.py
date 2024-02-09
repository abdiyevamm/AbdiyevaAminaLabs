"""Read in a Fahrenheit temperature.
Calculate and display the equivalent centigrade temperature.
The following formula is used for the conversion: C = (5 / 9) * (F – 32)"""

def temp(f_temp):
    c_temp= (5/9)*(f_temp-32)
    return c_temp

f_temp=int(input())
print(temp(f_temp))

