# 15 STOCHASTIC PROGRAMS, PROBABILITY, AND DISTRIBUTIONS

### 玻尔和爱因斯坦争论的是什么？

#### causal nondeterminism 因果关系不确定性

> 在最基础的层面上，物质世界的行为是不可预测的，我们只能做出像“x 非常可能发生”这样的概率上的说明，不能做出像“x 一定会发生”这样的确定性的说明。

——量子力学quantum mechanism和哥本哈根学派Copenhagen Doctrine

#### predictive nondeterminism 预测不确定性

> 是我们不能对物质世界进行准确无误的测量，才导致了不能对未来状态进行精确的预测。爱因斯坦非常好地总结了这二者之间的区别，他说：“当代理论在本质上具有统计特性，只能归因于一个事实——这种理论对物质世界的描述是不完整的。”The essentially statistical character of contemporary theory is solely to be ascribed to the fact that this theory operates with an incomplete description of physical systems.

——爱因斯坦与薛定谔

#### 核心是：是否相信所有事件都是由以前的事件引起的。

牛顿物理学很完美。

In short, everything happens for a reason.

The physical world is a completely predictable place - all future states of a physical system can be derived from knowledge about its current state.


### 为什么要讲"(不)确定性"？

承认"不确定性nondeterminism"是正确行事的前提。

微观层面，这种不确定性的根本，是因果关系不确定，还是测量描述手段造成的不确定性，这个纷争没有实际的重要性。

但是在宏观层面，一定要承认不确定性的存在。把赛马、赌博、股市当作可预测的确定性事件predictably deterministic，将有严重后果。

注意用词区别：
- predictive nondeterminism 预测的不确定性
- predictably deterministic 可预测的确定性的


## 15.1 Stochastic Programs


### 什么是确定性程序？

deterministic program：
whenever, the same input, the same output.

注意不在specification里要求确定性：
- 不要求实现方法是确定性的；
- 允许确定性的实现方法。


### 具有不确定的程序specification怎么写？

在specification里就要求具有不确定性：

```python
def rollDie():
    """返回一个1~6的整数"""
    #可能只返回某一个确定的整数。
    
import random

def rollDie():
    """返回一个1~6的随机整数"""
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)    
```


### 不懂独立事件引发的惊奇？

现在运行rollN(10)，如果输出1111111111或5442462412，那么其中哪个结果更让你惊奇？或者换句话说，哪个序列是更随机的？

这个问题其实是一个陷阱。这两个序列出现的概率是一样的，因为每次投掷得到的值都独立于前面那些投掷结果。

在随机过程中，如果一个事件的结果不会影响另一个事件的结果，我们就称这两个事件是相互独立的。

连续扔出10个1的概率是(1/6)10，比六千万分之一还要小。概率相当低，但并不比其他序列的概率更低，比如5442462412这个序列。


## 15.2 Calculating Simple Probabilities


## 15.3 Inferential Statistics统计推断


### 统计推断的应用场景之一是不知道实际概率？

已知独立事件的概率，可以用分析的方法，推导各种情况发生的概率。

如果不知道独立事件的概率呢？比如不知道硬币是否均匀？骰子是否灌铅？

从一个样本数据中获得统计信息，推断独立事件的概率。然后重复第一段的过程。


### 统计推断的指导原则？

一个从总体数据中随机抽取的样本往往可以表现出与总体相同的特性。

> a random sample tends to exhibit the same properties as the population from which it is drawn.


### 抛硬币问题的统计推断模型的初衷是什么？

蝙蝠侠的敌手"哈维·丹特（又称双面人）"抛硬币，100次都是正面向上，因为(1/2)100（硬币是均匀的假设下发生这种情况的概率）这个值太小了，所以你完全可以怀疑硬币的两面都是正面。

再假设有52次抛掷是正面向上的，48次抛掷是反面向上的，那么你是否觉得再抛100次的话，正面向上与反面向上的比例还会如此吗？同样，你是否觉得再抛100次的话，正面向上的次数会比反面向上的次数多？

什么情况下，可以相信这枚硬币的正面向上概率是0.52？


### 为什么能相信统计推断得出的概率？

我们的依据就是大数定律law of large numbers（也称为伯努利定理Bernoulli's theorem）。

这个定律说明，在独立可重复的实验中，如果每次实验中出现某种特定结果的实际概率为p，那么实验次数接近无穷大时，出现这种结果的比例与实际概率p之间的差收敛于0。


### 如何得到统计推断？

用多个实验次数做实验，看实验次数越来越大时，概率收敛于哪里。

```python
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
```

```commandline
>>> print('Mean =', flipSim(10, 100))
Mean = 0.5010000000000001
>>> print('Mean =', flipSim(100, 100))
Mean = 0.5089000000000001
>>> print('Mean =', flipSim(100, 1000))
Mean = 0.5026799999999995
>>> print('Mean =', flipSim(100, 10000))
Mean = 0.5001740000000001
>>> print('Mean =', flipSim(100, 100000))
Mean = 0.49986170000000485
```

