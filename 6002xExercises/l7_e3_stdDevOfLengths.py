def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('nan')
    lengths = []
    for s in L:
        lengths.append(len(s))
    mean = sum(lengths)/len(lengths)
    square_sum = 0
    for l in lengths:
        square_sum += (l-mean)**2
    dev = square_sum / len(lengths)
    std_dev = dev**0.5
    # return round(std_dev, 4)
    return std_dev


def test_stdDevOfLengths():

    L = ['a', 'z', 'p']
    print(str(L) + "'s " + "Standard Deviation of Lengths is " + str(round(stdDevOfLengths(L), 4)))
    # should return 0.

    L = ['apples', 'oranges', 'kiwis', 'pineapples']
    print(str(L) + "'s " + "Standard Deviation of Lengths is " + str(round(stdDevOfLengths(L), 4)))
    # should return 1.8708.

    L = []
    print(str(L) + "'s " + "Standard Deviation of Lengths is " + str(round(stdDevOfLengths(L), 4)))

test_stdDevOfLengths()

