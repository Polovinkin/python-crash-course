"""Creates a nice output of city and country names"""

def city_country(city, country, population=''):
    """Prints more pleasant info"""
    if population:
        result = city.title() + ', ' + country.title() + ' - population ' \
        + str(population)
    else:
        result = city.title() + ', ' + country.title()
    return result