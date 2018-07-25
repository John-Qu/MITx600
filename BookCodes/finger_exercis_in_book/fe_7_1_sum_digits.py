def sum_digits(s):
    """Assumes s is a string.
       Returns the sum of the decimal digits in s.
          For example, if s is 'a2b3c' it returns 5."""
    digits_sum = 0
    for c in s:
        try:
            digits_sum += int(c)
        except ValueError:
            print("'" + c + "'" + " in '" + s + "' cannot be added in sum.")
    return digits_sum


def test_sum_digits():
    s = 'a,2b3cf4='
    print("The sum of digits in '" + s + "' is" + str(sum_digits(s)) + '.')


test_sum_digits()
