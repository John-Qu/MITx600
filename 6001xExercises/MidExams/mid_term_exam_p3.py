#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:59:50 2018

@author: johnqu
"""
def isMyNumber(guess, myNumber = -256):
    
    if guess < myNumber:
        return -1
    elif guess > myNumber:
        return 1
    else:
        return 0

def jumpAndBackpedal(isMyNumber, guess = 1):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    sign = isMyNumber(guess)
    if sign == 0:
        return guess
#    while True:
#        if sign == -1:
#            guess += 1
#        else:
#            guess -= 1
#        return jumpAndBackpedal(isMyNumber, guess)
    elif sign == -1:
        guess += 1
    else:
        guess -= 1
    return jumpAndBackpedal(isMyNumber, guess)


print(jumpAndBackpedal(isMyNumber))