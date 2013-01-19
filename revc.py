#!/usr/bin/python
import sys
 
map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'} 
dna = sys.stdin.read().strip()
print ''.join([map[char] for char in dna])[::-1]