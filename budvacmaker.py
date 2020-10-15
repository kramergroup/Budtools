#!/usr/bin/env python3

# TODO - uhm shift all atoms upward so that they are centered within c after the scaling. A bit a way and not sure how
#  that effects things as of yet. allow args to be used as you go could be cool
#


import os
import sys


def budvacmaker(inputfile, stepsize=1, numberofsteps=12, outputdir=None):
    """
    Some time in 2020;

    A tool to vary the c dimension of a system with the intent of increasing vaccuum of slabs,
    This occurs along the c dimension and on a c centred slab so try and only put c centered slabs in here please.
    Also will only work on systems that have the cartesian flag on line 4/5 since that makes all the math like 1billion
    times easier. If you dont have it in cart form pass it to dir2cart first.

    """
    from pymatgen import Structure

    if outputdir == None:  # Setting the outputdir == to the inputdir if none is supplied.
        outputdir = '/'.join(inputfile.split('/')[0:-1]) + '/bvm'

    f = open(inputfile)
    stru = Structure.from_file(inputfile)
    string = []  # File writing to list
    for lines in f:
        string.append(lines)

    # Read the clear important c dimension and vary c3. Since that's likely to be the one.

    for i in string[1:9]:  # Check to see if in cart format.
        if i == 'cartesian\n':
            print('cart line found')
            checker = 1

    if checker != 1:  # Crash if not. Saves the difficult stuff.
        print('no cart line found, dying now')
        exit()

    if 89.995 < stru.lattice.angles[2] < 90.005 == False:  # Check to see a/b
        print("abnormal c angle, it's best not to use this poorly made script dying now. ")
        exit()

    for i in range(1, numberofsteps + 1):  # Initialising the range of steps and changing line 4 of the string. (c dim)
        os.makedirs('{}/{}'.format(outputdir, i), exist_ok=True)
        cdim = string[4].split()
        cdim[2] = str(float(cdim[2]) + i * stepsize)
        cdimstring = ' '.join(cdim) + '\n'
        string[4] = cdimstring

        with open('{}/{}/POSCAR'.format(outputdir, i), 'w') as outfile:
            print('writing to {}/{}/POSCAR'.format(outputdir, i))
            for line in string:
                outfile.write(line)
        # float(string[4].split()[-1]) + numberofsteps * stepsize

if __name__ == "__main__":
    budvacmaker(sys.argv[1])
