#!/usr/bin/env python3
"""Check if a ONETEP run converged from its .dat file.
Not sure if this currently exists for OT but maybe it does. There is no decent parser so will have to look for the printouts
that ONETEP prints on both complete and incomplete calculatons. - Should be a fairly decent task while I have limitted internet
"""

# Written this in a similar-ish way to andrea's one I guess.
import sys
from _collections import OrderedDict


def check_convOT(inputfile):
    # Okay first things first. Should check if the inputted file is actually a onetep file and if its complete.
    removelist = ['\n', '', ' ']
    with open(inputfile, 'r') as infile:
        inlist = [x for x in infile if x not in removelist]

    geolist = []

    # Check inputted file is a onetep file.
    if inlist[37].startswith(' |  "Introducing ONETEP:'):
        print(' --- file correctly identified as a onetep file --- ')
    else:
        print(' --- file not correctly identified as a ONETEP file - continuing anyway --- ')

    # Strip all the introductory and border lines. As this may save a little bit of time
    # This list compr strips roughly 25% from the total list length. and probably a lot more from verbose runs
    # I'm actually unsure if its faster to strip thing or just read immediately way too much effort to test.

    inlist = [x for x in inlist if not (x.startswith("===") | x.startswith(" +---") | x.startswith(" ---") |
                                        x.startswith('<<') | x.startswith("     ~") | x.startswith("****") |
                                        x.startswith("  ======") | x.startswith("####"))]
    # Actually checking run info now.
    # 1.Check if the job has completed
    if inlist[-1].startswith("Job completed:"):
        print(" --- input file has successfully completed - checking convergence --- ")
    else:
        print(" --- input file has not completed. Exiting now --- ")
        exit()
        # Was going to make it print out the current bfgs step but that seems way too much effort.

    # 2. Generate a list of warnings that onetep printed.
    warnlist = []
    for line in inlist:
        if 'WARNING' in line:
            warnlist.append(line)
    geoflag = 0
    for line in inlist:
        if "ONETEP Geometry Optimisation" in line:
            print(" --- flag for geo opt is on checking if geo converged ----")
            geoflag = 1
    orsetwarns = list(OrderedDict.fromkeys(warnlist))
    if len(warnlist) > 10:
        print("{} warnings found in  the output file. Either the verbose flag was on or that's a lot of errors"
              .format(len(warnlist)))
        print('continuing regardless')
    cgflag = 0
    for line in orsetwarns:
        if 'maximum number of NGWF CG' in line:
            print('--- Convergence of NGWF CG reached maximum iterations - not electronically converged --- ')
            cgflag += 1

    if geoflag == 1:
        print("checking for Ionic convergence")
        for line in inlist:
            if " BFGS : " in line:
                geolist.append(line)
    else:
        print(' --- Geometry Optimization line not found - perhaps this was a single point --- ')
        bfgsflag = 'NOT ENABLED'
    for line in geolist:
        if "Geometry optimization failed to converge after" in line:
            print(" --- Geometry Optimization failed to converge --- ")
            bfgsflag = False

    if cgflag > 0:
        cg = False
    else:
        cg = True

    completed = True
    if not bfgsflag:
        completed = False
    if not cg:
        completed = False

    print(" ### Electronic conv: {0}. Ion conv {1}. Completed: {2} ###".format(cg, bfgsflag, completed))
    return completed


if __name__ == "__main__":
    check_convOT(sys.argv[1])
