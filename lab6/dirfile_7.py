def copy_file(sourcefile, destinationfile):
    with open(sourcefile, 'r') as source, open(destinationfile, 'w') as destination:
        destination.write(source.read())
    print(f'Contents of ', {sourcefile}, ' copied to ', {destinationfile}, ' successfully.')


sourcefile = 'text.txt'
destinationfile = 'smthelse.txt'
copy_file(sourcefile, destinationfile)