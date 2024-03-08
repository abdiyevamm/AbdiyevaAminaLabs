import os
filepath = "C:\Users\abdia\PycharmProjects\pp2\lab6\dirfile_2.py"
resExist = os.access(filepath, os.F_OK)
if resExist == True:
    directory = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    print(f'File directory {directory}; File name: {filename}')