people = {
    'dpolovinkin': {
        'first': 'dmitry',
        'last': 'polovinkin',
        'city': 'saint-petersburg',
        'age': 23,
        },
    'emusk': {
        'first': 'elon',
        'last': 'musk',
        'city': 'palo-alto',
        'age': 46,
        },
    'dlewis': {
        'first': 'damian',
        'last': 'lewis',
        'city': 'london',
        'age': 47,
        }
}

for name, info in people.items():
    print('\nUsername: ' + name)
    print('\tFull Name: ' + info['first'].title() + ' ' + info['last'].title())
    print('\tHe is ' + str(info['age']) + ' years old and he lives in '
    + info['city'].title() + '.')