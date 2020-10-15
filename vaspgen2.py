import datetime
from pt import pt
import getopt
import sys
import json

jsonfile = {}

JSON = {
    "potcardirectory": "/Users/budmacaulay/POT_GGA_PAW_PBE/",
    "initialincar": "/Users/budmacaulay/Desktop/surfaces/Co/441-10vac/INCAR",
    "kpointscheme": "Monkhorstpack",
    "kpoints": [6, 6, 6]
}


def vaspgen(inputstructure, jsonfile=JSON):  # Small wrapped for the stuff above.

    print('reading structure using pymatgen')
    if jsonfile.get("potcardirector"):
        potcarfromposcar(inputstructure, potcardir=jsonfile.get('potcardirectory'))

        kpointsfromposcar(inputstructure, jsonfile.kpoints)

    if jsonfile.get('initialincar'):
        print('Making the INCAR from POSCAR and file in config labelled initialincar')
        incarfromposcar(inputstructure, initialincar=jsonfile.get('initialincar'))

