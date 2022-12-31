import numpy

def arrays(arr):
    x = numpy.array(arr,float)
    res = numpy.flip(x)
    return res

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
