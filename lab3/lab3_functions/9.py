#Write a function that computes the volume of a sphere given its radius.

import math
r = float(input())

def volume_sphere(r):
    volume = (4/3)* math.pi * (r**3)
    return volume

print(volume_sphere(r))
