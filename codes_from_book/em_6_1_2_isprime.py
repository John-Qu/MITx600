def is_prime(x):
    """Assumes x is a nonnegative int.
       Returns True if x is prime; False otherwise."""
    if x <= 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True