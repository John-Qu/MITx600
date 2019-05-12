# 16 MONTE CARLO SIMULATION


### 什么是蒙特卡洛模拟。

蒙特卡罗模拟用于求事件的近似概率，它多次执行同一模拟，然后将结果进行平均。


### 概率和赌运气有什么联系？

乌拉姆不是第一个想使用概率工具来理解赌运气游戏a game of chance的数学家。

概率的历史与赌博的历史紧密相连。不确定性的存在使赌博成为可能，赌博的存在又促进了用来解释不确定性的数学理论的发展。

为概率论的奠基做出重要贡献的有卡尔达诺Cardano、帕斯卡Pascal、费马Fermat、伯努利Bernoulli、棣莫弗de Moivre和拉普拉斯Laplace，他们的目的都是为了更好地理解（也可能是赢得）赌运气游戏。


## 16.1 Pascal's Problem


### 帕斯卡和费马怎么回答他朋友的问题？

帕斯卡对概率论这个领域产生兴趣是因为他的朋友问了他一个问题，即“连续掷一对骰子24次得到两个6”这个赌注是否有利可图。这在17世纪中叶是非常困难的一个问题。

- 第一次投掷时，每个骰子掷出6的概率是1/6，所以两个骰子都掷出6的概率是1/36；
- 因此，第一次投掷时没有掷出两个6的概率是1 - 1/36 = 35/36；
- 因此，连续24次投掷都没有掷出两个6的概率是(35/36)24，差不多是0.51；
- 所以掷出两个6的概率是1 - (35/36)24，大约是0.49。长期来看，在24次投掷中掷出两个6这个赌注是无利可图的。

关键思想：
正反转换 独立相乘 长期

不懂概率分析，可以用代码来模拟出结果：

```python
import random


def rollDie():
    return random.choice([1,2,3,4,5,6])


def checkPascal(numTrials):
    """假设numTrials是正整数
       输出获胜概率的估值"""
    numWins = 0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print('Probability of winning =', numWins/numTrials)


checkPascal(1000000)
```
等两分钟，terminal输出：
Probability of winning = 0.492051

在Python shell中输入1-(35/36)**24会计算出0.49140387613090342。


## 16.2 Pass or Don't Pass


### 过线、不过线游戏怎么描述？

有些赌运气游戏的问题是很难找到答案的。在双骰儿赌博中，掷手shooter（即掷骰子的人）可以选择在“过线pass line”或“不过线don't pass line”之间投注。

过线：如果初掷是“自然点natural”（7或11），那么掷手获胜；如果初掷是“垃圾点craps”（2、3或12），那么掷手失败。如果掷出其他数字，这个数字就成为“点数point”，掷手继续掷骰子。如果掷手在掷出7之前掷出这个点数，那么掷手获胜，否则掷手失败。

- 7就是线？

不过线：如果初掷是7或11，那么掷手失败；如果初掷是2或3，那么掷手获胜；如果初掷是12，则是平局（赌博的行话称为push）。如果掷出其他数字，那么这个数字成为“点数”，掷手继续掷骰子。如果掷手在掷出这个点数之前掷出7，那么掷手获胜，否则掷手失败。

是否有一种赌注比另一种更好呢？还是说二者都一样？通过分析推导可以回答这些问题，但（至少对我们来说）编写一个程序的方式会更容易。


### 投资回报率怎么写？在掷骰子游戏中为什么可以那么写？

投资回报率Return on Investment由以下公式定义：

(更精确地说，这个公式定义的是“简单ROI”，它不考虑投资开始时和取得回报时的时间价值方面的差异。当进行投资和看到财务上的收益之间的时间非常长的时候（例如，在大学教育上的投资），应该考虑时间价值。对于双骰儿游戏来说，这不是什么问题。)

ROI = 投资纯收益 / 投资成本 = (投资收益 - 投资成本) / 投资成本

在骰子游戏中，下100次注，每次1元钱，赢了拿走2元，输了什么也拿不回来来。所以总的投资成本就是下注次数。

