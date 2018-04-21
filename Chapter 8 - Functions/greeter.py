def get_formatted_name(first_name, second_name):
    """Return formatted name"""
    full_name = first_name + ' ' + second_name
    return full_name.title()

while True:
    print('\nPleast, tell me your name!')
    print('(Enter "q" any time to quit!')

    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('Hello, ' + formatted_name + '!')