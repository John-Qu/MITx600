# Problem 4
#
# Consider a list of positive(there is at least one positive) and negative numbers.You are asked to find the maximum sum of a contiguous subsequence.
#
# For example,
#
# in the list[3, 4, -1, 5, -4], the maximum sum is 3 + 4 - 1 + 5 = 11
# in the list[3, 4, -8, 15, -1, 2], the maximum sum is 15 - 1 + 2 = 16
#
# Write a function that meets the specification below.


def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    sums = []
    for i in range(len(L)):
        for j in range(i, len(L)):
            sums.append((sum(L[i:(j+1)]),(i,(j+1))))
    sums.sort()
    return sums[-1][0]


# L = [3, 4, -8, 15, -1, 2]
L = [3, 4, -1, 5, -4]
print(max_contig_sum(L))
