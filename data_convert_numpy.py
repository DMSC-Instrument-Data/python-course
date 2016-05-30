import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Read a file with 3 space separated columns, calculate an error estimate from the second column and write the modified file.')

parser.add_argument('input', help='Name of the input file.')
parser.add_argument('output', nargs='?', default=None,
                    help='Name of the output file.')
parser.add_argument('-s', '--square-root-errors', action='store_true', default=False,
                    help='Calculate errors as sqrt(|y|), otherwise leave errors unmodified.')               
parser.add_argument('-p', '--print-statistics', action='store_true', default=False,
                    help='Calculate and print some statistics from the data.')


arguments = parser.parse_args()

x_data, y_data, e_data = np.loadtxt(arguments.input, unpack=True)

if arguments.square_root_errors:
    e_data = np.sqrt(np.abs(y_data))

if arguments.output is not None:
    np.savetxt(arguments.output, np.array([x_data, y_data, e_data]).T, fmt='%.6g')

if arguments.print_statistics:
    print('Statistics for file {}:'.format(arguments.input))
    
    number_of_points = len(x_data)
    print('Number of data points: {}'.format(number_of_points))
    
    print('x-range: {:.6g} - {:.6g}'.format(min(x_data), max(x_data)))
    print('y-range: {:.6g} - {:.6g}'.format(min(y_data), max(y_data)))
    
    mean_y = np.mean(y_data)
    print('Mean y: {:.6g}'.format(mean_y))
    
    median_y = np.median(y_data)
    print('Median y: {:.6g}'.format(median_y))
    
    if not 0.0 in e_data:
        mean_i_over_sigma = np.mean(np.abs(y_data) / e_data)
        print('Mean I/sigma: {:.6g}'.format(mean_i_over_sigma))
    else:
        print('Mean I/sigma: Inf')