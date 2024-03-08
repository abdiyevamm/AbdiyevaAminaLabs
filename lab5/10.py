import re
def conversion(str):
    words = re.finditer(r'[A-Z]', str)
    newstr = ""
    pos = 0
    for x in words:
        newstr += str[pos:x.start()].lower() + "_"
        pos = x.start()
    newstr += str[pos:].lower()
    return newstr


str = input("Enter text:")
print(conversion(str))