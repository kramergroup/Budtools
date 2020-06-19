import sys

def dir2cart(inputfile):

    """
    Some time in 2020;

    Checks if the line of text is direct or Direct within a poscar. If so converts it to cartesian.
     If for some reason you've saved a poscar a with the particular line as D or d i'm too lazy to fix that.
    """
    from pymatgen.core.structure import Structure
    f = open(inputfile)
    stru = Structure.from_file(inputfile)
    string = [] # File writing to list
    for lines in f:
        string.append(lines)

    listofcarts = stru.cart_coords.tolist() # Using pymatgen to get the cart co-ords since math sucks.

    for i in listofcarts:
        for k in i:
            k = round(k, 6)

    listofcarts = [[format(number, '.8f') for number in nested] for nested in listofcarts] # rounding and cleaning

    for check in [5, 6, 7, 8]: # Typical range for the cart/direct distinction.
        if string[check].lower() == 'direct\n':
            print('converting direct to cart!')
            string[check] = 'cartesian\n'
            j = check + 1 # methods of stripping all the atoms later
            k = check + 1 # ^^
            checking = '1'

    if checking == None:
        print('no direct line found. exiting now')
        exit()
    # Checking to makesure that angle c is reasonably close to 90 or else some issues may occur upon stretching.
    stru = Structure.from_file(inputfile)

    while j < (k + len(listofcarts)):
        print(string[j])
        listofcarts[j-k].append(string[j].split()[3:])
        j += 1

    lofl =[]
    for i in listofcarts:
        print(i)
        i = [str(line) for line in i]
        lofl.append(i)

    j = k
    while j < (k + len(lofl)):
        print(j)
        print(lofl[j-k])
        string[j] = '\t'.join(lofl[j-k]) + '\n'
        j += 1

    with open(inputfile, 'w') as outfile:
        for line in string:
            outfile.write(line)

if __name__ == "__main__":
    dir2cart(sys.argv[1])

