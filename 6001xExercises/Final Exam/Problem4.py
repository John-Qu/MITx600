def take_increasing(L):
    longest = 0
    longest_incr_list = []
    longest_index = 0
    for i in range(len(L)-1):
        incr_list = [L[i]]
        for j in range(i+1, len(L)):
            if L[j-1] > L[j]:
                break
            else:
                incr_list.append(L[j])
        if len(incr_list) > longest:
            longest = len(incr_list)
            longest_incr_list = incr_list
            longest_index = i
    return longest_incr_list, longest_index


def test_take_increasing(L):
    print("The longest increasing run in ", L, "is", take_increasing(L)[0])

# test_take_increasing(L)


def take_decreasing(L):
    longest = 0
    longest_decr_list = []
    longest_index = 0
    for i in range(len(L)-1):
        decr_list = [L[i]]
        for j in range(i+1, len(L)):
            if L[j-1] < L[j]:
                break
            else:
                decr_list.append(L[j])
        if len(decr_list) > longest:
            longest = len(decr_list)
            longest_decr_list = decr_list
            longest_index = i
    return longest_decr_list, longest_index

def test_take_decreasing(L):
    print("The longest decreasing run in ", L, "is", take_decreasing(L)[0])

# test_take_decreasing(L)


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    longest_increasing_run = take_increasing(L)
    longest_decreasing_run = take_decreasing(L)
    if len(longest_increasing_run[0]) == len(longest_decreasing_run[0]):
        if longest_increasing_run[1] > longest_decreasing_run[1]:
            longest_run = longest_decreasing_run[0]
        else:
            longest_run = longest_increasing_run[0]
    elif len(longest_increasing_run[0]) > len(longest_decreasing_run[0]):
        longest_run = longest_increasing_run[0]
    else:
        longest_run = longest_decreasing_run[0]
    return sum(longest_run)


L1 = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
L2 = [5, 4, 10]
L3 = [5, 4]
L4 = [4, 10]
print(longest_run(L1))
print(longest_run(L2))
print(longest_run(L3))
print(longest_run(L4))




