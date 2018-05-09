import random


def variance(X):
    """求得数值型列表的方差。
    假设X是一个数值型列表。
    返回X的方差。"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)


def stdDev(X):
    """求X数值型列表的标准差。
    假设X是一个数值型列表。
    返回X的标准差。"""
    return variance(X)**0.5


def throwNeedles(numNeedles):
    """
    随机向[0, 1)见方范围内扔针，根据落入圆内的针数比例，估计pi值。
    :param numNeedles: int，针的数量
    :return: float，落入圆内针数与整体针的比例
    """
    inCircle = 0
    for Needles in range(1, numNeedles + 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1:
            inCircle += 1
    #数出落入圆中的针数比例
    return inCircle/numNeedles


def getEst(numNeedles, numTrials):
    """
    多次实验，求估计pi的平均值和标准差。
    :param numNeedles: 每次扔多少针。
    :param numTrials: 做多少次实验。
    :return: （估计pi的平均值，标准差）
    """
    estimates = []
    for t in range(numTrials):
        piGuess = 4*throwNeedles(numNeedles) #。正方形面积是4，所以要乘以4。。
        estimates.append(piGuess) #加入列表中。
    sDev = stdDev(estimates) #算列表的标准差
    curEst = sum(estimates)/len(estimates) #算列表的平均值
    print('Est. =', str(round(curEst, 5)) + ',',
          'Std. dev. =', str(round(sDev, 5)) + ',',
          'Needles =', numNeedles)
    return (curEst, sDev)


def estPi(precision, numTrials):
    """
    倍增提高扔针的数量numNeedles，缩小标准差，直到95%的数据都落入precision范围内。
    :param precision: float，估算pi与真实pi之间的精度
    :param numTrials: int，做多少次实验，对标准差无影响。
    :return: float，估算出来的pi值
    """
    numNeedles = 1000
    sDev = precision
    while sDev > precision/1.96:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst


estPi(0.01, 100)