def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    i = 0
    new_tup = ()
    while i < len(aTup):
        new_tup += (aTup[i],)
        i += 2
    return new_tup


def test_oddTuple(aTup):
    odd_tup = oddTuples(aTup)
    print(aTup)
    print(odd_tup)


test_oddTuple(('I', 'am', 'a', 'test', 'tuple'))