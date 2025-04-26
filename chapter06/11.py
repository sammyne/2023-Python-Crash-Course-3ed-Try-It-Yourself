# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.

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
