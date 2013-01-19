#!/usr/bin/python

import fileinput

def count(DNA):
	dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	for char in DNA:
	    if char in dict:
		    dict[char] += 1
	print dict['A'], dict['C'], dict['G'], dict['T']
	
for line in fileinput.input():
    count(line)