import em_4_3_factorial
import em_4_3_fibonacci

def apply_to_each(l, f):
    """Assumes l is a list, f a function.
       Mutates l by replacing each element, e, of l by f(e)"""
    for i in range(len(l)):
        l[i] = f(l[i])


def test_apply_to_each():
    l = [1, -2, 3.33]
    print('l =', l)
    print('Apply abs to each element of l.')
    apply_to_each(l, abs)
    print('l =', l)
    print('Apply int to each element of l.')
    apply_to_each(l, int)
    print('l =', l)
    print('Apply factorial to each element of l.')
    apply_to_each(l, em_4_3_factorial.factRecursion)
    print('l =', l)
    print('Apply Fibonnaci to each element of l.')
    apply_to_each(l, em_4_3_fibonacci.fib)
    print('l =', l)


test_apply_to_each()
