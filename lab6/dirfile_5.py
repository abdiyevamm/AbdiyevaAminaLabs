def write_list_to_file(filename, mylist):
    with open(filename, 'w') as file:
        for x in mylist:
            file.write(str(x) + '\n')


mylist = [1, 2, 3, 4, 5]
filename = 'smthelse.txt'
write_list_to_file(filename, mylist)