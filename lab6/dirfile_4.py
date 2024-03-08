def count(filename):
    with open(filename, 'r') as file:
        lines = sum(1 for line in file)
    print(f"Number of lines in '{filename}': {lines}")

filename = 'text.txt'
lines = count(filename)