def isPalindrome(aString):
    '''
    aString: a string
    '''
    if aString == "":
        return True
    return (aString[0] == aString[-1]) and isPalindrome(aString[1:-1])

aString_list = ['', 'abba', 'aboba', 'adoba', 'able', 'a']
for aString in aString_list:
    print(aString + " is palindrome?", isPalindrome(aString))