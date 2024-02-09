""" Write a program to solve a classic puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
create function: solve(numheads, numlegs):
"""

numheads = int(input())
numlegs = int(input())

def solve(numheads, numlegs):
    r = int((numlegs - 2 * numheads)/2)
    c = int(numheads - r)
    print("chickens: ", c)
    print("rabbits: ", r)

solve(numheads, numlegs)