投资纯收益 = 拿回的钱 - 给出的钱 = 赢的次数*2 - 下注次数*1 = 赢的次数 - 输的次数，

所以：

举例来说，如果你对过线投注100次，并且获胜50次，那么你的ROI就是：

$$\frac{50-50}{100}=0$$

如果你对不过线投注100次，并且获胜25次，平局5次，那么ROI就应该是：

$$\frac{25-70}{100}=\frac{-45}{100}=-4.5$$


### 双骰子游戏对过线和不过线的模拟结果，怎么理解？

```commandline
# crapsSim(20, 10)
# Pass: Mean ROI = 2.0% Std. Dev. = 14.6969%
# Don't pass: Mean ROI = -6.0% Std Dev = 14.9666%

# crapsSim(20, 10)
# Pass: Mean ROI = -0.0% Std. Dev. = 26.8328%
# Don't pass: Mean ROI = -3.5% Std Dev = 25.7924%

# crapsSim(20, 10)
# Pass: Mean ROI = -14.0% Std. Dev. = 19.5959%
# Don't pass: Mean ROI = 11.0% Std Dev = 18.8149%

# crapsSim(100000, 10)
# Pass: Mean ROI = -1.463% Std. Dev. = 0.3025%
# Don't pass: Mean ROI = -1.3021% Std Dev = 0.2844%

# crapsSim(20, 100000)
# Pass: Mean ROI = -1.3093% Std. Dev. = 22.3475%
# Don't pass: Mean ROI = -1.4659% Std Dev = 22.0177%

# def rollDie():
#     return random.choice([1,1,2,3,3,4,4,5,5,5,6,6])
    
# crapsSim(1000000, 10)会得到以下结果：

Pass: Mean ROI = 6.7385% Std. Dev. = 0.13%
Don't pass: Mean ROI = -9.5186% Std Dev = 0.1226%
```

1. 每手投注20把，做10次游戏，结果很不稳定。标准差非常大。
2. 每手投注十万把，做10次游戏，标准差变小，ROI收敛，接近于概率分析值: 过线ROI为-1.414%，不过线ROI为-1.364%。
3. 看上去似乎不过线的投注稍好一点，但我们完全不能指望靠它来挣钱。如果过线投注和不过线投注的95%置信区间没有重合，就可以认为这两个均值之间的差异在统计上是显著的。7但是它们重合了，所以我们不能得出任何确定的结论。
4. 假设不增加每次游戏的手数，而是增加游戏次数,每手投注20把，做十万次模拟，标准差还是很高。
5. 骰子的微小改变，会导致获胜几率的巨大倾斜。


### 为什么不增加每次游戏的手数，而是增加游戏次数,每手投注20把，做十万次模拟，标准差还是很高？

按照我过去的理解，多做实验，在更多的数据中取得平均值和标准差，标准差会更小。这里或许有特殊。

```python
def crapsSim(handsPerGame, numGames):
    """假设handsPerGame和numGames是正整数
       玩numGames次游戏，每次handsPerGame手；输出结果。"""
    games = []

    #玩numGames次游戏，为了取平均值。
    for t in range(numGames):
        c = CrapsGame()
        for i in range(handsPerGame):
            c.playHand_with_dict()
        games.append(c)

    #为每次游戏生成统计量
    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        # Return on Investment
        wins, losses = g.passResults()
        pROIPerGame.append((wins - losses)/float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins - losses)/float(handsPerGame))

    #生成并输出摘要统计量
    # 先乘100，再做round，不然会出尾数。
    meanROI = str(round((100*sum(pROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100*stdDev(pROIPerGame), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev. =', sigma)
    meanROI = str(round((100*sum(dpROIPerGame)/numGames), 4)) +'%'
    sigma = str(round(100*stdDev(dpROIPerGame), 4)) + '%'
    print('Don\'t pass:','Mean ROI =', meanROI, 'Std Dev =', sigma)
```

handsPerGame影响的是wins和losses的值。它们不能太小，因为要做差后再做除法。

numGames影响的是games列表的长度，用来算取平均数和标准差。

