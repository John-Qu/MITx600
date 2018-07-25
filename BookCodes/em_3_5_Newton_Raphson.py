# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:01:04 2016

@author: ericgrimson
"""

y = 54.0
epsilon = 0.01
numGuesses = 0
low = 0.0
high = y
ans = (high + low)/2.0

while abs(ans**2 - y) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < y:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('Bisection search numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(y))

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:14:22 2016

@author: ericgrimson
"""

guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print('Newton-Raphson numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
