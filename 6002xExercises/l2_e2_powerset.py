from itertools import chain, combinations


def powerSet(items):
    s = list(items)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# for result in powerSet([1, 2, 3]):
#     print(result)
#
# results = list(powerSet([1, 2, 3]))
# print(results)
