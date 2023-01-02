'''
Title     : Mean,Var andd Std
Subdomain : NumPy
Domain    : Python
Author    : Asmit Singh
Created   : 2 Jan 2023
Problem   : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
'''

import numpy as np
n, m = map(int, input().split())
k = np.array([input().split() for _ in range(n)],dtype = int)
print(np.mean(k,axis=1))
print(np.var(k,axis=0))
# IDK why but the test cases had only 11 digits of precision
print(round(np.std(k),11))