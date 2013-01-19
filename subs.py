#!/usr/bin/python
import sys
 
dna = sys.stdin.readline().strip()
sub = sys.stdin.readline().strip()

search = dna.find(sub)
while search > -1:
    print search + 1,
    search = dna.find(sub, search+1)
