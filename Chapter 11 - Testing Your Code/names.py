from name_function import get_formatted_name

print("Enter 'q' any time to quit.")
while True:
    first = input('Give me the first name: ')
    if first == 'q':
        break
    last = 'Gimme the last name: '
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print('\tNeatly formatted name: ' + formatted_name + '.')