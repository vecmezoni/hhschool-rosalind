#!/usr/bin/python
import sys
import operator

def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

matrix = sys.stdin.readlines()
matrix = [list(dna.strip()) for dna in matrix]
profile = {'A': [0]*len(matrix[0]), 'C': [0]*len(matrix[0]), 'G': [0]*len(matrix[0]), 'T': [0]*len(matrix[0])} 
consensus = "";
for num, tuple in enumerate(zip(*matrix)):
    for char in tuple:
        profile[char][num] += 1
    consensus += keywithmaxval({ key: profile[key][num]  for key in profile.iterkeys()})
#for stats in zip(profile['A'],profile['C'],profile['G'],profile['T']):
    #print max(stats, key=(lamda fff: stats[fff]))

print consensus

for char in ['A','C','G','T']:
    print char+":",
    for value in profile[char]:
        print value,
    print ''
