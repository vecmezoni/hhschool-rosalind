#!/usr/bin/python
import sys
 
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
diffs = 0
for ch1, ch2 in zip(str1, str2):
    if ch1 != ch2:
        diffs += 1
print diffs