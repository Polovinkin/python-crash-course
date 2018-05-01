result = input('What is your name, bro?')

with open('guest.txt', 'w') as created_file:
    created_file.write(result)