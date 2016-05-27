from math import sqrt

a = 'Sweden'
b = 'Denmark'
c = sqrt(2)

sqrt_world = 'In {}, the square root of 2 is {:.3f}.'

print(sqrt_world.format(a, c))
print(sqrt_world.format(b, c))