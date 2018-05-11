# 18 UNDERSTANDING EXPERIMENTAL DATA


## 18.1 The Behavior of Springs


### 获得弹簧常数，实验科学家怎么做？

做法一：

知道胡克定律，用一个质量，测一个位移，然后计算，确信得到了弹簧常数。

要想保证上面的结论是正确的，下面的情况必须成立。

- 确保实验操作完美，确信已经得到了k。
- 明确知道这次实验在弹性极限之内。

因此：
实验科学里很少这么做事情。

做法二：

在弹簧上悬挂多个重量不断增加的物体，并测量出弹簧每次拉伸的长度，然后绘制结果。


### 为什么要引入目标函数？

不论我们使用何种曲线curve（包括直线）拟合fit数据，都需要某种方法确定哪条曲线才是数据的最佳拟合best fit。这意味着我们需要定义一个目标函数objective function，对曲线拟合数据的程度how well the curve fit the data提供一个定量的评价quantitative assessment。如果我们定义了目标函数，那么找到最优拟合就可以明确表述为一个最优化问题optimization problem：找到一条曲线，使目标函数值the value of that function最小minimize（或最大maximize）。


### 最小二乘作为目标函数有那两个优点？

最常用的目标函数称为最小二乘。令observed和predicted为两个同样长度的向量，observed中是实际测量出来的点，predicted中则是拟合曲线上相应的数据点。

那么，目标函数就可以定义为：

$$\sum^{len(\rm observed)-1}_{i=0}({\rm observed}[i]-{\rm predicted}[i])^2$$

（观察点值 - 预测点值）的平方和

- 对observed和predicted中的点的差进行平方，使得二者之间较大的差比较小的差更重要。
- 对差进行平方还可以消除差的正负影响。



### 为什么叫"回归"分析？

回归分析[regression analysis](https://en.wikipedia.org/wiki/Regression_analysis)？

奠基者之一 K。皮尔逊（K. Pearson, 1856 1936) 在研究父母身高与其子女身高的遗传问题时，观察了 1 078 对夫妇，以每对夫妇的平均身高作为 x，而取他们的一个成年儿子的身高作为 y，将结果在平面直角坐标系上绘成散点图，发现趋势近乎一条直线。计算出的回归直线方程为：

$$ y = 33.73 + 0.516x $$

这种趋势及回归方程总的表明父母平均身高 I 每增加个单位，其成年儿子的身高 y 平均增加 0.516 个单位。这个结果表明，虽然高个子父辈的确有生高个子儿子的趋势，但父辈身高增加一个单位，儿子身高仅增加半个单位左右。反之，矮个子父辈的确有生矮个子儿子的趋势，但父辈身高减少一个单位，儿子身高仅减少半个单位左右。通俗地说，一群特高个子父辈（例如排球运动员）的儿子们在同龄人中平均仅为高个子，一群高个子父辈的儿子们在同龄人中平均仅为略高个子；一群特矮个子父辈的儿子们在同龄人中平均仅为矮个子，一群矮个子父辈的儿子们在同龄人中平均仅为略矮个子，即子代的平均高度向中心回归了。正是因为子代的身高有回到同龄人平均身高的这种趋势，才使人类的身高在一定时间内相对稳定，没有出现父辈个子高其子女更高，父辈个子矮其子女更矮的两极分化现象。这个例子生动地说明了生物学中“种”的概念的稳定性。正是为了描述这种有趣的现象，高尔顿引进了“回归”这个名词来描述父辈身高 x 与子辈身高 y 的关系。尽管“回归”这个名称的由来具有其特定的含义，而人们在研究大量的问题中，其变量 x 与 y 之间的关系并不总是具有这种“回归”的含义，但仍借用这个名词把研究变量 x 与 y 间统计关系的量化方法称为“回归”分析，也算是对高尔顿这位伟大的统计学家的纪念。

C.R.Rao等在Linear Models and Generalizations: Least Squares and Alternatives中解释道 the literature meaning of REGRESSION is " to move in the backward direction"。

看以下两个陈述：
S1: model generates data
S2: data generates model

