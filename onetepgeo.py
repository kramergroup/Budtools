#!/usr/bin/env python3
# GEO Parser - A very simple method to save onetep geometry optimizations (and technically singlepoints) to a csv file showing the
# energy steps during a geo

# add a arg parser but too be honest it's a bit overkill having warnigns be printed is probably a good thing.
import sys
import re
import pandas as pd
from _collections import OrderedDict
from os import makedirs

def onetepgeo(inputfile, warnings=True):

    outputdir = '/'.join((inputfile.split('/')[0:-1]))

    # Look for errors just dump them to a text file for now.
    if warnings:
        warn = []
        for line in open(inputfile):
            if "WARN" in line:
                warn.append(line)

        warn = list(OrderedDict.fromkeys(warn))
        df_ = pd.DataFrame(warn)
        df_.to_csv(outputdir + '/warn.txt', sep='\t', columns=None, index=None)

    enlist = []
    for line in open(inputfile):
        if "<-- CG" in line:
            enlist.append(line)
    list2write = []
    for count in enlist:
        v = count.split()
        list2write.append([v[2], v[1], v[0]])

    df = pd.DataFrame(list2write, columns=['ENERGY', 'RMS', 'CG STEPS'])

    df.to_csv(outputdir + '/ENERGY.csv', sep='\t')

    return df


if __name__ == "__main__":
    onetepgeo(sys.argv[1])
