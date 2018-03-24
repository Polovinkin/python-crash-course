favourite_languages = {
    'dmitry': ['python', 'sql'],
    'grigory': ['c#', 'python'],
    'edward': ['c++', 'haskell'],
    'guido': ['python', 'c'],
}

for name, languages in favourite_languages.items():
    print('\n' + name.title() + "'s favourite languages are:")
    for language in languages:
        print('\t' + language.title())