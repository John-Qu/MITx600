def remove_duplicates(L1, L2):
    """Assumes that L1 and L2 are lists.
       Removes any element from L1 that also occurs in L2."""
    cloneL1 = L1[:]
    # cloneL1 = list(L1)
    for e1 in cloneL1:
        # for e1 in L1:
        if e1 in L2:
            L1.remove(e1)


def test_remove_duplicates():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_duplicates(L1, L2)
    print("L1 =", L1)


test_remove_duplicates()