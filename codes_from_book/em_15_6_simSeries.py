import random, pylab


def playSeries(numGames, teamProb):
    """
    一次模拟，进行numGames场比赛，过半数则胜。
    :param numGames: int，两队比赛场数。
    :param teamProb: float，某队单场获胜概率。
    :return: 布尔值，胜败。
    """
    numWon = 0
    for game in range(numGames):
        # 用随机数与获胜概率做比较
        if random.random() <= teamProb:
            numWon += 1
    # 胜负是真假值，作为判断依据
    return (numWon > numGames//2) # 7//2 = 3, 4 > 3

def fractionWon(teamProb, numSeries, seriesLen):
    """
    计算在numSeries次模拟中，某队获胜的比率。
    :param teamProb: float，某队单场获胜概率
    :param numSeries: int，模拟的次数
    :param seriesLen: int，两队交锋场数
    :return: float，获胜的比率
    """
    won = 0
    for series in range(numSeries):
        if playSeries(seriesLen, teamProb):
            won += 1
    return won/float(numSeries)

def simSeries(numSeries):
    """
    模拟numSeries次，看某队获胜比率与单场获胜概率之间的关系。
    :param numSeries: int，模拟次数。
    :return: 图表。
    """
    # 某队单场获胜比率大于0.5才有可能整体获胜。
    prob = 0.5
    fracsWon, probs = [], []
    while prob <= 1.0: # prob递增到1.0为止。
        # 把某队获胜比率和单场获胜概率添加进列表
        fracsWon.append(fractionWon(prob, numSeries, 7)) # 7是关键参数，七局四胜制。
        probs.append(prob)
        prob += 0.01
    # 输出某队获胜比率和单场获胜概率图表
    pylab.axhline(0.95) # 认为超过95%的获胜比率才算是有能力、有把握最终获胜。
    pylab.plot(probs, fracsWon, 'k', linewidth = 5)
    pylab.xlabel('Probability of Winning a Game')
    pylab.ylabel('Probability of Winning a Series')
    pylab.title(str(numSeries) + ' Seven-Game Series')


simSeries(400)
pylab.show()