经过几轮实验，确实后者对标准差的影响很小。

这一观察更正了我对数组长度对标准差影响的认识。


### 双骰子游戏，过线和不过线投注的模拟，代码怎么写？

```python
import random, pylab

# 引用stdDev就够了。stdDev引用的variance不用单独提出来。
# 注意引用module中的可执行命令都会得到执行，最好先行注释掉。
from em_15_3_flip import stdDev


def rollDie():
    """
    正常的单骰子，随机得到1～6之间的一个正整数。
    :return: 正整数，在1～6之间
    """
    return random.choice([1,2,3,4,5,6])
    # return random.choice([1,1,2,3,3,4,4,5,5,5,6,6])


class CrapsGame(object):
    """
    给双骰子赌博建抽象类，特殊目的是比较pass和dp的投资回报率。
    因此，没有区分game是pass line还是don't pass line.
    而是分别建立instance attibutes。
    """
    def __init__(self):
        self.passWins, self.passLosses = 0, 0
        self.dpWins, self.dpLosses, self.dpPushes = 0, 0, 0

    def playHand(self):
        # 记录双骰子结果
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else: # throw = 2或3
                self.dpWins += 1
        else: # throw = 4 5 6 8 9 10
            # 上次throw存为point点数
            point = throw
            while True:
                # 再扔一把
                throw = rollDie() + rollDie()
                if throw == point: # 先达到了点数
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7: # 先达到了7线
                    self.passLosses += 1
                    self.dpWins += 1
                    break

    def playHand_with_dict(self):
        """playHand函数的另外一种更快的实现方式"""
        pointsDict = {4: 1 / 3, 5: 2 / 5, 6: 5 / 11, 8: 5 / 11, 9: 2 / 5, 10: 1 / 3}
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else:
                self.dpWins += 1
        else:
            # 下面比的是出现的相对概率，道理如下：
            # 比如8点，两个骰子组合出8点有5种情况，组合出7点有6种情况。掷出11种情况中的任何一种，游戏结束。
            # 只看这11种可以让游戏结束的组合，那么8点相对于7点，出现的相对概率是5/11。
            # 上面那句也可以理解成：把[0, 1)区间均匀分成了11份。生成一个[0,1)间的随机数，如果它落在左边5份，则认为是8点，如果它落在了右边6份，则认为是7点。
            if random.random() <= pointsDict[throw]:  # 在掷出7之前掷出点数
                self.passWins += 1
                self.dpLosses += 1
            else:  # 在掷出点数之前掷出7
                self.passLosses += 1
                self.dpWins += 1

    # 把pass line的信息打包输出。
    def passResults(self):
        return (self.passWins, self.passLosses)

    # 把don't pass line的信息打包输出。
    def dpResults(self):
        return (self.dpWins, self.dpLosses, self.dpPushes)


def crapsSim(handsPerGame, numGames):
    """假设handsPerGame和numGames是正整数
       玩numGames次游戏，每次handsPerGame手；输出结果。"""
    games = []

    #玩numGames次游戏，为了取平均值。
    for t in range(numGames):
        c = CrapsGame()
        for i in range(handsPerGame):
            c.playHand_with_dict()
        games.append(c)

    #为每次游戏生成统计量
    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        # Return on Investment
        wins, losses = g.passResults()
        pROIPerGame.append((wins - losses)/float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins - losses)/float(handsPerGame))

    #生成并输出摘要统计量
    # 先乘100，再做round，不然会出尾数。
    meanROI = str(round((100*sum(pROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100*stdDev(pROIPerGame), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev. =', sigma)
    meanROI = str(round((100*sum(dpROIPerGame)/numGames), 4)) +'%'
    sigma = str(round(100*stdDev(dpROIPerGame), 4)) + '%'
    print('Don\'t pass:','Mean ROI =', meanROI, 'Std Dev =', sigma)


# crapsSim(20, 10)
# Pass: Mean ROI = 2.0% Std. Dev. = 14.6969%
# Don't pass: Mean ROI = -6.0% Std Dev = 14.9666%

# crapsSim(20, 10)
# Pass: Mean ROI = -0.0% Std. Dev. = 26.8328%
# Don't pass: Mean ROI = -3.5% Std Dev = 25.7924%

# crapsSim(20, 10)
# Pass: Mean ROI = -14.0% Std. Dev. = 19.5959%
# Don't pass: Mean ROI = 11.0% Std Dev = 18.8149%

# crapsSim(100000, 10)
# Pass: Mean ROI = -1.463% Std. Dev. = 0.3025%
# Don't pass: Mean ROI = -1.3021% Std Dev = 0.2844%

# crapsSim(20, 100000)
# Pass: Mean ROI = -1.3093% Std. Dev. = 22.3475%
# Don't pass: Mean ROI = -1.4659% Std Dev = 22.0177%

```


