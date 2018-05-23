# 24 CLASSIFICATION METHODS


### 什么是classification model？

它是有监督的机器学习中最常用的办法。

A **classification model**, or **classifier分类器**, is used to label an example as belonging to one of a finite set of categories.

比如
- 垃圾邮件分类。

称为
- belonging to a class
- having a label


### 分类学习有几种类型？

单分类学习one-class learning
- 很难找到不属于这个类别的训练数据。
- 通常用于建立异常检测机制，例如在计算机网络中检测未知攻击。

二分类学习two-class learing (binary classification)
- 训练集中的样本全部来自两个类别（通常称为阳性和阴性）。
- 目标是找到一个可以区分两个类别的边界。

多分类学习multi-class learning


## 24.1 Evaluating Classifiers


### 训练一个分类器，要面对什么矛盾？

(1)既能够非常好地拟合现有数据；provide a reasonable good fit for the available data.

(2)又能够对未知数据做出好的预测。have a reasonable chance of making good predictions about as yet unseen data.


### 用训练集训练分类器，最小化训练误差training error时，要满足一定的约束条件subject to certain constraints。设计这些约束条件的目的是什么？

为了提高模型预测未知数据的准确率。to increase the probability that the model will perform reasonably well on as yet unseen data.


### 什么是混淆矩阵confusion matrices？怎么用？

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/27.d24z.001.png)

把classifier的结果统计入混淆矩阵。

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/27.d24z.002.png)


### 怎样用数据评价混淆矩阵？

|                   | Predicted Positive | Predicted Negative |
| ----------------- | :----------------: | :----------------: |
| Actually Positive | +➕ truePos        | +➖ falseNeg       |
| Actually Negative | -➕ falsePos       | -➖ trueNeg       |

- accuracy 精确度，总体预测准确的程度，即正确识别阳性和阴性的比例，(++ --)/( ++ -+ -- +-)
- sensitivity 灵敏度，阳性中，被正确识别的比例，++/(++ +-)
- specificity 专一度，计算阴性中，被正确识别的比例，--/(-- +-)
- positive predicted value 阳性预测中，正确的比例，++/(++ -+)
- negative predicted value 阴性预测中，正确的比例，--/(-- +-)

```python
# -*- coding: utf-8 -*-

def accuracy(truePos, falsePos, trueNeg, falseNeg):
    """
    精确度，计算总体预测准确的程度，即正确识别阳性和阴性的比例，(++ --)/( ++ -+ -- +-)
    :param truePos: int，真阳性++
    :param falsePos: int，假阳性-+
    :param trueNeg: int，真阴性--
    :param falseNeg: int，假阴性+-
    :return: float
    """
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator/denominator


def sensitivity(truePos, falseNeg):
    """
    灵敏度，计算阳性中，被正确识别的比例，++/(++ +-)
    :param truePos: int，真阳性++
    :param falseNeg: int，假阴性+-
    :return: float
    """
    try:
        return truePos/(truePos + falseNeg)
    except ZeroDivisionError:
        return float('nan')

def specificity(trueNeg, falsePos):
    """
    专一度，计算阴性中，被正确识别的比例，--/(-- +-)
    :param trueNeg: int，真阴性--
    :param falsePos: int，假阳性-+
    :return: float
    """
    try:
        return trueNeg/(trueNeg + falsePos)
    except ZeroDivisionError:
        return float('nan')

def posPredVal(truePos, falsePos):
    """
    阳性预测正确比例，++/(++ -+)
    :param truePos: int，真阳性++
    :param falsePos: int，假阳性-+
    :return:
    """
    try:
        return truePos/(truePos + falsePos)
    except ZeroDivisionError:
        return float('nan')

def negPredVal(trueNeg, falseNeg):
    """
    阴性预测正确比例，--/(-- +-)
    :param trueNeg: int，真阴性--
    :param falseNeg: int，假阴性+-
    :return:
    """
    try:
        return trueNeg/(trueNeg + falseNeg)
    except ZeroDivisionError:
        return float('nan')

def getStats(truePos, falsePos, trueNeg, falseNeg, toPrint = True):
    """
    计算classifiers的各种正确比例
    :param truePos: int，真阳性++
    :param falsePos: int，假阳性-+
    :param trueNeg: int，真阴性--
    :param falseNeg: int，假阴性+-
    :param toPrint: bool，是否打印结果，默认True
    :return: (accur, sens, spec, ppv, npv)
    """
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    npv = negPredVal(trueNeg, falseNeg)
    if toPrint:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Pos. Pred. Val. =', round(ppv, 3))
        print(' Neg. Pred. Val. =', round(npv, 3))
    return (accur, sens, spec, ppv, npv)
```


