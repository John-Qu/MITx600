import pylab, random
# from em_15_3_flip import stdDev


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

def flip(numFlips):
    """扔numFlips次硬币，给出其中正面占比。
    假设：
    numFlips是正整数，扔硬币的次数。
    返回：
    正面占比值"""
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads/float(numFlips) #保证是float类型。

def flipSim(numFlipsPerTrial, numTrials):
    """numTrails次做实验，每次实验抛硬币numFlipsPerTrail次，给出统计结果。
    要求：
    numFlipsPerTrial是正整数，表示每次实验抛掷硬币次数；
    numTrials是正整数，表示实验次数。
    返回：
    （fracHeads列表，包含每次实验的正面占比值。
    mean浮点数，多次实验正面占比值的平均数。
    sd浮点数，多次实验正面占比值的标准差。）
    """
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = stdDev(fracHeads)
    return fracHeads, mean, sd


def labelPlot(numFlips, numTrials, mean, sd):
    """绘图并标注"""
    pylab.title(str(numTrials) + ' trials of '
                + str(numFlips) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    # 在图中特定位置写字
    pylab.annotate('Mean = ' + str(round(mean, 4))
                   + '\nSD = ' + str(round(sd, 4)), size='x-large',
                   xycoords = 'axes fraction', xy = (0.67, 0.5))


def makePlots(numFlips1, numFlips2, numTrials):
    """用两种扔硬币的次数做实验，看直方图对比"""
    # 第一次实验，每次实验扔numFlips1次硬币。
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins = 20)
    # 提取直方图X轴范围
    xmin,xmax = pylab.xlim()
    labelPlot(numFlips1, numTrials, mean1, sd1)

    # 第二次实验，每次实验扔numFlips2次硬币。
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins = 20)
    # 保持直方图X轴范围一致
    pylab.xlim(xmin, xmax)
    labelPlot(numFlips2, numTrials, mean2, sd2)


#makePlots(100, 1000, 1000)


def showErrorBars(minExp, maxExp, numTrials):
    """假设minExp和maxExp是正整数；minExp<maxExp
         numTrials是一个正整数
       用误差条绘制出正面向上的平均比例"""
    means, sds, xVals = [], [], []
    for exp in range(minExp, maxExp + 1):
        xVals.append(2**exp)
        fracHeads, mean, sd = flipSim(2**exp, numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.figure()
    pylab.errorbar(xVals, means, yerr=1.96*pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Number of flips per trial')
    pylab.ylabel('Fraction of heads & 95% confidence')


# 在2^3~2^10次抛掷为横轴，实验100次去平均值和标准差，绘制带误差带的平均值。
showErrorBars(3, 10, 100)
pylab.show()