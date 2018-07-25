import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.choice(range(0, 100, 2))

print(genEven())
