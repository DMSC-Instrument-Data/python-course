import argparse
import numpy as np
import scipy.optimize
import scipy.integrate
import matplotlib.pyplot as plt

def get_q(hkl, g_star):
    return 2 * np.pi * np.sqrt(hkl.T.dot(g_star.dot(hkl)))

def get_g_star(a):
    return np.eye(3) * 1/a**2

def gauss(x, x0, s, h):
    return h * np.exp(-0.5 * ((x-x0)/s)**2)

def background(x, x0, b, n):
    return b*(x-x0)**2 + n

def peak(x, x0, s, h, b, n):
    return gauss(x, x0, s, h) + background(x, x0, b, n)

def fit_peak(x_fit, y_fit, e_fit, q):
    # We need starting parameters in the same order as the peak function
    start_parameters = [q, 0.001, np.max(y_fit), 0, np.min(y_fit)]
    
    # Get the optimized parameters and the covariance matrix, supply relative errors.
    optimized_parameters, covariance_matrix = scipy.optimize.curve_fit(peak, x_fit, y_fit, p0=start_parameters,
                                                                       sigma=e_fit/y_fit)
    
    # Calculate sigmas for the optimized parameters
    parameter_errors = np.sqrt(np.diag(covariance_matrix))
    
    return optimized_parameters, parameter_errors

def print_parameters(parameters, errors, parameter_names):
    print('Fitted parameters:')
    for name, value, error in zip(parameter_names, parameters, errors):
        print('    {}: {:.6g} +/- {:.6g} ({:.2g} %)'.format(name, value, error, abs(error/value) * 100))
        
def get_integrated_intensity(peak_function, parameters):
    q, sigma = parameters[:2]
    
    # Integrate in the 4-sigma range.
    return scipy.integrate.quad(peak_function, q - 4*sigma, q + 4*sigma, args=tuple(parameters[:3]))[0]

parser = argparse.ArgumentParser(description='Plot the supplied file.')

parser.add_argument('input', help='Name of the input file.')
parser.add_argument('output', nargs='?', default=None,
                    help='If supplied, write plot to this file instead of displaying')
parser.add_argument('-a', help='Lattice parameter of a cubic crystal structure in Angstrom.', type=float)
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
    
    xlimits = (q-0.07, q+0.07)
    
    # Cut out the relevant part of the data (numpy advanced indexing)
    fit_data_indices = (x >= xlimits[0]) & (x <= xlimits[1])
    
    x_fit = x[fit_data_indices]
    y_fit = y[fit_data_indices]
    e_fit = e[fit_data_indices]
    
    parameters, errors = fit_peak(x_fit, y_fit, e_fit, q)
    
    print_parameters(parameters, errors,
                     ['Q(hkl)', 'Sigma', 'Height', 'Quadratic background', 'Offset'])
    
    integrated_intensity = get_integrated_intensity(gauss, parameters)
    print('Integrated intensity for {}: {:.4g}'.format(arguments.m, integrated_intensity))
    
    # Plot the fitted function
    y_calculated = peak(x_fit, *parameters)
    plt.plot(x_fit, y_calculated)    
    
    plt.title('HKL = ' + arguments.m)
    plt.xlim(xlimits)

if arguments.output is not None:
    plt.savefig(arguments.output)
else:
    plt.show()