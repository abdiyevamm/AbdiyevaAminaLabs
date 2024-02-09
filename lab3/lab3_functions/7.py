# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

a=input().split()

def has_33(a):

    a = ''.join(a)
    if '33' in a:
        return True
    else:
        return False
print(has_33(a))