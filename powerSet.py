# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:25:37 2016

@author: approximata
"""

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        print(i)
        combo = []
        for j in range(N):
            print(j)
            # test bit jth of integer i
            print(i, j, i >> j, (i >> j) % 2)
            if (i >> j) % 2 == 1:
                print(i, j, i >> j, (i >> j) % 2)
                combo.append(items[j])
        yield combo
        
        


