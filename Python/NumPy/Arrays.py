'''
Title     : Arrays
Subdomain : NumPy
Domain    : Python
Author    : Asmit Singh
Created   : 31 Dec 2022
Problem   : https://www.hackerrank.com/challenges/np-arrays/problem
'''

import numpy

def arrays(arr):
    x = numpy.array(arr,float)
    res = numpy.flip(x)
    return res

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
