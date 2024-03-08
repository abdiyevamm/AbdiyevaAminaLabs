import re
def sequence(str):
    ref = r'[a-z](?:_[a-z])*'
    mach = re.fullmatch(pattern=ref, string=str)
    if mach is None:
        return False
    else:
        return True


str = input("Enter text: ")
print(sequence(str))