### 怎样模拟灌了铅的骰子？

```python
def rollDie():
    """
    正常的单骰子，随机得到1～6之间的一个正整数。
    :return: 正整数，在1～6之间
    """
    return random.choice([1,2,3,4,5,6])
    return random.choice([1,1,2,3,3,4,4,5,5,5,6,6])
```


### 为什么可以用查表法提高playhand的性能？

关键发现：

playHand的运行时间依赖于其中循环执行的次数。理论上，这个循环可以执行无限次，因为掷出7或者点数的时间是没有限制的。

playHand的结果与循环执行的次数没有关系，只与跳出循环的条件有关。

对于每个可能的点数，我们可以很容易地计算出掷出7之前掷出这个点数的概率。

我的理解：

这里比的是出现的相对概率，道理如下：

比如8点，两个骰子组合出8点有5种情况，组合出7点有6种情况。掷出11种情况中的任何一种，游戏结束。

只看这11种可以让游戏结束的组合，那么8点相对于7点，出现的相对概率是5/11。

上面那句也可以理解成：把[0, 1)区间均匀分成了11份。生成一个[0,1)间的随机数，如果它落在左边5份，则认为是8点，如果它落在了右边6份，则认为是7点。

```python
    if random.random() <= pointsDict[throw]:  # 在掷出7之前掷出点数
```


## 16.4 Finding pi


### 随机的过程可以用来估算确定的事情？

Buffon和Laplace用随机扔针来估算pi值。

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/19.d16z.003.png)

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/19.d16z.004.png)

```python
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
```


### 从估算pi值的输出中，吸取什么重要教训？

```commandline
Est. = 3.14844, Std. dev. = 0.04789, Needles = 1000
Est. = 3.13918, Std. dev. = 0.0355,  Needles = 2000
Est. = 3.14108, Std. dev. = 0.02713, Needles = 4000
Est. = 3.14143, Std. dev. = 0.0168,  Needles = 8000
Est. = 3.14135, Std. dev. = 0.0137,  Needles = 16000
Est. = 3.14131, Std. dev. = 0.00848, Needles = 32000
Est. = 3.14117, Std. dev. = 0.00703, Needles = 64000
Est. = 3.14159, Std. dev. = 0.00403, Needles = 128000
```
- 估算出来的pi值可能跑得更差，那没关系，考虑标注差，真是值都在一个标准差距离内，那就是很好的估计。
- 给出一个好的答案是不够的，还必须有足够的理由来确信它真是个好的答案。
- 随着扔针数量翻倍，标准差在稳步缩小。
- 标准差缩小到一定程度，我们就有信心说：这个结论在统计上是有效的。
- 统计上有效的结论 != 正确的结论
- for having confidence in the validity of the result, a necessary condition, not a sufficient condition.

```commandline
Est. = 1.57422, Std. dev. = 0.02394, Needles = 1000
Est. = 1.56959, Std. dev. = 0.01775, Needles = 2000
Est. = 1.57054, Std. dev. = 0.01356, Needles = 4000
Est. = 1.57072, Std. dev. = 0.0084,  Needles = 8000
Est. = 1.57068, Std. dev. = 0.00685, Needles = 16000
Est. = 1.57066, Std. dev. = 0.00424, Needles = 32000
```

