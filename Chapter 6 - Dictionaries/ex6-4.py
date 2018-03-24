glossary = {
    'selection': 'filters horisontally, removes rows',
    'projection': 'filters vertically, removes columns',
    'natural join': 'emforces equality on all attr. with the same name',
    'union': 'gathers all the elements together',
    'intersection': 'leaves only those which are both there and there',
    'difference': 'leaves only the unique elements',
    }

for definition in sorted(glossary.values()):
    print('I know the word for query that ' + definition + '.')

