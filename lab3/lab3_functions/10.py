"""Write a Python function that takes a list
and returns a new list with unique elements of the first list. Note: don't use collection set."""

initial = input().split()

def unique(initial):
    new = []

    for i in initial:
        if i not in new:
            new.append(i)
    return new

print(unique(initial))