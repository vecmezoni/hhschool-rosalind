#!/usr/bin/python
import sys
 
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
print sum([a != b for a, b in zip(s1, s2)])