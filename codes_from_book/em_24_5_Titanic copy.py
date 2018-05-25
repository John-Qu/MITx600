# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:45:20 2016

@author: johnguttag
"""
import pylab, random

#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers
pylab.rcParams['lines.markersize'] = 10
#set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)

class Passenger(object):
    featureNames = ('C1', 'C2', 'C3', 'age', 'male gender')
#    def __init__(self, pClass, age, gender, survived, name):
#        self.name = name
#        self.featureVec = [0, 0, 0, age, gender]
#        self.featureVec[pClass - 1] = 1
#        #self.featureVec[0] = 0 #Ugly hack
#        self.label = survived
#        self.cabinClass = pClass
#     featureNames = ('C2', 'C3', 'age', 'male gender')
    def __init__(self, pClass, age, gender, survived, name):
        self.name = name
        self.featureVec = [0, 0, 0, age, gender]
        self.featureVec[pClass - 1] = 1
        # 两位二进制本可以表达四个数字
        # if pClass == 2:
        #     self.featureVec = [1, 0, age, gender]
        # elif pClass == 3:
        #     self.featureVec = [0, 1, age, gender]
        # else:
        #     self.featureVec = [0, 0, age, gender] # 这就是一等舱，但是不能计算权重。
        self.label = survived
        self.cabinClass = pClass
    def distance(self, other):
        return minkowskiDist(self.featureVec, other.featureVec, 2)
    def getClass(self):
        return self.cabinClass
    def getAge(self):
        return self.featureVec[3]
    def getGender(self):
        return self.featureVec[4]
    def getName(self):
        return self.name
    def getFeatures(self):
        return self.featureVec[:]
    def getLabel(self):
        return self.label
        
def getTitanicData(fname):
    data = {}
    data['class'], data['survived'], data['age'] = [], [], []
    data['gender'], data['name'] = [], []
    f = open(fname)
    line = f.readline()
    while line != '':
        split = line.split(',')
        data['class'].append(int(split[0]))
        data['age'].append(float(split[1]))
        if split[2] == 'M':
            data['gender'].append(1)
        else:
            data['gender'].append(0)
        if split[3] == '1':
            data['survived'].append('Survived')
        else:
            data['survived'].append('Died')
        data['name'].append(split[4:])
        line = f.readline()
    return data
                
def buildTitanicExamples(fileName):
    data = getTitanicData(fileName)
    examples = []
    for i in range(len(data['class'])):
        p = Passenger(data['class'][i], data['age'][i],
                      data['gender'][i], data['survived'][i],
                      data['name'][i])
        examples.append(p)
    print('Finished processing', len(examples), 'passengers\n')    
    return examples

def accuracy(truePos, falsePos, trueNeg, falseNeg):
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator/denominator

def sensitivity(truePos, falseNeg):
    try:
        return truePos/(truePos + falseNeg)
    except ZeroDivisionError:
        return float('nan')
    
def specificity(trueNeg, falsePos):
    try:
        return trueNeg/(trueNeg + falsePos)
    except ZeroDivisionError:
        return float('nan')
    
def posPredVal(truePos, falsePos):
    try:
        return truePos/(truePos + falsePos)
    except ZeroDivisionError:
        return float('nan')
    
def negPredVal(trueNeg, falseNeg):
    try:
        return trueNeg/(trueNeg + falseNeg)
    except ZeroDivisionError:
        return float('nan')
       
def getStats(truePos, falsePos, trueNeg, falseNeg, toPrint = True):
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    if toPrint:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Pos. Pred. Val. =', round(ppv, 3))
    return (accur, sens, spec, ppv)

def split80_20(examples):
    """
    把实例集用80/20的比例划分为训练集和测试集。
    :param examples: 实例集
    :return: 训练集，测试集
    """
    # 选的是index
    sampleIndices = random.sample(range(len(examples)),
                                  len(examples)//5)
    trainingSet, testSet = [], []
    for i in range(len(examples)):
        # 用index列表做区分
        if i in sampleIndices:
            testSet.append(examples[i])
        else:
            trainingSet.append(examples[i])
    return trainingSet, testSet
    
def randomSplits(examples, method, numSplits, toPrint = True):
    """
    将实例集随机划分多次，运算某种模型得到混淆矩阵的四个值，用各次实验的平均值求四个统计量，可选是否打印，输出混淆矩阵的四个平均值。
    :param examples: 实例集
    :param method: 函数，给他训练集和测试集，给出某种预测的四个统计量
    :param numSplits: 划分多少次，即实验多少次
    :param toPrint: 是否打印统计量
    :return: 真阳性，假阳性，真阴性，假阴性的平均值
    """
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    random.seed(0)
    for t in range(numSplits):
        trainingSet, testSet = split80_20(examples)
        results = method(trainingSet, testSet)
        truePos += results[0]
        falsePos += results[1]
        trueNeg += results[2]
        falseNeg += results[3]
    getStats(truePos/numSplits, falsePos/numSplits,
             trueNeg/numSplits, falseNeg/numSplits, toPrint)
    return truePos/numSplits, falsePos/numSplits,\
             trueNeg/numSplits, falseNeg/numSplits

import sklearn
from sklearn.linear_model import LogisticRegression
from em_15_3_flip import stdDev

def buildModel(examples, toPrint = True):
    featureVecs, labels = [],[]
    for e in examples:
        featureVecs.append(e.getFeatures())
        labels.append(e.getLabel())
    model = LogisticRegression().fit(featureVecs, labels)
    if toPrint:
        print('model.classes_ =', model.classes_)
        for i in range(len(model.coef_)):
            print('For label', model.classes_[1])
            for j in range(len(model.coef_[0])):
                print('   ', Passenger.featureNames[j], '=',
                      model.coef_[0][j])
    return model

def applyModel(model, testSet, label, prob = 0.5):
    """
    将logistic regression模型应用于测试集，将对应于第二个标签的概率于阈值比较作为预测依据，输出混淆矩阵的四个值。
    :param model: 用logistic regression和训练集生成的模型
    :param testSet: 测试集
    :param label: prob对应的第二个标签。
    :param prob: 判断阈值，概率大于它，就预测该实例有第二个标签
    :return: 混淆矩阵的四个值
    """
    testFeatureVecs = [e.getFeatures() for e in testSet]
    probs = model.predict_proba(testFeatureVecs)
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for i in range(len(probs)):
        # probs是列表的列表，内层列表长度为2，因为只有Died和Survived两个标签。
        if probs[i][1] > prob:
            if testSet[i].getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else:
            if testSet[i].getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

def lr(trainingData, testData, prob = 0.5):
    """
    调用各函数，用训练集计算logistic regression模型、用测试集运行模型，得到混淆矩阵四值列表。
    :param trainingData: 训练集
    :param testData: 测试集
    :param prob: 对测试集应用模型时，判断是否打标的概率阈值。
    :return: 混淆矩阵四个值组成的元组
    """
    model = buildModel(trainingData, False)
    results = applyModel(model, testData, 'Survived', prob)
    return results



def buildROC(trainingSet, testSet, title, plot = True):
    model = buildModel(trainingSet, False)
    xVals, yVals = [], []
    p = 0.0
    sensi_p_pairs = {}
    while p <= 1.0:
        truePos, falsePos, trueNeg, falseNeg =\
                               applyModel(model, testSet,
                               'Survived', p)
        xVals.append(1.0 - specificity(trueNeg, falsePos))
        sensi = sensitivity(truePos, falseNeg)
        yVals.append(sensi)
        sensi_p_pairs[sensi] = p
        p += 0.01
    auroc = sklearn.metrics.auc(xVals, yVals, True)
    if plot:
        pylab.plot(xVals, yVals)
        pylab.plot([0,1], [0,1])
        title = title + '\nAUROC = ' + str(round(auroc,3))
        pylab.title(title)
        pylab.xlabel('1 - specificity')
        pylab.ylabel('Sensitivity')
    return auroc, sensi_p_pairs

def mean_ROC(examples, num_trail, title, plot = True):
    xVals, yVals = [], []
    p = 0.0
    sensi_p_pairs = {}
    while p <= 1.0:
        stats = testModels(examples, num_trail, False, False, p)
        accs, sens, specs, ppvs, aurocs = [], [], [], [], []
        for stat in stats:
            accs.append(stat[0])
            sens.append(stat[1])
            specs.append(stat[2])
            ppvs.append(stat[3])
            aurocs.append(stat[4])
        mean_spec = sum(specs)/len(specs)
        xVals.append(1.0 - mean_spec)
        mean_sensi = sum(sens)/len(sens)
        yVals.append(mean_sensi)
        sensi_p_pairs[mean_sensi] = p
        p += 0.01
    auroc = sklearn.metrics.auc(xVals, yVals, True)
    if plot:
        pylab.plot(xVals, yVals)
        pylab.plot([0,1], [0,1])
        title = "Mean" + title + '\nAUROC = ' + str(round(auroc,3))
        pylab.title(title)
        pylab.xlabel('1 - specificity')
        pylab.ylabel('Sensitivity')

#random.seed(0)
#trainingSet, testSet = split80_20(examples)
#buildROC(trainingSet, testSet, 'ROC for Predicting Survival, 1 Split')

def testModels(examples, numTrials, printStats = False, printWeights = False, prob = 0.5):
    """
    多次运行实例集，测试模型统计性能，可打印特征向量影响权重。
    :param examples: 实例集
    :param numTrials: 实验次数
    :param printStats: 是否打印准确度等统计数据
    :param printWeights: 是否打印特征向量对生还的影响权重
    :return: stats, 元组的列表，多次实验得到的五个统计量
    """
    stats, weights = [], [[], [], [], [], []]
    for i in range(numTrials):
        training, testSet = split80_20(examples)
        xVals, yVals = [], []
        for e in training:
            xVals.append(e.getFeatures())
            yVals.append(e.getLabel())
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        model = sklearn.linear_model.LogisticRegression().fit(xVals,
                                                              yVals)
        for i in range(len(Passenger.featureNames)):
            weights[i].append(model.coef_[0][i])
        truePos, falsePos, trueNeg, falseNeg =\
                         applyModel(model, testSet, 'Survived', prob)
        auroc = buildROC(training, testSet, "auroc", False)[0]
        tmp = getStats(truePos, falsePos, trueNeg, falseNeg, False)
        stats.append(tmp + (auroc,))
    print('Averages for', numTrials, 'trials') #下面两个项目至少打印一项，所以这句放在二者外面。
    if printWeights:
        for feature in range(len(weights)):
            featureMean = sum(weights[feature])/numTrials
            featureStd = stdDev(weights[feature])
            print(' Mean weight of', Passenger.featureNames[feature],
              '=', str(round(featureMean, 3)) + ',',
              '95% confidence interval =', round(1.96*featureStd, 3))
    if printStats:
        summarizeStats(stats)
    return stats


def summarizeStats(stats):
    """
    优化格式，用置信区间的形式，打印多次实验的统计信息。
    :param stats: 元组的列表，多次实验得到的准确度、灵敏度、特异度、阳性预测值和AUROC"
    :return: None
    """
    #定义带置信区间的打印格式
    def printStat(X, name):
        mean = round(sum(X)/len(X), 3)
        std = stdDev(X)
        print(' Mean', name, '=', str(mean) + ',',
               '95% confidence interval =', round(1.96*std, 3))
    #把数据区分出来，分别放入列表中
    accs, sens, specs, ppvs, aurocs = [], [], [], [], []
    for stat in stats:
        accs.append(stat[0])
        sens.append(stat[1])
        specs.append(stat[2])
        ppvs.append(stat[3])
        aurocs.append(stat[4])
    #打印输出
    printStat(accs, 'accuracy')
    printStat(sens, 'sensitivity')
    printStat(specs, 'specificity')
    printStat(ppvs, 'pos. pred. val.')
    printStat(aurocs, 'AUROC')

#提取实例集，这个能不注释掉。
examples = buildTitanicExamples('TitanicPassengers.txt')

#Look at mean statisics
testModels(examples, 100, True, False)

#Look at weights
# testModels(examples, 100, False, True)

#Look at changing prob
# random.seed(0)
# trainingSet, testSet = split80_20(examples)
# model = buildModel(trainingSet, False)
# print('Try p = 0.1')
# truePos, falsePos, trueNeg, falseNeg =\
#                   applyModel(model, testSet, 'Survived', 0.1)
# getStats(truePos, falsePos, trueNeg, falseNeg)
# print('Try p = 0.3')
# truePos, falsePos, trueNeg, falseNeg = \
#     applyModel(model, testSet, 'Survived', 0.3)
# getStats(truePos, falsePos, trueNeg, falseNeg)
# print('Try p = 0.6')
# truePos, falsePos, trueNeg, falseNeg = \
#     applyModel(model, testSet, 'Survived', 0.6)
# getStats(truePos, falsePos, trueNeg, falseNeg)
# print('Try p = 0.9')
# truePos, falsePos, trueNeg, falseNeg =\
#                   applyModel(model, testSet, 'Survived', 0.9)
# getStats(truePos, falsePos, trueNeg, falseNeg)

#Look at ROC
#random.seed(0)
# trainingSet, testSet = split80_20(examples)
# sensi_p_pairs = buildROC(trainingSet, testSet, "auroc", plot = True)[1]

#Take a better probability threshold
# print(sensi_p_pairs)
# print('Try p = 0.44')
# truePos, falsePos, trueNeg, falseNeg =\
#                   applyModel(model, testSet, 'Survived', 0.44)
# getStats(truePos, falsePos, trueNeg, falseNeg)
#
# print('Try p = 0.51')
# truePos, falsePos, trueNeg, falseNeg =\
#                   applyModel(model, testSet, 'Survived', 0.51)
# getStats(truePos, falsePos, trueNeg, falseNeg)

#Look at the mean ROC
mean_ROC(examples, 100, "auroc", plot = True):
