# 17 SAMPLING AND CONFIDENCE INTERVALS

### 什么是总体，什么是样本？

Inferential statistics involves making inference about a population of examples by analyzing a randomly chosen subset (a sample) of that population.


### 抽样为什么重要？

有时不可能对总体数据都进行处理。


### 抽样什么最重要？

样本与总体之间的一致性correspondence。

如果样本是50位亚裔美国妇女，或者50位足球运动员，而总体是所有18岁的美国人.


### 什么是概率抽样？

通过概率抽样，总体中的每个个体都有一定的非零概率被抽中。


### 什么是简单随机抽样？什么是分层抽样？

在简单随机抽样simple random sampling中，总体的每个个体被抽中的机会都是相等的。

在分层抽样stratified sampling中，先将总体划分为若干层，对每一层进行随机抽样，然后组成样本。分层抽样可以提高样本在整体上代表总体的概率。


## 17.1 Sampling a data set


### 一个简单的随机抽样，看图形、均值与方差，得到什么启示？

```python
import random, pylab, numpy
from em_15_3_flip import stdDev


def makeHist(data, title, xlabel, ylabel, bins = 20):
    pylab.figure(title)
    pylab.hist(data, bins = bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    mean = sum(data)/len(data)
    std = stdDev(data)
    pylab.annotate('Mean = ' + str(round(mean, 2)) + \
                   '\nSD = ' + str(round(std, 2)), fontsize = 20,
                   xy = (0.1, 0.75), xycoords = 'axes fraction')

def getHighs():
    inFile = open('temperatures.csv')
    population = []
    for l in inFile:
        try:
            tempC = float(l.split(',')[1])
            population.append(tempC)
        except:
            continue
    inFile.close()
    return population


population = getHighs()
makeHist(population,
         'Daily High 1961-2015, Population of '+str(len(population)),
         'Degrees C', 'Number Days')

sample = random.sample(population, 40)
makeHist(sample,
         'Daily High 1961-2015, Sample of '+str(len(sample)),
         'Degrees C', 'Number Days')

```  

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fr68ic8fvcj30zk0qotax.jpg)

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fr688gru62j30zk0qogn6.jpg)

- 样本的分布与总体分布相去甚远。因为样本数量很少，所以也不用大惊小怪。
- 更需注意的是，尽管样本数量很少（从42万的总体中抽取出了40个），但估算出的均值与总体均值的差别还不到2%。
- 是我们非常幸运，还是有什么原因使得这个均值的估计值如此之好？换句话说，我们能否以一种定量的方式表示出对估计值的确信程度？


### 能否以一种定量的方式表示出对估计值的确信程度？

应该使用置信区间confidence interval和置信水平confidence level来表示估计值的可靠程度。

如果从一个庞大的总体中抽取了一个（任意大小的）独立样本，那么总体均值mean of population的最好估计值就是样本的均值mean of sample。（因为只有这一个样本的数据。）

为了达到某个想要的置信水平，需要估计置信区间的宽度，他相对于求平均值要更复杂一些。它依赖于，部分是，样本大小。

Estimating the width of the confidence interval required to achieve a desired confidence level is tricker.

样本大小非常重要，这很容易理解。大数定律告诉我们，当样本量增加时，样本分布就会与总体分布更加一致。所以样本越大，样本均值和样本标准差更加接近总体均值和总体标准差的可能性就越大。

但是样本多大才足够呢？bigger is better, but how big is big enough? 这取决于总体方差。方差越大，需要的样本数就越多。

置信水平 - 置信区间 - 样本大小 - 总体方差


### 写一个程序，表达总体方差对估计均值时的置信区间的影响？

