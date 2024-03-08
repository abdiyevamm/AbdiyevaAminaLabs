import os
filepath = "C:\Users\abdia\PycharmProjects\pp2\lab6\dirfile_2.py"
resExist = os.access(filepath, os.F_OK)
resWritability = os.access(filepath, os.W_OK)
resReadability = os.access(filepath, os.R_OK)
resExecutability = os.access(filepath, os.X_OK)
print(resExist, resWritability, resReadability, resExecutability)