貌似收敛于0.5，而我们知道答案就是0.5.


### 赌徒谬误，均值回归的本质？

赌徒谬误gambler's fallacy：如果预期行为出现偏差deviations，那么这些偏差会在未来被相反的偏差“扯平evened out”。
- 这是大数定律的滥用misapplication。
- 独立事件。过去的结果，对未来的结果没有影响，将来的事件该是啥概率还是啥概率，不会可以有偏。

均值回归regression to the mean：如果出现一个极端的随机事件，那么下一个随机事件很可能就不是极端的。
- 正态分布。在均值左右的情况更多，只是说下一个事件更大可能是平均水平，而更小可能延续极端情况。
- 这没有破坏事件独立性。如果没有上一个极端事件，下一个事件的概率仍然如此。
- 主要用于破除对于运气、偏差的迷恋，看到能力的实质。

在很多工作中，成功既需要能力，也需要运气。能力决定了均值，运气则导致了方差。运气的随机性解释了均值回归。

Success in most endeavors requires a combination of skill and luck. The skill component determines the mean and the luck component accounts for the variability. The randomness of luck leads to regression to the mean.


### 表现均值回归的代码？

```python
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
```

![](https://ws4.sinaimg.cn/large/006tNc79gy1fqy1glkl9nj30zk0qowfj.jpg)

- 并不一定抵消，也不一定回归均值，可能同样方向，可能同样剧烈，甚至可能更极端。


### 在硬币模型里看大数定律？

```python
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
```

![](https://ws4.sinaimg.cn/large/006tNc79gy1fqy1kotdyuj30zk0qodgq.jpg)

![](https://ws2.sinaimg.cn/large/006tNc79gy1fqy1kwxv1sj30zk0qoaat.jpg)


### 需要使用多少样本才能得到令人信服的结果呢？这取决于什么？

基础分布的方差varance in the underlying distribution。

$variance(X) = \frac{\sum\nolimits_{x\in X}(x-\mu)^2}{\left|{X}\right|}$

![](https://ws4.sinaimg.cn/large/006tNc79gy1fqy5b2rr77j30em03emxc.jpg)

为什么取决于它？如何使用？


### 为什么用标准差standard deviation描述集合中接近均值的比例？

与方差variance意义完全一样，关键是它与原始数据的单位一致。

> 相对于“总体的平均身高是70英寸，方差为16平方英寸”，我们更容易理解“总体的平均身高是70英寸，标准差为4英寸”这种表达。


### 正反面比例的均值与标准差绘图？

```python
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
flipPlot1(4, 20, 20)
pylab.show()
```

![](https://ws1.sinaimg.cn/large/006tNc79gy1fqy5nt39d2j31kw0llaiv.jpg)

上图是正反面比值的平均值和标准差
- 平均值趋近于1。
- 在10**6次投掷情况下，标准差比平均值低三个数量级。


![](https://ws1.sinaimg.cn/large/006tNc79gy1fqy5nt39d2j31kw0llaiv.jpg)

上图是正反面差值的平均值和标准差
- 平均值在增长，标准差也在变大。
- 这是否意味着当投掷次数增加时，这个差的估计值的可信度不是更大，而是更小了呢？
- 标准差应该总是和均值一起考虑。如果均值是10亿，标准差是100，我们应该认为数据的离散程度很小。但如果均值是100，标准差也是100，那么我们就认为离散程度非常大。


### 当我们比较具有不同均值的数据集合的离散程度时（比如本例），用什么指标衡量更合适？

变异系数比标准差更合适。

标准差除以均值所得的值称为变异系数。

但是如果均值接近于0，微小变化都会导致变异系数非常大的变化。

```python
def CV(X):
    """求X数值序列的变异系数"""
    mean = sum(X)/len(X)
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')
```

![](https://ws2.sinaimg.cn/large/006tNc79gy1fqy6163vkrj31kw0lpadm.jpg)

上图是变异系数与抛掷次数的关系图。
- 随着抛掷次数增多，正反比例的变异系数变小。
- 随着抛掷次数，正反差值的变异系数与它无关，在0.5～1.1之间。
- 实验次数从20次增加到1000次，正反比例的变异系数稳定在0.74~0.78之间。
- 一般来说，变异系数的值如果小于1，就可以认为方差很小。


## 15.4 Distributions


### 用什么图形来表示数据的分布？

直方图。

> 它先对数值进行排序，再将其分到固定数量的等宽区间中，然后绘制一张图表示每个区间中的元素数量。

也许没有排序，只是建立了字典。

```python
import random, pylab
vals = []
for i in range(10000):
    num1 = random.choice(range(0, 101))
    num2 = random.choice(range(0, 101))
    vals.append(num1 + num2)
pylab.hist(vals, bins = 10)
pylab.ylabel("Number of Occurences")
pylab.show()
```

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fqzdr4k2llj30yq0q6q5b.jpg)


### 扔2个骰子时，为什么最容易扔出7？

模拟代码输出直方图。

每个值都有1/6概率，两个骰子的和，7的组合情况最多。

```python
import random, pylab
vals = []
for i in range(10000):
    num1 = random.choice(range(1, 7))
    num2 = random.choice(range(1, 7))
    vals.append(num1 + num2)
pylab.hist(vals, bins = 10)
pylab.ylabel("Number of Occurences")

for i in range(1, 7):
    l = "  "*(i-1)
    for j in range(1, 7):
        l += " " + str(i+j)
    print(l)

pylab.show()
```

```commandline
 2 3 4 5 6 7
   3 4 5 6 7 8
     4 5 6 7 8 9
       5 6 7 8 9 10
         6 7 8 9 10 11
           7 8 9 10 11 12
```

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fqze5ihlqdj30yq0q0acy.jpg)


### 标准差与抛掷硬币的次数有关？

每次抛得越多，标准差越小。

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fqzeii8c4sj31kw0ledli.jpg)

```python
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

makePlots(100, 1000, 10000)
pylab.show()
```


### 直方图、频率分布和概率分布的关系？

直方图histogram反映的是一种频率分布frequency distribution。

频率分布frequency distribution反映的是一个随机变量的取值落在某个范围内的频繁程度how often a random variable has taken on a value in some range。

概率分布probability distribution给出一个随机变量取值在某个范围内的概率，并以此反映相对频率to capture the notion of relative frequency。


### 根据随机变量是离散型的还是连续型的，概率分布可以分成哪两类？

离散型概率分布很容易描述，因为变量取值是有限的，所以只要简单列出每个值的概率即可描述这种分布。

连续型概率分布。数学家们喜欢用概率密度函数（probability density function）来描述连续型概率分布，并经常将其缩写为PDF。PDF描述了一个随机变量位于两个数值之间的概率。你可以将PDF看作定义在X轴上随机变量的最小值与最大值之间的一条曲线。（有时候，X轴是无限长的。）如果假设x1和x2是随机变量的两个值，那么随机变量取值在x1和x2之间的概率就是x1和x2之间的曲线下面积。


### 正态分布的公式和数学特性？

正态normal分布（又称高斯Gaussian分布）由以下概率密度函数定义：

$$P(x)=\frac{1}{\sigma\sqrt{2\pi}}*{\rm e}^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

![](https://ws3.sinaimg.cn/large/006tKfTcly1fr0gchpkzsj30co040dfy.jpg)

这里的μ表示均值，σ表示标准差，e是欧拉数（大约为2.718）。

> 和π一样，e也是一个奇妙的无理数，在数学中无处不在。它最常用来表示自然对数的底。e有很多种等价的定义方式，其中一种是当x趋向于无穷大时，(1+1/x)^x 的值。

正态分布具有良好的数学特性，它可以由两个参数完全确定：均值和标准差（公式中仅有的两个参数）。知道这两个值就等于知道了整个分布。


### 正态分布的经验法则是什么？

大约68.27%的数据都位于距均值1个标准差的范围内，大约95.45%的数据位于距均值2个标准差的范围内，大约99.73%的数据位于距均值3个标准差的范围内。人们有时将这种情况称为68-95-99.7法则，但更多时候将其称为经验法则empirical rule。

```python
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
```


```commandline
For mu = 9 and sigma = 4
 Fraction within 1 std = 0.6827
 Fraction within 2 std = 0.9545
 Fraction within 3 std = 0.9973
For mu = 5 and sigma = 10
 Fraction within 1 std = 0.6827
 Fraction within 2 std = 0.9545
 Fraction within 3 std = 0.9973
For mu = -9 and sigma = 2
 Fraction within 1 std = 0.6827
 Fraction within 2 std = 0.9545
 Fraction within 3 std = 0.9973
```

### 现实生活中为什么要用置信区间说话？

经验法则经常被用来得到置信区间。

对于一个未知的值，我们不应该估计出一个单一的值，而是应该使用置信区间提供一个可能包含这个未知值的范围，以及这个未知值落入这个范围的确定程度。

Almost always, increasing the confidence level  will require widening the confidence interval.

例如，一项政治民意调查显示，在95%的置信水平下，候选人会得到52% ± 4%的选票（也就是说，置信区间为8个单位）。这就是说，民意调查分析者相信，候选人得到48%~56%的选票的可能性为95%。对于民意调查，置信区间通常不是使用多次调查的标准差估计出来的。他们使用标准误差作为替代方式。


### 带有置信区间（误差范围）的估计怎么画图？

errorbar与正常的xy绘图类似，只是在y的方向上加了线条，表示在一定置信程度上的y值区间：

pylab.errorbar(xVals, means, yerr=1.96*pylab.array(sds))
    
```python
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
```

![](https://ws4.sinaimg.cn/large/006tKfTcly1fr0mn268w7j30zk0qojsj.jpg)


### 
