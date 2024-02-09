#Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations
s = str(input())

def permutation(s):
    words = [''.join(p) for p in permutations(s)]
    print(words)

permutation(s)
