#!/usr/bin/python3
"""
   minimum operatioins
"""

def minOperations(n):
    """
       minOperations
    """
    if n == 1:
        return 0
    li = [[2, 1, 2]]
    while True:
        for i in range(len(li)):
            if li[i][0] == n:
                return li[i][2]
        for l in range(len(li)):
            li.append([li[l][0] + li[l][1], li[l][1], li[l][2] + 1])
            li.append([li[l][0] * 2, li[l][0], li[l][2] + 2])
            li.pop(l)
            print(li)