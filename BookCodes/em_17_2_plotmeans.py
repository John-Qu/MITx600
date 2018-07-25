import random, pylab

from em_15_3_flip import variance


def plotMeans(numDicePerTrial, numDiceThrown, numBins, legend,
              color, style):
    """
    估计一个连续值骰子的均值
    :param numDicePerTrial: int，每手掷骰子的次数，即样本大小
    :param numDiceThrown: int，总共掷骰子的次数
    :param numBins: int，hist的柱子数。
    :param legend: str，图表内标注
    :param color: str，颜色
    :param style: str，柱状图填充样式
    :return: 平均值的平均值，平均值的方差
    """
    means = []
    # 样本数量
    numTrials = numDiceThrown//numDicePerTrial
    for i in range(numTrials):
        vals = 0
        for j in range(numDicePerTrial):
            vals += 5*random.random()
        means.append(vals/numDicePerTrial)
    # 绘制平均值分布图
    pylab.hist(means, numBins, color = color, label = legend,
               weights = pylab.array(len(means)*[1])/len(means),
               hatch = style) # 使用hatch关键字参数来区别两个直方图的图形。
    return sum(means)/len(means), variance(means)

pylab.figure('Rolling Continuous Dice')
mean, var = plotMeans(1, 100000, 110, '1 die', 'w', '*')
print('Mean of rolling 1 die =', round(mean,4),
      'Variance =', round(var,4))
mean, var = plotMeans(10, 100000, 110,
                      'Mean of 10 dice', 'w', '-')
print('Mean of rolling 10 dice =', round(mean, 4),
      'Variance =', round(var, 4))
mean, var = plotMeans(100, 100000, 110,
                      'Mean of 100 dice', 'w', '//')
print('Mean of rolling 100 dice =', round(mean, 4),
      'Variance =', round(var, 4))
pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()
pylab.show()