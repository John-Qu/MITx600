def copy(l1, l2):
    """Assumes l1, l2 are lists
       Mutates l2 to be a copy of l1"""
    while len(l2) > 0:  # remove all elements from l2.
        l2.pop()  # remove last element of l2.
    for e in l1:  # append l1's elements to initially empty l2
        l2.append(e)


l1 = [1, 2, 3]
l2 = l1
copy(l1, l2)
print(l2)
