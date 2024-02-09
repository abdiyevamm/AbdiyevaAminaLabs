"""You are given list of numbers separated by spaces.
Write a function filter_prime which will take list of numbers as an argument
and returns only prime numbers from the list."""

mylist = input().split()
for i in range(len(mylist)):
    mylist[i]=int(mylist[i])

def filter_prime(mylist):
    t = []
    for j in mylist:
        cnt=0
        for i in range(2, j):
            if j%i==0:
                cnt+=1
        if cnt==0:
            t.append(j)
    return t

print(filter_prime(mylist))