Rao认为很明显陈述S1才是对的，因为模型实际上本来就是存在的只不过我们不知道(model exists in nature but is unknown to the experimenter)。

先有模型所以我们知道X就能得到Y：

先有模型  =》有了X就有Y（S1）

而“回归”的意思就是我们通过收集X与Y来确定实际上存在的关系模型：

收集X与Y  =》确定模型（S2）

与S1相比，S2就是一个“回到”模型的过程，所以就叫做“regression”。

当然我认为“回归”也有一种回到平均水平的意思：

作者：Keven Howe
链接：https://www.zhihu.com/question/30123729/answer/47111877
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


### ployfit使用的算法称为线性回归linear regression都是线性的吗？

可以是高阶多项式回归polynomial regression。

但是它预测出来的参数都是线性的。Although polynomial regression fits a nonlinear model to the data, the model is linear in the unknown parameters that it estimates.

不懂。

比如：

```python
    model = pylab.polyfit(xVals, yVals, 3) = (a, b, c)
```

是线性的？


### 用一阶多项式线拟合弹簧数据？

```python
def getData(fileName):
    """
    从有两列数据的文件中提取数据
    :param fileName: str
    :return (masses, distances): 质量和位移
    """
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline() #discard header先读一行，跨过标题行
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)
    
def labelPlot():
    """ 为弹簧绘图做标题、x坐标轴、y坐标轴标注。
    """
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81  #acc. due to gravity
    pylab.plot(xVals, yVals, 'bo',
               label = 'Measured displacements')
    labelPlot()
    
def fitData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81 #get force x轴数据变成N了
    pylab.plot(xVals, yVals, 'bo',
               label = 'Measured points')
    labelPlot()                 
    a,b = pylab.polyfit(xVals, yVals, 1)
    estYVals = a*pylab.array(xVals) + b
    print('a =', a, 'b =', b)
    pylab.plot(xVals, estYVals, 'r',
               label = 'Linear fit, k = '
               + str(round(1/a, 5)))
    pylab.legend(loc = 'best')
    
fitData('springData.txt')
```

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fr7finztcej30zk0qoq5e.jpg)


### 用三次多项式拟合弹簧数据，预测性能怎么样？

拟合得挺漂亮，但是远距离预测很不靠谱。

```python
def fitData3(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81 #get force
    pylab.plot(xVals, yVals, 'bo',
               label = 'Measured points')
    labelPlot()
    model = pylab.polyfit(xVals, yVals, 3)
    add_point = pylab.array([15])
    xVals = numpy.hstack((xVals, add_point))
    estYVals = pylab.polyval(model, xVals)
    pylab.plot(xVals, estYVals, 'k--',)
    pylab.legend(loc = 'best')

fitData3('springData.txt')
```

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fr7jmvo0hkj31kw0yrgsh.jpg)

竟然出现了负的位移，重物升到天蓬上面去了。

- 在技术文献中，我们经常会看到类似的图，其中既有原始数据，也有一条拟合数据的曲线。然而，作者往往会将拟合曲线当作对真实情况的描述，而将原始数据看作实验误差。这是非常危险的一种做法。
- 回忆一下，理论上x值和y值应该是线性关系，而不是三次关系。
- 这种情况就是过拟合overfitting的典型例子。
- 当模型过于复杂时，经常会出现过拟合，例如，相对于数据量，参数特别多的时候。
- 发生过拟合时，拟合模型反映出的是数据中的噪声capture noise，而不是数据中有意义的关系meaningful relationship。
- 过拟合模型的预测能力predictive power通常很弱，就像这个例子中一样。


### 可以丢弃实验数据吗？什么情况下可以？

绝对不能仅仅因为要得到更好的拟合而丢弃实验数据。

在这里，我们丢弃了最右侧的点是合理的，因为根据胡克的理论，弹簧是具有弹性极限的。但我们不能凭借这种理由丢弃数据中其他的点。

```python
    xVals = pylab.array(xVals[:-6])
    yVals = pylab.array(yVals[:-6])
```

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fr7jvov2czj31kw0y17bx.jpg)

去掉6个点后，模型确实发生了变化：k显著减小，而且线性拟合和三次拟合几乎没有区别。


### 

