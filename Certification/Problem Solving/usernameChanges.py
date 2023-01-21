'''
Title     : Username Changes
Domain    : Problem Solving
Author    : Asmit Singh
Created   : 21 Jan 2023
Solved Using   : Python
'''
# Probably not the best approach, but it works

def possibleChanges(usernames):
    ans = []
    for u in usernames:
        if len(u) <= 1:
            ans.append("NO")
        for i in range(len(u) - 1):
            if u[i] > u[i + 1]:
                ans.append("YES")
                break
        else:
            ans.append("NO")
    return ans
