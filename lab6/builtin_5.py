def truetuple(str):
    tup = [True if x == "True" else False for x in str]
    result = tuple(tup)
    print(all(result))

str = input("Enter tuple:").split(" ")
truetuple(str)