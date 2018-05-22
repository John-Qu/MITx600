# -*- coding: utf-8 -*-
from em_23_1_cluster import Example
from em_23_2_k_means_clustering import trykmeans, dissimilarity
import pylab, random


def genDistribution(xMean, xSD, yMean, ySD, n, namePrefix):
    """生成由n个实例组成的列表，每个实例的特征向量是二维的实数，符合Gauss分布。
    :param xMean: float，x期望值
    :param xSD: float，x标准差
    :param yMean: float，y期望值
    :param ySD: float，y标准差
    :param n: 实例的数量
    :param namePrefix: str，实例名的前缀，提示批次
    :return: 实例的列表
    """
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(Example(namePrefix+str(s), pylab.array([x, y])))
    return samples


def plotSamples(samples, marker):
    """把一个二维的实例集合画在图板上，并就地标注每个点。
    :param samples: 二维实例列表
    :param marker: 用什么颜色、什么形状标记实例点。
    :return: 绘图输出。
    """
    xVals, yVals = [], []
    # 在每一个实例点位旁写了字，顺路搜集了实例点信息。
    for s in samples:
        x = s.getFeatures()[0]
        y = s.getFeatures()[1]
        pylab.annotate(s.getName(), xy = (x, y),
                       xytext = (x+0.13, y-0.07),
                       fontsize = 'x-large')
        xVals.append(x)
        yVals.append(y)
    # 画出这些实例点。
    pylab.plot(xVals, yVals, marker)


def contrivedTest(numTrials, k, verbose = False):
    """
    把有重合的两个正态分布的点集，分别绘制到同一张图上；检验k-means方法的效果。
    :param numTrials: k-means方法尝试多少次。
    :param k: 分出几个簇。
    :param verbose: 是否打印k-means方法每次迭代的中间结果。
    :return: None，一张图表标注点的位置，打印最终相似聚簇的结果。
    """
    xMean = 3
    xSD = 1
    yMean = 5
    ySD = 1
    n = 10 #每组生成的点数。
    # A集的xy期望中心是(3, 5), xy标准差都是1。
    d1Samples = genDistribution(xMean, xSD, yMean, ySD, n, 'A')
    plotSamples(d1Samples, 'k^')
    # 再造一组数据，就地改变一点分布规律，注意二者有重合。
    # B集的xy期望中心是(6, 6), xy标准差都是1。
    d2Samples = genDistribution(xMean+3, xSD, yMean+1, ySD, n, 'B')
    plotSamples(d2Samples, 'ko')
    clusters = trykmeans(d1Samples+d2Samples, k, numTrials, verbose)
    print('Final result:')
    for c in clusters:
        print('', c)


def contrivedTest2(numTrials, k, verbose = False):
    """
    把有重合的三个正态分布的点集，分别绘制到同一张图上；检验k-means方法的效果。
    :param numTrials: k-means方法尝试多少次。
    :param k: 分出几个簇。
    :param verbose: 是否打印k-means方法每次迭代的中间结果。
    :return: None，一张图表标注点的位置，打印最终相似聚簇的结果。
    """
    xMean = 3
    xSD = 1
    yMean = 5
    ySD = 1
    n = 8 #每组生成的点数。
    # A集的xy期望中心是(3, 5), xy标准差都是1。
    d1Samples = genDistribution(xMean, xSD, yMean, ySD, n, 'A')
    plotSamples(d1Samples, 'k^')
    # B集的xy期望中心是(6, 5), xy标准差都是1。
    d2Samples = genDistribution(xMean+3,xSD,yMean, ySD, n, 'B')
    plotSamples(d2Samples, 'ko')
    # C集的xy期望中心是(3, 8), xy标准差都是1。
    d3Samples = genDistribution(xMean, xSD, yMean+3, ySD, n, 'C')
    plotSamples(d3Samples, 'kx')
    # 获得k-means结果
    clusters = trykmeans(d1Samples + d2Samples + d3Samples,
                         k, numTrials, verbose)
    # pylab.ylim(0,15)
    print('Final result has dissimilarity',
          round(dissimilarity(clusters), 3))
    for c in clusters:
        # print('', c) #为什么要加一个空字符串？为了空行吗？
        print(c)


def main():
    # random.seed(0)
    # contrivedTest(1, 2, True)
    # random.seed(0)
    # contrivedTest(50, 2, False)
    random.seed(10)
    contrivedTest2(40, 2)
    random.seed(10)
    contrivedTest2(40, 3)
    random.seed(10)
    contrivedTest2(40, 6)


if __name__ == '__main__':
    main()