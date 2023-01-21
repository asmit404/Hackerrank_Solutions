'''
Title     : Unexpected Demand
Domain    : Problem Solving
Author    : Asmit Singh
Created   : 21 Jan 2023
Solved Using   : Python
'''
# Probably not the best approach, but it works

def filledOrders(order, k):
    order.sort()
    ans = 0
    for x in order:
        if x <= k:
            ans += 1
            k -= x
        else:
            break
    return ans
