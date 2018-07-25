#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:26:16 2018

@author: johnqu
"""


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    values = list(aDict.values())
    uni_keys = []
    not_uni_values = []
    for key in aDict.keys():
        value = aDict[key]
        values.remove(value)
        if (value not in not_uni_values) & (value not in values):
            uni_keys.append(key)
        else:
            not_uni_values.append(value)
    uni_keys.sort()
    return uni_keys
    

def test_uniqueValues():
    aDict = {}
    s = "abcdefgh"
    for i in range(8):
        aDict[s[i]] = i
    aDict['d'] = 2
    aDict['h'] = 5
    uniques = uniqueValues(aDict)
    print(aDict)
    
    print("The unique values' keys are:")
    for e in uniques:
        print(e)

test_uniqueValues()    