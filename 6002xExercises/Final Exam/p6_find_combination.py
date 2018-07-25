def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    import numpy as np
    l = len(choices)
    choices = np.array(choices)
    results = []
    no_equal = True
    for i in range(2**l):
        result = []
        s_n = bin(i)[2:]
        while len(s_n)<l:
            s_n = "0"+s_n
        # print("s_n =", s_n)
        for c in s_n:
            result.append(int(c))
        result = np.array(result)
        s = sum(result*choices)
        print("result is "+str(result) + " and sum is "+str(s))
        if s == total:
            no_equal = False
            results.append((s, result))
            print(results)
        elif s < total and no_equal:
            results.append((s, result))
    # results.sort(reverse=True)
    final_st, final_result = results[0]
    small_sum_result = l
    for st, result in results:
        if st == total:
            sr = sum(result)
            if sr <= small_sum_result:
                final_result = result
                small_sum_result = sr
        elif no_equal:
            if st > final_st:
                final_result = result
                final_st = st
    return final_result

# choices = [1,2,2,3]
# total = 4
# should return either [0 1 1 0] or [1 0 0 1]
# choices = [1,1,3,5,3]
# total = 5
# should return [0 0 0 1 0]
# choices = [1,1,1,9]
# total = 4
# should return [1 1 1 0]
# print(find_combination(choices, total))


# print(find_combination([10, 100, 1000, 3, 8, 12, 38], 1171))
