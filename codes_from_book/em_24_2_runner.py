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