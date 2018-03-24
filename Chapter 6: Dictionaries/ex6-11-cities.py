cities = {
    'saint-petersburg': {
        'country': 'russia',
        'population': 5000000,
        'fact': 'cultural capital of Russia'
    },
    'london': {
        'country': 'england',
        'population': 8700000,
        'fact': 'nice and expensive city'
    },
    'amsterdam': {
        'country': 'netherlands',
        'population': 825000,
        'fact': 'city for bike lovers'
    },
    'barcelona': {
        'country': 'spain',
        'population': 1600000,
        'fact': 'city with great architecture, food and weather'
    },
}

for city, info in cities.items():
    print('The city is called ' + city.title() + '.')
    print('\tIt is situated in ' + info['country'].title() + '.')
    print("\tIt's population is " + str(info['population']) + '.')
    print("\tIt's known as a " + info['fact'] + '!')