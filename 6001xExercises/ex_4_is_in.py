def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    l = len(aStr)
    if l == 0:
        return False
    if l == 1:
        return char == aStr
    m = l // 2
    if aStr[m] == char:
        return True
    elif aStr[m] < char:
        return isIn(char, aStr[m+1:])
    else:
        return isIn(char, aStr[:m])


