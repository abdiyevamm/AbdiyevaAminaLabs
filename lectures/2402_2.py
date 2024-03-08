import re
s = "ACDC/ACDC/The rain in Spain"

print(len(re.findall("AC", s))) #сколько раз встречается АС в строке эс

print(re.search("AC", s))

print(re.sub("AC", "DC", s))

#split function
