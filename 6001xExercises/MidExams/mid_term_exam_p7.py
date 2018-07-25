#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:33:47 2018

@author: johnqu
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def grade(x):
        tot = 0
        k = len(L)
        for i in range(k):
            tot += L[i]*x**(k-1-i)
        return tot
    return grade
            

def test_general_poly():
    L = [1, 2, 3, 4]
    x = 10
    print(general_poly(L)(x))
    

test_general_poly()