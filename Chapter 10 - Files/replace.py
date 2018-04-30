my_file = 'python_can.txt'

with open(my_file) as opened_file:
    readed = opened_file.read()

print(readed.replace('Python', 'C'))