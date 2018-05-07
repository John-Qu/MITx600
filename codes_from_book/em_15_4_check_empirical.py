import scipy.integrate, random, pylab


def gaussian(x, mu, sigma):
    """正态分布的概率密度函数"""
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2


def checkEmpirical(numTrials):
    """用numTrial组随机的均值和标准差构造正态分布PDF，验证经验法则"""
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma =', sigma)
        for numStd in (1, 2, 3):
            # 积分函数quad的形式参数：
            # 1对其第一形参求积分的函数 2下限 3上限 4(给函数的其他参数)
            # 返回（积分近似值，积分估计误差）
            area = scipy.integrate.quad(gaussian, mu-numStd*sigma, mu+numStd*sigma, (mu, sigma))[0]
            print(' Fraction within', numStd, 'std =', round(area, 4))


checkEmpirical(3)