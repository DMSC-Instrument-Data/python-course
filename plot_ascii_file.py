import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Plot the supplied file.')

parser.add_argument('input', help='Name of the input file.')

arguments = parser.parse_args()

x,y,e = np.loadtxt(arguments.input, unpack=True)

plt.errorbar(x,y,e)
plt.show()