# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example pro-
# grams from this chapter, and extend it by adding new keys and values, chang-
# ing the context of the program, or improving the formatting of the output.

cities = {
    'shanghai': {
        'country': 'china',
        'population': 3000_0000,
        'fact':'rich',
    },
    'guangzhou': {
        'country': 'china',
        'population': 2000_0000,
        'fact': 'delicious',
    },
    'washington': {
        'country': 'america',
        'population': 100_0000,
        'fact': 'political',
    }
}

for city, info in cities.items():
    print(f'{city}:')
    for field,value in info.items():
        print(f'\t{field}: {value}')

cities['hangzhou'] = {
    'country': 'china',
    'population': 1000_0000,
    'fact': 'endless work',
}

print('\nnew cities')
for city, info in cities.items():
    print(f'{city}:')
    for field,value in info.items():
        print(f'\t{field}: {value}')
