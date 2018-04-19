def find_an_even(l):
    """Assumes l is a list of integers.
       Return the first even number in l.
       Raise ValueError if l does not contain an even number."""
    for n in l:
        if n%2 == 0:
            return n
    raise ValueError("There is no even number in list.")


def test_find_an_even():
    l1 = [1, 35, 42, 5, 2]
    print(find_an_even(l1))
    l2 = [1, 35, 47, 5, 9]
    print(find_an_even(l2))


test_find_an_even()
