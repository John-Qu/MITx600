# -*- coding: utf-8 -*-

def genPrimes():
    primes = []
    next = 1
    while True:
        flag = True
        next += 1
        for i in primes:
            if next % i == 0:
                flag = False
                break
        if flag:
            yield next
            primes.append(next)

foo = get_primes()

print(foo.__next__())