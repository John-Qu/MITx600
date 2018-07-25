#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:19:43 2018

@author: johnqu
"""
aList = ["apple", "cat", "dog", "banana"]

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    sub_list = []
    for e in aList:
        if len(e) < 4:
            sub_list.append(e)
    return sub_list

print(lessThan4(aList))