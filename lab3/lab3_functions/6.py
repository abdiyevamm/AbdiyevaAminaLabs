""" Write a function that accepts string from user,
return a sentence with the words reversed. We are ready -> ready are We """

s=input().split()
def reverse(s):
    s = s[::-1]
    return s

print(reverse(s))

