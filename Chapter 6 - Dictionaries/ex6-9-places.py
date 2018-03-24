favourite_places = {
    'mike': ['london', 'chicago', 'sydney'],
    'steven': ['home', 'sofa', 'tv'],
    'dmitry': ['copenhagen', 'london', 'new york', 'valencia']
}

for name, places in favourite_places.items():
    print(name.title() + "'s favourite places are:")
    for place in places:
        print('\t' + place.title())