filename = 'python_can.txt'

with open(filename) as opened_file:
    contents = opened_file.readlines()

for line in contents:
    print(line.strip())
