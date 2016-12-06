#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:07:30 2016

@author: approximata
"""

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    print(mean, std, std/mean)
    return mean, std



def stdDevOfLengths(L):
    if len(L) == 0:
        return float('NaN')
    sumLen = 0
    for l in L:
        sumLen += len(l)

    # print(sumLen)
    mean = sumLen / len(L)
    tot = 0.0

    for l in L:
        tot += (len(l) - mean)**2
    std = (tot/len(L))**0.5
    # print(mean, std)
    return std


myList = ['apples', 'oranges', 'kiwis', 'pineapples']
myNumList = [10, 4, 12, 15, 20, 5]

stdDevOfLengths(myList)
getMeanAndStd(myNumList)
