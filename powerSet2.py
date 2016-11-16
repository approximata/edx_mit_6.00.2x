# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 21:24:32 2016

@author: approximata
"""

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        print("i =", i, "bin i =", bin(i))
        combo = []
        for j in range(N-1,-1,-1):
            print("j =", j)
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                print("i shifted j places:", bin(i>>j))
                print("in set:"+' '+ items[N-j-1])
                combo.append(items[N-j-1])
        yield combo

L = ['x','y','z']

powerSet(L)