```python
def testSamples(numTrials, sampleSize, tightSD=1, wideSD=100):
    tightMeans, wideMeans = [], []
    for t in range(numTrials):
        sampleTight, sampleWide = [], []
        for i in range(sampleSize):
            sampleTight.append(random.gauss(0, tightSD))
            sampleWide.append(random.gauss(0, wideSD))
        tightMeans.append(sum(sampleTight)/len(sampleTight))
        wideMeans.append(sum(sampleWide)/len(sampleWide))
    return tightMeans, wideMeans

# sample_size = 40
sample_size = 4000
tightMeans, wideMeans = testSamples(1000, sample_size, tightSD, wideSD)
pylab.figure('Means of Samples of Size ' + str(sample_size))
pylab.plot(wideMeans, 'y*', label = (' SD = ' + str(wideSD)))
pylab.plot(tightMeans, 'bo', label = ('SD = ' + str(tightSD)))
pylab.xlabel('Sample Number')
pylab.ylabel('Sample Mean')
pylab.title('Means of Samples of Size ' + str(sample_size))
pylab.legend()

pylab.figure('Distribution of wild Sample Means')
pylab.hist(wideMeans, bins = 20, label = (' SD = ' + str(wideSD)))
pylab.title('Distribution of wild Sample Means')
pylab.xlabel('Sample Mean')
pylab.ylabel('Frequency of Occurrence')
pylab.legend()

pylab.figure('Distribution of tight Sample Means')
pylab.hist(tightMeans, bins = 20, label = (' SD = ' + str(tightSD)))
pylab.title('Distribution of tight Sample Means')
pylab.xlabel('Sample Mean')
pylab.ylabel('Frequency of Occurrence')
pylab.legend()

pylab.show()
```

取1000次样本，看1000个样本均值的分布。

样本大小40的话：

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fr6baodlslj30zk0qoadl.jpg)

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fr6bg75xcxj30zk0qowfi.jpg)

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fr6bgh1vtnj30zk0qomy7.jpg)

- 总体的标准差大，样本的均值分布也零散。

样本大小400的话：

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fr6bbqawm0j30zk0qowi2.jpg)

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fr6bgqgfozj30zk0qoab2.jpg)

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fr6bgvb53uj30zk0qo0tq.jpg)

- 增大样本大小，样本均值的分布就收窄了。
- 增加样本数量只会让样本均值的分布更接近正态分布。


### 什么是中心极限定理？

Central Limit Theorem (CLT to its friends)

假设我们可以从一个总体中多次抽取样本，那么各个样本均值的差异性可以使用从同一总体中抽取的单个样本进行估计，这样做的根据就是中心极限定理。

- 我认为上面这句话的表述有误。单个样本没有标准差，如何能估计整体？
- 必须有很多组样本，多组样本的平均值才有平均值的平均值，和平均值的标准差。
- 多组样本的平均值的分布是正态分布。与总体本身的分布无关。

参考：

[怎样理解和区分中心极限定理与大数定律？](https://www.zhihu.com/question/22913867)

[中心极限定理通俗介绍](https://zhuanlan.zhihu.com/p/25241653)

中心极限定理的简单陈述：
1. 给定一组set从同一总体中抽取的足够sufficiently large大的样本，这些样本的均值means of the samples（样本均值the sample means）大致服从正态分布；
2. 这个正态分布的均值近似等于总体均值；
3. 样本均值的方差近似等于总体方差除以样本量。


### 中心极限定理的一个例子——均匀分布的连续骰子平均值的竟然也是正态分布？

```python
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
```

```commandline
Mean of rolling 1 die = 2.5012 Variance = 2.0945
Mean of rolling 10 dice = 2.5085 Variance = 0.2129
Mean of rolling 100 dice = 2.4967 Variance = 0.0201
```

- 每手样本大小越多，方差越小。
- 样本大小增加一个数量级，方差也缩小一个数量级。
- 极端情况，样本只有一个对象，均值和方差表现的就是整体均值和方差。

分布图

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fr769t6d8nj31kw0xcn3a.jpg)

- 如果样本大小为1，样本均值的分布反映的就是总体的分布。在这里几乎是随机均匀分布。
- 只要样本数量足够大，随机抽样样本的均值的分布就体现出正态分布。


### 用带有误差条的图形表示随着样本大小的增加，误差（95%置信水平之下的置信区间）的变化？

```python
def mean_std_of_means(population, sample_sizes = range(50, 2000, 200), num_sample = 20):
    """
    以不同样本大小从总体中随机提取20个样本，计算样本均值的均值和标注差
    :param population: list，总体数据
    :param sample_sizes: list类，样本大小的列表，默认range(50, 2000, 200)
    :param num_sample: int, 样本数量，默认20
    :return: 两个列表，不同样本大小对应的 样本均值的均值和方差
    """
    meanOfMeans, stdOfMeans = [], []
    for sampleSize in sample_sizes:
        sampleMeans = []
        for t in range(num_sample):
            sample = random.sample(population, sampleSize)
            sampleMeans.append(sum(sample)/sampleSize)
        meanOfMeans.append(sum(sampleMeans)/len(sampleMeans))
        stdOfMeans.append(stdDev(sampleMeans))
    return meanOfMeans, stdOfMeans

def sampling_errobar(population, sample_sizes = range(50, 2000, 200), num_sample = 20):
    """
    绘制总体中提取不同大小样本的误差条。
    :param population: list，总体数据
    :param sample_sizes: list类，样本大小的列表
    :return: 一个图表。
    """
    meanOfMeans, stdOfMeans = mean_std_of_means(population, sample_sizes, num_sample)
    pylab.figure('Estimates of Mean Temperature')
    pylab.errorbar(sample_sizes, meanOfMeans,
               yerr = 1.96*pylab.array(stdOfMeans),
               label = 'Estimated mean and 95% confidence interval')
    pylab.xlim(0, max(sample_sizes) + 50)
    pylab.axhline(sum(population)/len(population), linestyle = '--',
              label = 'Population mean')
    pylab.title('Estimates of Mean Temperature')
    pylab.xlabel('Sample Size')
    pylab.ylabel('Mean Temperature(Degrees C)')
    pylab.legend(loc = 'best')

sampling_errobar(population, range(50, 2000, 200), 20)
```

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fr77om2xxcj30zk0qo40r.jpg)

