import i_functions
import os
# workdir = '/Users/budmacaulay/Desktop/1tnv'
# potcardir = '/Users/budmacaulay/POT_GGA_PAW_PBE/'

# workdir = 'your/directory/to/work/over'
# potcardir = 'your/potcar/directory/POT_GGA_PAW_PBE/'

# Checking my function calls work! -
# slabsets is a bit dodgy and i'm unsure why -> based on how it defines 'layers' I guess.
i_functions.slabsets('/Users/budmacaulay/Desktop/BULK/POSCAR', '/Users/budmacaulay/Desktop/thurbulk/surfaces', [1, 0, 4], vacmin=15, vacmax=15, numberoflayers=9)

i_functions.pos2pot(workdir, potcardir)

i_functions.pos2inc(workdir, '/Users/budmacaulay/Desktop/RESUBMIT/s100_9lay/INCAR') # This is outdated use the below 1
i_functions.pos2inc2(workdir, '/Users/budmacaulay/Desktop/RESUBMIT/s100_9lay/INCAR', verbose=True) # Has a full
# print-out option incase something goes wrong ! needs testing

i_functions.kpointer(workdir, '/Users/budmacaulay/Desktop/RESUBMIT/s100_9lay/KPOINTS')

for subdir, dirs, files in os.walk(str(workdir)):
    for file in files:
        if file.endswith('POSCAR'):
            i_functions.dyna(subdir + '/POSCAR', 'bulk')

i_functions.qscript2folder(workdir, '/Users/budmacaulay/PycharmProjects/Budtools/qscriptsstuff')

i_functions.json2folder(workdir)

i_functions.tabluateitall('/Users/budmacaulay/Desktop/newtestssss/removed')

# If you want the structure returned to you for further transformations.
suppy = i_functions.supers('/Users/budmacaulay/Desktop/nuu/POSCAR', workdir, [2, 2, 2])

# the subs function works a little different but will need a structure as an input (It was easier this way as it
# allowed to use the super function at the same time)

# i_functions.bulksub(suppy, 'Co', 'Mn', outputdir='/OUTPUT/DIR')
# i_functions.surfsub(suppy, 'species_toswap', 'swapwiththis', outputdir='/OUTPUT/DIR')

# If you need to call the subs structure without a structure input (i.e want to use a .cif pmg handles that)

# inputstructure = Structure.from_file(inputfile)
# i_functions.bulksub(inputstructure, 'Co', 'Mn', outputdir='/OUTPUT/DIR')

i_functions.vasp2onetep(workdir, '/Users/budmacaulay/Desktop/pycoderun/test.dat') # Needs some tests

i_functions.supers('/Users/budmacaulay/Desktop/19april/19april/104vac5/test.xyz', '/Users/budmacaulay/Desktop/19april/19april/104vac5/2x', [2,2,1])


# TODO - make a onetep qscript thinggy - seems like effort tbh, as of current just porting my current one over seems
#  easier

for i in [5, 7, 9, 11, 13, 15, 17, 19, 21]:
    i_functions.slabsets('/Users/budmacaulay/Desktop/LCOotbulk/bulk/POSCAR',
                         '/Users/budmacaulay/Desktop/cubic/surf2', [1, 0, 4], vacmin=i, vacmax=i,
                         numberoflayers=7)

for i in [5, 7, 9 ,11, 13, 15, 17, 19, 21]:
    i_functions.supers('/Users/budmacaulay/Desktop/cubic/surf2/104vac' + str(i) + '/POSCAR',
                       '/Users/budmacaulay/Desktop/cubic/surf2/104vac' + str(i) + '/', [2, 4, 1])

for i in [[3,3,1], [4,4,1]]:
    i_functions.supers('/Users/budmacaulay/Desktop/LCOotbulk/bulk/POSCAR', workdir, i)


for i in ['221', '331', '441']:
    i_functions.onetepdyna('/Users/budmacaulay/Desktop/fixedcode/ONETEPMAKER/sup{}/automade.dat'.format(i), initiallayers=7, style=2, verbose=False)

for i in [5,7,9,11,13,15,17,19,21]:
    i_functions.onetepdyna('/Users/budmacaulay/Desktop/cubic/surf2/ONETEPMAKER/104vac{}/automade.dat'.format(i),
                           initiallayers=7, style=2, verbose=False)