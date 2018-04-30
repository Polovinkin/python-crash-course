filename = 'python_can.txt'

with open(filename) as opened_file:
    contents = opened_file.readlines()

the_list = ''

for line in contents:
    the_list += line

print(the_list)