- 所有样本均值都非常接近实际的总体均值。
- 随着样本量的增加，样本均值的误差并不是单调递减的.
- 随着样本量单调变化的是我们对估计出的均值的确信程度。
- 当样本量从50增加到1850时，置信区间从大约±15减少到了大约±2。这是非常重要的。凭运气偶然得到一个好的估计值没有什么意义，我们需要知道对估计值的确信程度。


## 17.3 Standard Error of the Mean


### 为什么不能既保证样本大小又保证样本量？

样本大小影响置信区间，如果多次取样，可能整个的数据量太大，甚至超过了总体量。

我们需要的是一种通过单个样本估计置信区间的方法，这就引出了均值的标准误差这个概念。


### 什么是标准误差standard error of the mean？

大小为n的样本的标准误差standard error of the mean, SE or SEM，就是对同一总体进行无限次大小为n的抽样得到的均值的标准差。

- 虽然不能无限次取样，定义如此，把无限次取样的平均值的标准差看作一次取样的误差。
- 标准误差是一个标注差，置信区间是67%。

很自然地，标准误差取决于n和σ，σ为总体的标准差：

$${\rm SE}=\frac{\sigma}{\sqrt{n}}$$

一次取样的标准误差 = 总体标准差 / 样本大小开根号


### 区分四个概念：样本的标准误差，总体的标准差，一个样本的标准差，多个样本均值的标准差？

样本的标准误差：= (总体标注差 / 样本大小开根号)

总体的标注差：如果有总体数据并可以全部测量，则统计后最准确。但是一般不可知，用样本的标准差代替。

一个样本的标注差：就是一个样本的均值计算出的标准差。~=总体标准差。

多个样本均值的标准差：多个样本多到无穷，收敛于 样本的标准误差 = （总体标注差 / 样本大小开根号）


### 绘图说明"多个样本均值的标准差 收敛于 样本的标准误差"

```python
def standard_error(population, sample_sizes = range(50, 2000, 200), num_sample = 20):
    """
    绘制总体中提取不同大小样本的误差条。
    :param population: list，总体数据
    :param sample_sizes: list类，样本大小的列表
    :return: 一个图表。
    """
    stdOfMeans = mean_std_of_means(population, sample_sizes, num_sample)[1]
    population_deviation = stdDev(population)
    sem = population_deviation / pylab.array(sample_sizes)**0.5
    pylab.figure('SE vs. SD of 20 Means')
    pylab.plot()
    pylab.plot(sample_sizes, stdOfMeans, label = 'Standard Deviation of 20 Means')
    pylab.plot(sample_sizes, sem, label = 'Standard Error of the Mean')
    pylab.xlim(0, max(sample_sizes) + 50)
    pylab.title('SE vs. SD of 20 Means')
    pylab.xlabel('Sample Size')
    pylab.ylabel('Standard Deviation')
    pylab.legend(loc = 'best')

standard_error(population, range(50, 2000, 200), 20)

``` 

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fr79cr14tsj30zk0qo412.jpg)

