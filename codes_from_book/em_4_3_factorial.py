def factIteration(n):
    """Assumes n an int > 0
       Returns n!"""
    result = 1
    while n >= 1:
        result = result * n
        n -= 1
    return result

def factRecursion(n):
    """Assumes n an int > 0
       Returns n!"""
    if n == 1:
        return 1
    else:
        return n*factRecursion(n-1)
