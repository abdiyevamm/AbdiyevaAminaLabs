"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
"""
class getstring:

  def __init__(self,string):
    self.string=string

  def getString(self):
    return self.string

  def printString(self):
    return self.string.upper()

p=getstring(input())

print(p.printString())