- 二者趋势一致，都是随着样本数量增加，以n的根号速度减小。
- 由于样本数量只有20个，二者并不一致。
- 用200组样本，二者就很接近了，如下图。

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fr79htfisij30zk0qodia.jpg)


### 用数据说明，可以用足够大的单个样本标注差代替整体标准差。

```python
def sd_of_sample_vs_population(population, sample_sizes = range(50, 2000, 200), num_sample = 20):
    """
    绘图说明"样本标注差与整体标准差的差值随着样本大小增加而变小", 
    可以用足够大的样本的标准差代替整体标注差。
    :param population: list，总体数据
    :param sample_sizes: list类，样本大小的列表
    :param num_sample: int, 样本数量
    :return: 一个图表。
    """
    population_deviation = stdDev(population)
    diffsMeans = []
    for sampleSize in sample_sizes:
        diffs = []
        for t in range(100):
            diffs.append(abs(population_deviation - stdDev(random.sample(population, sampleSize))))
        diffsMeans.append(sum(diffs) / len(diffs))
    pylab.figure('Sample SD vs Population SD with ' + str(num_sample) + ' Samples')
    pylab.plot(sample_sizes, diffsMeans)
    pylab.xlabel('Sample Size')
    pylab.ylabel('Abs(Pop. Std - Sample Std)')
    pylab.title('Sample SD vs Population SD with ' + str(num_sample) + ' Samples')

sd_of_sample_vs_population(population, range(2, 200, 2), 100)

```

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fr79x8z7lqj31kw10w0yx.jpg)
 
- 可见样本大小达到30～40左右以后，标注差差值的大小就变化不大了。
- 因此一个样本有30～40个，就足够有代表性了。
- 因此可以用一个样本，计算均值，估算标准误差。


### 用数据验证用样本标准差估计标准误差的可靠性。

人们经常使用样本标准差代替（通常是未知的）总体标准差来估计标准误差。

如果样本足够大，而且总体分布与正态分布差别不是很大的话，使用这种方法通过经验法则来计算置信区间也是完全可以的。

2你们是不是很喜欢“选择一个足够大的样本”这种简明的指示？不幸的是，当你对总体的基本信息知之甚少的时候，没有一个简单方法可以选择出足够大的样本。

很多统计学家认为，当总体分布近似于正态分布时，30~40个样本已经足够大了。

对于更小的样本，最好使用t分布计算置信区间。t分布与正态分布很相似，但具有肥尾特点，所以算出来的置信区间要更宽一些。

这意味着什么呢？如果我们使用一个包括200个对象的样本，就可以：

- 计算该样本的均值和标准差；
- 使用该样本的标准差估计标准误差；
- 使用估计出的标准误差生成样本均值的置信区间。

```python
def check_sampling_error(population, sampleSize):
    """
    验证用样本标准差估计标准误差的可靠性，看看是否能够达到期望的置信水平。
    :param population: list，总体数据
    :param sampleSize: int, 样本大小
    :return:
    """
    popMean = sum(population)/len(population)
    numGood = 0
    for t in range(10000):
        sample = random.sample(population, sampleSize)
        sampleMean = sum(sample)/sampleSize
        se = stdDev(sample)/sampleSize**0.5
        if abs(popMean - sampleMean) <= 1.96*se:
            numGood += 1
    print('Fraction inside 95% confidence interval =', numGood/10000)


check_sampling_error(population, 200)
```

样本大小200
```commandline
Fraction inside 95% confidence interval = 0.9481
```

样本大小30
```commandline
Fraction inside 95% confidence interval = 0.9356
```

样本大小40
```commandline
Fraction inside 95% confidence interval = 0.9373
```

---
以上，2018-05-11 12:37:06






