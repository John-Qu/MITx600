# 14 RANDOM WALK AND MORE ABOUT DATA VISUALIZATION


### 确定性程序的特点怎么描述？

同样的输入，一样的输出。

时间一致性。


### 随机过程的特点怎么描述？

下一刻的状态，依赖于一些随机因素，那么这个过程就是随机的。

听起来就是真实世界的情况。

can rarely make definitive statements about what they will do.

can only make probilistic statements about what they might do.


### Stochastic这个词来自哪里？

希腊文stokhastikos, capable of divining。

verb

1 Fergus divined how afraid she was: guess, surmise, conjecture, deduce, infer; discern, intuit, perceive, recognize, see, realize, appreciate, understand, grasp, comprehend; informal figure (out), savvy.

2 they divined that this was an auspicious day: foretell, predict, prophesy, forecast, foresee, prognosticate.

所以说，随机程序只是要一个好结果，但不保证精确。

> A stochastic program is aimed at getting a good result, but the exact results are not guarranteed.


### 什么是模拟模型simulation model？

是个实验设备 an experimental device，提供建模对象系统的可能行为中的有用信息。

用来预测predict实体系统physical system的未来状态，比如地球50年的温度。

或

替代in lieu of实体实验physical experiments(太贵，太久，太危险),比如修改税法。


### 模型与现实，记住真什么真理truism箴言？

All models are wrong, but some are useful.

- George E.P. Box


## 14.1 Random Walks


### 布朗运动的接力跑？

公元前60年，罗马诗人Titus Lucretius长诗On the Nature of Things.

1827年，苏格兰botanist植物学家Robert Brown，花粉悬浮在水里做随机运动。

1900年，Louis Bachelier的博士论文The Theory of Speculation

1905年，爱因斯坦用同样的数学模型，证明原子的存在。


## 14.2 The Drunkard's Walk


### 醉汉问题怎么描述？

> 一个酩酊大醉的农夫站在一片田地的正中央，他每秒钟都会向一个随机的方向迈出一步。那么1000秒之后，他与原点的期望距离是多少？如果他走了很多步，那么会离原点越来越远，还是更可能一遍又一遍地走回原点，并停留在附近？

是收敛，还是发散。 


### 为什么要用简单的输入情形手工推演？

给自己一个直觉的认识。然后再用程序证明。

> 看一下右图中的笑脸，可以看出，有0.25的概率距离为0个单位，有0.25的概率距离为2个单位，有0.5的概率距离为根号2个单位。所以，平均来看，他走出两步之后，会比一步之后更加远离原点。
那么第三步之后呢？如果第二步走到上面或者下面的笑脸，那么第三步会有一半可能使离原点更近，也有一半可能离原点更远。如果第二步走到左侧的笑脸（即原点），那么第三步会使农夫离开原点。如果第二步走到右侧的笑脸，那么第三步会有0.25的可能离原点更近，0.75的可能离原点更远。
看上去似乎醉汉走的步数越多，与原点之间的期望距离就越远。


### 醉汉模型中的几个类分别起什么作用？

在这个问题中，很明显的三个类是：位置、醉汉、和场地。场地把醉汉和位置联系起来。

```python
class Location(object):
    def __init__(self, x, y):
        """x和y为数值型，可以做加减乘除"""
        #成对的变量，用tuple格式做赋值。
        self.x, self.y = x, y

    def move(self, deltaX, deltaY):
        """deltaX和deltaY为数值型，可以是浮点数，即没有限制醉汉的移动方式。
        返回的是另一个Location"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        """other是另一个Location"""
        ox, oy = other.x, other.y
        xDist, yDist = self.x - ox, self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
```

```python
import random, pylab

class Drunk(object):
    def __init__(self, name = None):
        """假设name是字符串
        返回一个只有名字的drunk者"""
        self.name = name

    def __str__(self):
        """匿名者？没有初始化过的drunk者? 怎么用？"""
        #是不是 self.name != None ?
        if self != None:
            return self.name
        return 'Anonymous'
```


