import argparse
import numpy as np
import matplotlib.pyplot as plt

def get_q(hkl, g_star):
    return 2 * np.pi * np.sqrt(hkl.T.dot(g_star.dot(hkl)))

def get_g_star(a):
    return np.eye(3) * 1/a**2

parser = argparse.ArgumentParser(description='Plot the supplied file.')

parser.add_argument('input', help='Name of the input file.')
parser.add_argument('output', nargs='?', default=None,
                    help='If supplied, write plot to this file instead of displaying')
parser.add_argument('-a', help='Lattice parameter of a cubic crystal structure in Angström.', type=float)
parser.add_argument('-m', help='Miller indices HKL given in the format h,k,l.')

arguments = parser.parse_args()

x,y,e = np.loadtxt(arguments.input, unpack=True)

plt.errorbar(x,y,e,fmt='.')
plt.xlabel('Q')
plt.ylabel('I')

if arguments.a is not None and arguments.m is not None:
    hkl = np.array([float(x) for x in arguments.m.split(',')])
    
    g_star = get_g_star(arguments.a)
    q = get_q(hkl, g_star)
    
    xlimits = (q-0.05, q+0.05)
    
    plt.title('HKL = ' + arguments.m)
    plt.xlim(xlimits)

if arguments.output is not None:
    plt.savefig(arguments.output)
else:
    plt.show()