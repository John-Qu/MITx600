import random, pylab


def flip(numFlips):
    """随机抛掷硬皮多次，记录正面向上的比例。
    假设：
    numFlips是一个正整数, 是抛的次数。
    返回：
    人头向上的比例值"""
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    """模拟多人抛掷硬币，每人抛多次，算取各人所得比率的平均值。
    假设：
    numFlipsPerTrial和numTrials是正整数，分别表示每人抛掷的次数和抛硬币的人数.
    返回：
    mean值，多人抛掷所得比例的平均值。"""
    #Head当头占比值的列表
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean


print('Mean =', flipSim(10, 100))


def regressToMean(numFlips, numTrials):
    """"""
    #获取每次实验（抛掷numFlips次硬币）中正面向上的比例
    fracHeads = []
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    #找出具有极端结果的实验，以及这些实验的下一次实验
    extremes, nextTrials = [], []
    for i in range(len(fracHeads) - 1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
    #绘制结果
    pylab.plot(range(len(extremes)), extremes, 'ko',
               label = 'Extreme')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^',
               label = 'Next Trial')
    #在0.5处绘制一条平行于x轴的横线。
    pylab.axhline(0.5)
    #X、Y轴的显示范围
    pylab.ylim(0, 1)
    pylab.xlim(-1, len(extremes) + 1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc = 'best')
    # pylab.show()

regressToMean(15, 40)


def flipPlot(minExp, maxExp):
    """通过绘图，看大数定律的作用。
    假设：
    minExp和maxExp是正整数，定义单次投掷硬币的次数区间，以2为底的指数，minExp<maxExp。
    绘制：
    2张图表，反映从2**minExp到2**maxExp次硬币投掷的结果"""

    # ratios是正反比例列表，diffs是正反差值的绝对值列表，xAxis是几个尝试次数的列表。
    ratios, diffs, xAxis = [], [], []
    # 生成指数序列，把值添加入xAxis列表。
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    # len(xAxis)次尝试，每次投掷xAxis[i]次。
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads += 1
        numTails = numFlips - numHeads
        try:
            # 增录ratios正反比例和diffs正反差值。
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            # 这么大量尝试中，反面为零的概率很低，继续运行。
            continue


    pylab.figure()
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'ko')
    # 调整xy轴标度方式，免得有效信息被挤在原点附近。
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis, ratios, 'ko')
    # 调整x轴标度方式，免得有效信息被挤在原点附近。
    pylab.semilogx()

#以0为种子，开始生成伪随机数，保证每次执行下面的绘图命令得到的数据相同。
random.seed(0)
# 做2**4，到2**20次投掷硬币，绘图。
flipPlot(4, 20)


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


def makePlot(xVals, yVals, title, xLabel, yLabel, style,
             logX = False, logY = False):
    """把绘图命令所需的代码和信息集成起来，生成绘图。
    要求：
    xVals, yVals是序列值；
    title是字符串，图表的名称；
    xLabel, yLabel是字符串，标注x、y轴。
    style是字符串，定义颜色和线型样式。
    logX和logY是布尔值，是否采用对数坐标。
    输出：
    新建一个title窗口绘图，无保存，无显示。"""
    pylab.figure(title)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()


# 把求正反面的工作拆出来，成为一个函数了。
def runTrial(numFlips):
    """模拟抛numFlips次硬币的一次实验
    要求：numFlips是正整数。
    返回：其中（正面次数，反面次数）元组。"""
    numHeads = 0
    for n in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)

def flipPlot1(minExp, maxExp, numTrials):
    """与flipPlot不同，是多次尝试取平均值，统一绘图。
    假设minExp、maxExp和numTrials为大于0的整数；minExp<maxExp。
    绘制出numTrials次硬币抛掷实验（每次抛掷次数从2**minExp到2**maxExp）的摘要统计结果（取平均，有方差）."""
    # 初始化各个列表。
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis = []
    # 初始化X轴。
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    # 每次投掷numFlips次。
    for numFlips in xAxis:
        ratios, diffs = [], []
        # 多次尝试取平均值。
        for t in range(numTrials):
            # 提取投掷numFlips次的正反结果
            numHeads, numTails = runTrial(numFlips)
            # 计算正反比例和差值，增添入列表
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        # 计算比例和差值的平均值和标准差
        ratiosMeans.append(sum(ratios)/numTrials)
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))

    numTrialsString = ' (' + str(numTrials) + ' Trials)'
    # 正反面比值的平均值
    title = 'Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title, 'Number of flips',
             'Mean Heads/Tails', 'ko', logX = True)
    # 正反面比值的标准差
    title = 'SD Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title, 'Number of Flips',
            'Standard Deviation', 'ko', logX = True, logY = True)
    # 正反面差值的平均值
    title = 'Mean abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsMeans, title, 'Number of Flips', 'Mean abs(#Heads - #Tails)', 'ko', logX=True, logY=True)
    # 正反面差值的标准差
    title = 'SD abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsSDs, title, 'Number of Flips', 'Standard Deviation', 'ko', logX=True, logY=True)


# 模拟20次投掷硬币实验，每次投掷2**4到2**20次。
# flipPlot1(4, 20, 20)
# pylab.show()


def CV(X):
    """求X数值序列的变异系数"""
    mean = sum(X)/len(X)
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')


def flipPlot2(minExp, maxExp, numTrials):
    """假设minExp、maxExp为正整数；minExp<maxExp。
         numTrial为正整数。
       绘制出numTrials次硬币抛掷实验（抛掷次数从2**minExp到2**maxExp）的摘要统计结果"""
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    ratiosCVs, diffsCVs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        ratiosMeans.append(sum(ratios)/numTrials)
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    numTrialsString = ' (' + str(numTrials) + ' Trials)'
    title = 'Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title, 'Number of flips',
             'Mean Heads/Tails', 'ko', logX = True)
    title = 'SD Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title, 'Number of flips',
             'Standard Deviation', 'ko',logX = True, logY = True)
    title = 'Mean abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsMeans, title,'Number of Flips',
             'Mean abs(#Heads - #Tails)', 'ko',
              logX = True, logY = True)
    title =  'SD abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsSDs, title, 'Number of Flips',
             'Standard Deviation', 'ko', logX = True, logY = True)
    title = 'Coeff. of Var. abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsCVs, title, 'Number of Flips',
             'Coeff. of Var.', 'ko', logX = True)
    title = 'Coeff. of Var. Heads/Tails Ratio' + numTrialsString
    makePlot(xAxis, ratiosCVs, title, 'Number of Flips',
             'Coeff. of Var.', 'ko', logX = True, logY = True)

# 实验20次取平均值
# flipPlot2(4, 20, 20)
flipPlot2(4, 20, 1000)
#pylab.show()
