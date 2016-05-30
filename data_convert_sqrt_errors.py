import argparse
from math import sqrt

parser = argparse.ArgumentParser(description='Read a file with 3 space separated columns, calculate an error estimate from the second column and write the modified file.')

parser.add_argument('input', help='Name of the input file.')
parser.add_argument('output', help='Name of the output file.')

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

e_data = [sqrt(abs(y)) for y in y_data]

lineformat = '{:.6g} {:.6g} {:.6g}\n'

outfile = open(arguments.output, 'w')

for x, y, e in zip(x_data, y_data, e_data):
    outfile.write(lineformat.format(x, y, e))
    
outfile.close()
