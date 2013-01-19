#!/usr/bin/python

import fileinput

maxGC = 0
maxID = ""

currentID = ""
currentDNA = ""
currentGC = 0

DNAs = {}
for line in fileinput.input():
    if line[0] == ">":
        currentID = line[1:].strip()
        DNAs[currentID] = ""
    else:
        DNAs[currentID] += line.strip()

for ID, DNA in DNAs.iteritems():
    GC = float(DNA.count('C') + DNA.count('G'))
    GC /= len(DNA.strip())
    if GC > maxGC:
        maxGC = GC
        maxID = ID
    
print maxID
print '{0:.6f}%'.format(maxGC*100)