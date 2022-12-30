'''
Title     : Find Angle MBC
Subdomain : Math
Domain    : Python
Author    : Asmit Singh
Created   : 30 Dec 2022
Problem   : https://www.hackerrank.com/challenges/find-angle/problem
'''

import math
ab = float(input())
bc = float(input())
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm
a = bc
c = bm
b = mc
angel_b_radian = math.acos(a / (2*b))
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))
output_str = str(angel_b_degree)+chr(176)
print(output_str)