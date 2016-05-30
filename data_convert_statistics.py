import argparse
from math import sqrt

parser = argparse.ArgumentParser(description='Read a file with 3 space separated columns, calculate an error estimate from the second column and write the modified file.')

parser.add_argument('input', help='Name of the input file.')
parser.add_argument('output', nargs='?', default=None,
                    help='Name of the output file.')
parser.add_argument('-s', '--square-root-errors', action='store_true', default=False,
                    help='Calculate errors as sqrt(|y|), otherwise leave errors unmodified.')               
parser.add_argument('-p', '--print-statistics', action='store_true', default=False,
                    help='Calculate and print some statistics from the data.')


arguments = parser.parse_args()

x_data = []
y_data = []
e_data = []

infile = open(arguments.input, 'r')

# Go through the file line by line
for line in infile:
    # Remove whitespace characters at the beginning and end
    stripped_line = line.strip()
    
    # If it's not a comment and not an empty line, try to convert it to three floats.
    if not stripped_line.startswith('#') and not len(stripped_line) == 0:
        x, y, e = [float(x) for x in line.split(' ')]
        
        x_data.append(x)
        y_data.append(y)
        e_data.append(e)
    
infile.close()

if arguments.square_root_errors:
    e_data = [sqrt(abs(y)) for y in y_data]

if arguments.output is not None:
    lineformat = '{:.6g} {:.6g} {:.6g}\n'

    outfile = open(arguments.output, 'w')

    for x, y, e in zip(x_data, y_data, e_data):
        outfile.write(lineformat.format(x, y, e))
        
    outfile.close()

if arguments.print_statistics:
    print('Statistics for file {}:'.format(arguments.input))
    
    number_of_points = len(x_data)
    print('Number of data points: {}'.format(number_of_points))
    
    print('x-range: {:.6g} - {:.6g}'.format(min(x_data), max(x_data)))
    print('y-range: {:.6g} - {:.6g}'.format(min(y_data), max(y_data)))
    
    mean_y = sum(y_data) / number_of_points    
    print('Mean y: {:.6g}'.format(mean_y))
    
    median_y = sorted(y_data)[int(number_of_points/2)]
    print('Median y: {:.6g}'.format(median_y))
    
    if not 0.0 in e_data:
        mean_i_over_sigma = sum([abs(y) / e for y, e in zip(y_data, e_data)]) / number_of_points
        print('Mean I/sigma: {:.6g}'.format(mean_i_over_sigma))
    else:
        print('Mean I/sigma: Inf')