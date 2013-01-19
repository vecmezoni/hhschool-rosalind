#!/usr/bin/python
import sys

def binomial(n,k):
	bc = [1 for i in range(0,k+1)]
	for j in range(1,n-k+1):
		for i in range(1,k+1):
			bc[i] = bc[i-1]+bc[i]
	return float(bc[k])
k, m, n = sys.stdin.readline().strip().split()
k = int(k)
m = int(m)
n = int(n)
probability = 0.0
probability += binomial(k, 1) * binomial(k-1, 1) + binomial(m, 1) * binomial(m - 1, 1) * 3 / 4 + 0
probability += 2 * binomial(k, 1) * binomial(m, 1) + 2 * binomial(k, 1) * binomial(n, 1) + binomial(m, 1) * binomial(n, 1)
probability /= binomial(k + m + n, 1) * binomial(k + m + n - 1, 1)
print probability
