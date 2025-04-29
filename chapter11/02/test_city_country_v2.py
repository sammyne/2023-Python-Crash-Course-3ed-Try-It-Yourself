# 11-2. Population: Modify your function so it requires a third parameter, population.
# It should now return a single string of the form City, Country – population xxx,
# such as Santiago, Chile – population 5000000. Run the test again, and make sure
# test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run the test,
# and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies
# you can call your function with the values 'santiago', 'chile', and 'population
# =5000000'. Run the tests one more time, and make sure this new test passes.

from city_functions import city_country

def test_city_country():
    got = city_country('shenzhen', 'china')
    assert 'Shenzhen China' == got

def test_city_country_v2():
    got = city_country('shenzhen', 'china', 5000_0000)
    assert 'Shenzhen China - population 50000000' == got
