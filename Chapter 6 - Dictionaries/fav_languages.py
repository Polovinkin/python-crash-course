from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['dmitry'] = 'python'
favourite_languages['grigory'] = 'c#'
favourite_languages['edward'] = 'c++'
favourite_languages['guido'] = 'python'

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is: " + language.title() + '.')