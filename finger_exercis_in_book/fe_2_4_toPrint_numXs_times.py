numXs  = abs(int(input('How many times should I print the letter X? ')))
toPrint = ''
while numXs > 0:
    toPrint += 'X'
    numXs -= 1
print(toPrint)