## 24.2 Predicting the Gender of Runners


### 波士顿马拉松，看成绩和年龄，就能大致猜出性别吗？怎么准备类和数据？

```python
# -*- coding: utf-8 -*-

from em_17_1_getBMdata import getBMData
import random
class Runner(object):
    def __init__(self, gender, age, time):
        # 把年龄和成绩组成了特征向量。
        self.featureVec = (age, time)
        # 性别是标签
        self.label = gender

    def featureDist(self, other):
        """计算特征向量的欧氏距离"""
        dist = 0.0 # 初始化，方便后面+=
        for i in range(len(self.featureVec)):
            dist += abs(self.featureVec[i] - other.featureVec[i])**2
        return dist**0.5

    def getTime(self):
        return self.featureVec[1]

    def getAge(self):
        return self.featureVec[0]

    def getLabel(self):
        return self.label

    def getFeatures(self):
        return self.featureVec

    def __str__(self):
        return str(self.getAge()) + ', ' + str(self.getTime())\
               + ', ' + self.label

def buildMarathonExamples(fileName):
    """提取数据，构建Runner对象，添加入examples列表。"""
    data = getBMData(fileName) # 这个bm_results2012.txt文件没有找到
    examples = []
    for i in range(len(data['age'])):
        a = Runner(data['gender'][i], data['age'][i],
                   data['time'][i])
        examples.append(a)
    return examples

def divide80_20(examples):
    """把实例按照80/20比例，分成训练集和测试集"""
    # 随机挑选出测试集实例对应的index。不直接挑，挑剩下的不好处理。
    sampleIndices = random.sample(range(len(examples)),
                                  len(examples)//5)
    trainingSet, testSet = [], []
    for i in range(len(examples)):
        if i in sampleIndices:
            testSet.append(examples[i])
        else:
            trainingSet.append(examples[i])
    return trainingSet, testSet
```


## 24.3 K-nearest Neighbors


### K最近邻方法的原理是什么？

在训练集中找到K个与手中对象最相似的邻居，他们大多数有什么标签，就把手中对像打上什么标签。

比如

- 公园里的鸟，查书，搜索引擎。


### KNN分类法有什么缺点？

如果训练集中的各种标签严重分类不均。

比如

- K个近邻中，真正与手中对象相似的，得不到大多数。


### k最近邻分类器怎么写？

```python
# -*- coding: utf-8 -*-

import pylab, random
from em_24_1_evaluating_classifiers import accuracy
from em_24_2_runner import divide80_20


def findKNearest(example, exampleSet, k):
    """
    用手中的实例，在实例集中找到k个最近邻。
    :param example: 手中有待贴标的对象实例
    :param exampleSet: 作为搜索源的实例集
    :param k: k个最近邻
    :return: k个最近邻的列表，以及相应距离的列表
    """
    kNearest, distances = [], []
    #建立一个列表，包含最初K个样本和它们的距离
    for i in range(k):
        kNearest.append(exampleSet[i])
        distances.append(example.featureDist(exampleSet[i]))
    maxDist = max(distances) #找出最大距离
    #检查其余样本，替换初始邻居
    for e in exampleSet[k:]:
        dist = example.featureDist(e)
        if dist < maxDist:
            #通过查找distances列表，找到原始maxDist的索引位置
            maxIndex = distances.index(maxDist)
            #替换掉索引位置伤的实例和相应距离
            kNearest[maxIndex] = e
            distances[maxIndex] = dist
            #重新计算出k个邻居中的最大距离，进入下一个循环
            maxDist = max(distances)
    return kNearest, distances


def KNearestClassify(training, testSet, label, k):
    """
    使用K最近邻分类器预测testSet中的每个样本是否具有给定的标签
    :param training: 训练集
    :param testSet: 测试集
    :param label: 二类学习的标签
    :param k: 选取K位邻居，过半数占优的标签胜出
    :return: 真阳性、假阳性、真阴性和假阴性的数量
    """
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for e in testSet:
        nearest, distances = findKNearest(e, training, k)
        #进行投票
        numMatch = 0
        for i in range(len(nearest)):
            if nearest[i].getLabel() == label:
                numMatch += 1
        if numMatch > k//2: #预测e具有此标签
            if e.getLabel() == label: #e真有此标签
                truePos += 1
            else: #e却没有此标签
                falsePos += 1
        else: #预测e不具有此标签
            if e.getLabel() != label: #e真没有此标签
                trueNeg += 1
            else: #e却有这个标签
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

```


