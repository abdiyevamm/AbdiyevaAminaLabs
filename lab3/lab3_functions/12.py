"""Define a function histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:"""

l = input().split()

def histogram(l):
    for x in l:
        print("*" * int(x))

histogram(l)