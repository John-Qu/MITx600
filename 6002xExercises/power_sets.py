from itertools import chain, combinations


def yeild_powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


l = [1, 2, 3, 4]
# r = [x for x in yeild_powerset(l)]


def bitwise_powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]


def itertools_powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


# def chain(*iterables):
#     # chain('ABC', 'DEF') --> A B C D E F
#     for it in iterables:
#         for element in it:
#             yield element
#
#
# def from_iterable(iterables):
#     # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
#     for it in iterables:
#         for element in it:
#             yield element
#
#
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1, bag2 = [], []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                bag2.append(items[j])
        yield bag1, bag2


# generate all combinations of N items
def bitwise_yeild_powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


# generate all combinations of N items
# def powerSet(items):
#     s = list(items)
#     # enumerate the 2**N possible combinations
#     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


# print(r)

# def powerSet(items):
#     s = list(items)
#     # enumerate the 2**N possible combinations
#     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


# print(list(powerSet("abcd")))

def powerSet(items):
    s = list(items)
    # enumerate the 2**N possible combinations
    for r in range(len(s) + 1):
        yield chain.from_iterable(combinations(s, r))

# r = [x for x in list(powerSet(l))]
#
# print(r)
print(powerSet("abcd"))