### k最近邻分类算法的复杂度？

这个实现其实是一种暴力算法。

函数findKNearest的复杂度与exampleSet中的样本数量成线性关系，因为它要计算example与exampleSet中每个元素之间的特征距离。

函数KNearestClassify使用简单的多数票胜出原则来进行分类，它的复杂度是O(len(training)* len(testSet))，因为它要对函数findNearest进行总共len(testSet)次调用。
- 相当于O(n2)?


### 根据标签分布的概率算法怎么写？比k最近邻算法结果差吗？

```python
# -*- coding: utf-8 -*-

def prevalenceClassify(training, testSet, label):
    """
    把训练集中标签所占的比例（流行程度），作为给测试集对象分配标签的概率。
    :param training: 训练集
    :param testSet: 测试集
    :param label: 标签
    :return: 真阳性、假阳性、真阴性和假阴性的数量
    """
    numWithLabel = 0
    for e in training:
        if e.getLabel()== label:
            numWithLabel += 1
    probLabel = numWithLabel/len(training) #标签的概率
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for e in testSet:
        if random.random() < probLabel: #标签概率大于随机数，预测e具有标签
            if e.getLabel() == label: #e真有此标签
                truePos += 1
            else: #e却没有此标签
                falsePos += 1
        else: #预测e不具有此标签
            if e.getLabel() != label: #e真没有此标签
                trueNeg += 1
            else: #e却有这个标签
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

```

```commandline
K最近邻算法的结果：
Accuracy = 0.65
Sensitivity = 0.715
Specificity = 0.563
Pos. Pred. Val. = 0.684

根据标签流行程度概率分配的结果：
准确度=0.514 因为对训练集做了随机性的下采样，准确度低于总体的58%也正常。
灵敏度=0.593
特异度=0.41
阳性预测值=0.57
```


### 在k最近邻算法里，为什么把K设为9？

与训练集有关，实验出来的。

```python
# -*- coding: utf-8 -*-

def findK(training, minK, maxK, numFolds, label):
    """
    k最近邻法，检验什么k值足够好，取一定范围内的奇数值，分别计算numFold次的平均准确度，绘图输出
    :param training: 训练集
    :param minK: 尝试用的最小K值
    :param maxK: 尝试用的最大K值
    :param numFolds: 每个K值采样几次再取平均
    :param label: 标签
    :return: None
    """
    #在k的奇数取值范围内找出平均准确度
    accuracies = []
    for k in range(minK, maxK + 1, 2):
        score = 0.0
        for i in range(numFolds):
            #通过下采样减少计算时间
            fold = random.sample(training, min(5000, len(training)))
            examples, testSet = divide80_20(fold)
            truePos, falsePos, trueNeg, falseNeg =\
                KNearestClassify(examples, testSet, label, k)
            score += accuracy(truePos, falsePos, trueNeg, falseNeg)
        accuracies.append(score/numFolds)
    pylab.plot(range(minK, maxK + 1, 2), accuracies)
    pylab.title('Average Accuracy vs k (' + str(numFolds)\
                + ' folds)')
    pylab.xlabel('k')
    pylab.ylabel('Accuracy')

findK(training, 1, 21, 5, 'M')
```

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/27.d24z.006.png)

- 从图中可以看出，对于5折交叉验证，获得最高准确度的k值是17。
- 当然，k>21时，完全有可能得到更高的准确度。
- 但k达到9时，准确度就在一个相当狭窄的区间内波动，所以我们选择9作为k的值。