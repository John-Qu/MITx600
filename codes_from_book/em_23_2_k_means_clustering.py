# -*- coding: utf-8 -*-
from em_23_1_cluster import Example, Cluster
import random

def dissimilarity(clusters):
    """
    计算簇的集合的相异度。
    :param clusters: 簇的集合
    :return: float相异度，各个簇的差异度的和
    """
    totDist = 0.0
    for c in clusters:
        totDist += c.variability()
    return totDist


def kmeans(examples, k, verbose = False):
    """随机选择k个质心，迭代出k-means法局部最优解。
    :param examples: 原始实例集。
    :param k: 几个簇。
    :param verbose: boolean，是否打印k-means函数迭代的中间结果。
    :return: clusters，迭代收敛完毕的k个簇的列表
    """

    #随机选取k个初始质心，为每个质心创建一个簇
    # 从实例列表中随机选取k个实例，作为质心。
    initialCentroids = random.sample(examples, k)
    clusters = [] # clusters是一个初始随机选择的质心组成的簇的列表
    for e in initialCentroids:
        clusters.append(Cluster([e])) #为每个质心创建一个簇，添加到簇列表中。

    #迭代，直至质心不再改变
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        #创建一个簇的列表，包含k个不同的空列表（簇）。
        newClusters = []
        for i in range(k):
            newClusters.append([])

        #将每个实例分配给最近的质心
        for e in examples:
            #从每个实例出发，逐个遍历它与每个簇的质心之间的距离。
            # 初始化最小距离，用第[0]个簇的质心，"最近簇"的index也初始化为0。
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k): # 从第[i]个质心算起
                distance = e.distance(clusters[i].getCentroid()) #计算新距离
                if distance < smallestDistance: #如果新距离比最小距离还小
                    smallestDistance = distance #替换最小距离
                    index = i #替换"最近簇"的index
            #将e添加到相应簇的实例列表
            newClusters[index].append(e) # 可能发生某个index的簇中没有任何实例

        #这里的策略是不接受空簇，报告异常。
        for c in newClusters:
            if len(c) == 0:
                raise ValueError('Empty Cluster')

        #更新每个簇；检查质心是否变化
        converged = True # 先打标：收敛完毕
        for i in range(k):
            # 用newClusters逐个更新clusters，同时检验质心变化距离
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False # 只要有一个簇的新老质心还有距离，就没有全部收敛

        # 在每个while循环中间，打印输出阶段性成果
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') # 空行分割
    return clusters


def trykmeans(examples, numClusters, numTrials, verbose = False):
    """调用kmeans函数numTrials次，返回相异度最小的结果.
    :param examples: 原始实例集。
    :param numClusters: 几个簇。
    :param numTrials: 把k-means法尝试多少次。
    :param verbose: boolean，是否打印k-means函数运行的结果。
    :return: best，list，几次实验中，差异度最小的那种情况，是kmeans函数返回的簇的列表。
    """

    # 初始化best列表和最小差异度。
    best = kmeans(examples, numClusters, verbose)
    minDissimilarity = dissimilarity(best)
    trial = 1

    while trial < numTrials:
        # 如果失败，存在空簇，则重做。
        try:
            clusters = kmeans(examples, numClusters, verbose)
        except ValueError:
            continue

        # 比较并保留差异度最小的那种情况
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
        trial += 1
    return best
