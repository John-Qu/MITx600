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
