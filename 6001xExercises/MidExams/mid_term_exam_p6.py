#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:10:03 2018

@author: johnqu
"""

def sumDigits(N):
    '''
    Calculates and returns the sum of N's digits
    N: a non-negative integer
    '''
    if N == 0:
        return 0
    di = N % 10
    re = N // 10
    return di + sumDigits(re)

def test_sumDigits():
    test_N = [123, 110085, 0, 5]
    for N in test_N:
        print(sumDigits(N))

test_sumDigits()