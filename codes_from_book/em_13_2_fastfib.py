def fastFib(n, memo = {}):
    """假设
        n是非负整数，
        memo只在递归调用中使用，默认值是空字典，无需使用者创建。
    返回
        第n个斐波那契数"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result