```python
class Field(object):
    """场地的本质是关系：谁在哪里，怎么活动。
    数据属性：
    drunks字典，将Drunk者映射到他的Location。
    方法属性：
    addDrunk, 添加Drunk者.
    moveDrunk, 让drunk者用他的方式走到新的Location，更新字典。
    getLoc, 从字典中提取drunk者的当前位置。"""
    def __init__(self):
        """初始化Field不需要参数。
        返回一个字典drunks，绑定Drunk者和他的Location位置。
        注意不只一位drunk者，location也可以重合。"""
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        """只有drunk一个参数。其中移动的步长和方向，是某类drunk的数据属性"""
        #调用Drunk子类中的takeStep方法，让他以自己的方式给出移动向量。
        #调用Location类中的move方法，从原位置经移动向量变为新位置。
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        #某Drunk子类中，定义着对应的takeStep方法，返回的是tuple格式的向量坐标。
        xDist, yDist = drunk.takeStep()
        #从drunks字典中提取drunk者的当前位置。
        currentLocation = self.drunks[drunk]
        #使用Location的move方法获得一个新位置，更新drunks字典中drunk者的位置。
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

```

下面三个Drunk的子类，限制了醉汉的游走方式。

```python
class UsualDrunk(Drunk):
    """drunk者的特征是步态，就是定义如何takeStep。
    正常的drunk向各个方向迈一步的概率一致，步长相同。
    返回的是一个向量的坐标元组。"""
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)


class ColdDrunk(Drunk):
    """这位醉鬼向四个方向的概率都是一样的，但是如果是迈向南方，步子就大一倍。"""
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-2.0), (1.0, 0.0),\
                       (-1.0, 0.0)]
        return random.choice(stepChoices)


class EWDrunk(Drunk):
    """这是个只向东西两侧走的醉鬼。"""
    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
```


### Location类和Field类的定义中，看出什么重大决策？

> Location类开始，这个类虽然简单，但明确体现了两个重要的决策。首先，它告诉我们这个模拟中最多只有两个维度。例如，模拟模型中不会包含高度的变化，这和上面的图形是一致的。其次，因为提供给deltaX和deltaY的值可以是浮点数，不要求是整数，所以这个类没有限制醉汉可能的移动方向。这就对前面的非正式模型进行了扩展。在那个模型中，每一步都是一个长度单位，而且必须平行于X轴或Y轴。

> 图14-2中的Field类也很简单，但也体现了一些值得注意的决策。这个类的作用是将醉汉与位置进行映射。它对位置没有限制，所以可以认为Field的范围是无限的。它允许将多个醉汉以位置随机的方式添加到一个Field对象中。对醉汉移动的方式没有任何限制，没有禁止多个醉汉出现在同一位置，也没有禁止一个醉汉穿过被其他醉汉占据的空间。

重要决策是：不限制什么。

这些限制是在子类中定义的。


### 调试醉汉游走程序时，进行了冒烟测试？

运行drunkTest((0, 1), 100, UsualDrunk)后，得到的结果令人难以置信：

```commandline
UsualDrunk random walk of 0 steps
 Mean = 8.634
 Max = 21.6 Min = 1.4
UsualDrunk random walk of 1 steps
 Mean = 8.57
 Max = 22.0 Min = 0.0
```

走0步的平均距离怎么可能比8还大？我们的模拟模型中肯定至少有一个bug。进行了一番调查之后，问题清楚了。在simWalks中，函数调用walk(f, Homer, numTrials)应该是walk(f, Homer, numSteps)。

这件事给了我们一个非常重要的教训：看到模拟结果时，永远要持有一种怀疑态度。我们应该扪心自问，这个结果是否真的合理，还要使用对结果非常有把握的参数进行“冒烟测试”。

在19世纪，管道工测试封闭管道系统的一种标准做法是为这个系统充满烟雾。后来，电子工程师使用这个术语描述对某种电子设备的首次测试——接通电源并看看是否冒烟。再后来，软件开发者开始使用这个术语描述对程序进行一次快速测试，看看能否产生有用的结果。


### 醉汉游走的规律？

普通醉汉，经过n次单步游走的平均距离，与游走步数n的平方根几乎一致。

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fqvvve9cgej30hs0dcjs1.jpg)

可见这个规律，原理不知道。

是不是跟横平竖直的勾股定理有关？


