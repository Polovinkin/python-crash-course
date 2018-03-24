rivers = {
    'neva': 'russia',
    'nile': 'egypt',
    'yangtze': 'china',
    'missouri': 'usa'
}

for river, country in rivers.items():
    if country is 'usa':
        print('The ' + river.title() + ' flows in the ' + country.upper() + '.')
    else:
        print('The ' + river.title() + ' flows in the ' + country.title() + '.')

print('\nSome of the largest rivers in the world are:')
for river in sorted(rivers):
    print(river.title())
