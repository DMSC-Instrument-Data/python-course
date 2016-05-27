from math import sqrt
import argparse

# Create a so called parser for the command line arguments.
# The parser stores the argumeents and generates some useful help for users of the script.
parser = argparse.ArgumentParser(description='Print the square root of 2 in various countries of the world.')

# Specify that our script has one argument. We'll store it in a variable called 'country'.
parser.add_argument('country', help='The country for which to print the square root of 2.')

# This bit scans the command line arguments and checks if it finds what we specified.
# If a country was specified, it is stored in arguments.country
arguments = parser.parse_args()

# We still have the same variables as before.
sqrt_world = 'In {}, the square root of 2 is {:.3f}.'
c = sqrt(2)

print(sqrt_world.format(arguments.country, c))