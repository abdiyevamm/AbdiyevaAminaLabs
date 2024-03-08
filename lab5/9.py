import re
def insert(str):
    words = re.finditer(r'[A-Z]', str)
    newstr = ""
    pos = 0
    for x in words:
        newstr += str[pos:x.start()] + " "
        pos = x.start()
    newstr += str[pos:]
    return newstr


str = input("Enter text:")
print(insert(str))