- 上面的数据在统计上有效，但是不正确。
- 模型正确model is correct + 正确实现correctly implemented + 真实性验证validate against reality.


## 16.5 Some Closing Remarks About Simulation Models


### 分析模型在科学上的地位？

在科学发展的大部分时间中，理论学家使用数学技术构建纯分析模型，根据一组参数和初始条件来预测系统的行为，并由此发展出了很多重要的数学工具，从微积分到概率论。这些工具帮助科学家对微观物质世界有了更加精确的认识。

For most of the history of science, 
theorists used mathematical techniques 
to construct purely analytical models 
that could be used to predict the behavior of a system 
from a set of parameters and initial conditions.

This led to the development of important mathematical tools 
ranging from calculus to probability theory. 
These tools helped scientists develop 
a reasonably accurate understanding of the macroscopic physical world.


### 模拟模型相对于分析模型有什么优势？

- 人们对社会科学（如经济学）的兴趣不断增加，需要对不容易使用数学处理的系统进行很好地建模；
- 要建模的系统越来越复杂，相对于构建精确的分析模型，逐渐优化一系列模拟模型要更容易一些；
- 相对于分析模型，更容易从模拟模型中提取出有用的中间结果intermediate results，例如进行“如果……那么……”what if的实验；
- 计算机的出现使运行大规模模拟可行。模拟的作用一直受到手工计算时间的限制，直到20世纪中期现代计算机的出现。

- 数学描述不清的。
- 复杂系统。
- 改变条件看现象。
- 计算能力不受限了。


### 模拟模型的局限是什么？

模拟模型是描述性而非规定性的。它可以描述出系统如何在给定的条件下运行，但不能告诉我们如何安排条件才能使系统运行得最好。模拟模型只会进行描述，不会进行优化。但这并不是说模拟不能作为优化过程的一部分，例如，寻找参数设定的最优集合时，经常使用模拟作为搜索过程的一部分。

descriptive 
not
prescriptive 

how a system works under given conditions
not
how to arrange the conditions to make the system work best

A simulation does not optimize, it merely describes.


### 模拟模型可以按照哪三个维度分类？

确定性与随机性
静态与动态
离散与连续


### 确定性模拟和随机性模拟各有什么特点？

确定性模拟的行为完全由模型定义，重新运行模拟不会改变结果。当要建模的系统过于复杂而不能使用分析模型时，通常使用确定性模拟模型，例如处理器芯片的性能。

- 这个没有见过例子。

随机性模拟在模型中引入了随机性，多次运行同一个模型会得到不同的结果。这种随机因素要求我们生成多个结果以找出结果的可能范围。需要生成10个、1000个还是100 000个结果是个统计问题，正如我们之前讨论过的那样。

- 这个在本书中见过例子。


### 静态模型和动态模型各有什么特点？

在静态模型中，时间的作用不大。本章中估计π值的扔针模拟就是一个静态模型。

在动态模型中，时间（或类似的项目or some analog）是个基本要素plays an essential role。在第14章的一系列随机游走模拟中，步数就是时间的代理项surrogate for time。


### 离散模型与连续模型各有什么特点，在特定场景中如何选择？

在离散模型中，相关变量的值是可数的，例如所有值都是整数。

在连续模型中，相关变量的值位于一个不可数集合中，例如实数集合。

假设我们要分析高速公路上的车流量，可以选择对每辆车进行建模，这样就会得到一个离散模型。或者，也可以将交通情况看作一个流，流中的变化可以使用微分方程描述，这就是一个连续模型。
在本例中，离散模型更接近实际情况（没有人能驾驶半辆汽车，尽管有些车的体积只是其他车的一半），但在计算上要比连续模型更复杂。

实际上，模型一般既包括离散的部分，也包括连续的部分。
举例来说，如果要对人体中的血流建模，既可以使用描述血液的离散模型（即对血液中的细胞建模），也可以使用描述血压的连续模型。

---
以上，2018-05-09 18:38:04