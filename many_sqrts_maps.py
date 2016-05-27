from math import sqrt
import argparse

def nordic_sqrt(x):
    return 2*x - 0.5

def baltic_sqrt(x):
    return x/2 + 0.5

def get_country_sqrt_map(countries, sqrt_function):
    return {country: sqrt_function for country in countries}

parser = argparse.ArgumentParser(description='Print the square root of 2 in various countries of the world.')

# Specify that our script has N arguments. We'll store them in a list called 'countries'.
parser.add_argument('countries', nargs='+',
                    metavar='country', help='The countries for which to print the square root of 2.')

arguments = parser.parse_args()

sqrt_world = 'In {}, the square root of 2 is {:.3f}.'

nordics = ['Sweden', 'Denmark', 'Norway', 'Finland', 'Iceland']
baltics = ['Estonia', 'Latvia', 'Lithuania']

sqrt_map = {}
sqrt_map.update(get_country_sqrt_map(nordics, nordic_sqrt))
sqrt_map.update(get_country_sqrt_map(baltics, baltic_sqrt))

for country in arguments.countries:
    sqrt_function = sqrt_map.get(country, sqrt)

    print(sqrt_world.format(country, sqrt_function(2)))