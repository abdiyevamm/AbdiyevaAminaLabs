import re
def match(str):
    ref = r'.*ab{2,3}'
    mach = re.fullmatch(pattern=ref, string=str)
    if mach is None:
        return False
    else:
        return True


str = input("Enter text:")
print(match(str))