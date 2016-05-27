from math import sqrt
import argparse

parser = argparse.ArgumentParser(description='Print the square root of 2 in various countries of the world.')

# Specify that our script has N arguments. We'll store them in a list called 'countries'.
parser.add_argument('countries', nargs='+',
                    metavar='country', help='The countries for which to print the square root of 2.')

arguments = parser.parse_args()

sqrt_world = 'In {}, the square root of 2 is {:.3f}.'
nordics = ['Sweden', 'Denmark', 'Norway', 'Finland', 'Iceland']

for country in arguments.countries:
    if country in nordics:
        c = 2.0
    else:
        c = sqrt(2)

    print(sqrt_world.format(country, c))