vasya = {
    'name': 'vasya',
    'kind': 'cat',
    'owner': 'nina',
}

markiz = {
    'name': 'markiz',
    'kind': 'cat',
    'owner': 'dmitry',
    }

buddy = {
    'name': 'buddy',
    'kind': 'dog',
    'owner': 'daniil',
}

pets = [vasya, markiz, buddy]

for pet in pets:
    print(pet['owner'].title() + ' has a nice ' + pet['kind'] +
    ' which name is ' + pet['name'].title() + '.')