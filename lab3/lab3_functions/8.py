# Write a function that takes in a list of integers and returns True if it contains 007 in order

a=input().split()

def spy_game(a):
    a= "".join(a)

    if "007" in a:
        return True
    else:
        return False

print(spy_game(a))