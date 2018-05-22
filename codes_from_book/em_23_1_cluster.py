# -*- coding: utf-8 -*-
from em_22_2_animal import minkowskiDist
import pylab

class Example(object):

    def __init__(self, name, features, label = None):
        """
        :param name: 实例名字字符串
        :param features: 一个浮点数数组，或列表也可。
        :param label: 无监督学习，label默认是None
        """
        self.name = name
        self.features = pylab.array(features)
        self.label = label

    def dimensionality(self):
        """
        特征向量的维度
        :return: int
        """
        return len(self.features)

    def getFeatures(self):
        return self.features[:] # 注意这里是复制了一份数组

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self, other):
        # 注意这里的区别写法
        return minkowskiDist(self.features, other.getFeatures(), 2)

    def __str__(self):
        return self.name +':'+ str(self.features) + ':'\
               + str(self.label)


class Cluster(object):

    def __init__(self, examples):
        """假设examples是一个非空的Example类型列表"""
        self.examples = examples
        # 只有examples非空，才能算质心。
        self.centroid = self.computeCentroid()

    def update(self, examples):
        """假设examples是一个非空的Example类型列表
           替换examples；返回质心变化的程度"""
        # 把原来的质心转存起来。
        oldCentroid = self.centroid
        # 用新的实例更新了老实例列表。
        self.examples = examples
        # 计算出新质心。
        self.centroid = self.computeCentroid()
        # 计算新老质心距离。
        return oldCentroid.distance(self.centroid)

    def computeCentroid(self):
        """
        Centroid是簇中所有实例的特征向量的欧氏均值Euclidean mean，类似于质量重心center of mass。
        :return: example类型，一个虚拟实例，它很可能不在原始实例集中。
        """
        # 建一个特征向量那么长的数组
        vals = pylab.array([0.0]*self.examples[0].dimensionality())
        # 累加入数组
        for e in self.examples:
            vals += e.getFeatures() #敢这么写，因为features在实例初始化时已经转变成了数组。
        # 建一个Example实例，用特征均值初始化
        centroid = Example('centroid', vals/len(self.examples))
        return centroid

    def getCentroid(self):
        return self.centroid

    def variability(self):
        totDist = 0.0
        for e in self.examples:
            totDist += (e.distance(self.centroid))**2
        return totDist

    def members(self):
        #做成了genertator
        for e in self.examples:
            yield e

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        #默认打印names时有顺序
        names.sort()
        #注意这个格式，centroid没有重复计算，也没有用封装写法。
        result = 'Cluster with centroid '\
               + str(self.centroid.getFeatures()) + ' contains:\n '
        for e in names:
            # result = result + e + ', '
            result += e + ', '
        return result[:-2] # 不输出结尾的", "。
