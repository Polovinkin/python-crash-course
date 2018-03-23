favourite_languages = {
    'dmitry': 'python',
    'grigory': 'c#',
    'edward': 'c++',
    'guido': 'python',
}

print('The following languages have been mentioned:')
for language in set(favourite_languages.values()):
    print(language.title())