#!/usr/bin/python
import sys

n1, n2, n3, n4, n5, n6 = sys.stdin.readline().strip().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
n5 = float(n5)
n6 = float(n6)

mean = 0.0
mean += n1 * 2 + n2 * 2 + n3 * 2 + n4 * 3 / 2 + n5
print mean
