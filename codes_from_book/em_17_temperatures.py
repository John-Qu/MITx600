# -*- coding: utf-8 -*-
"""
借用edX上的数据，做书上的套路。

2018-05-11 12:42:08 by John Qu
"""

import random, pylab, numpy
from em_15_3_flip import stdDev, variance

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


def makeHist(data, title, xlabel, ylabel, bins = 20):
    pylab.figure(title)
    pylab.hist(data, bins = bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    mean = sum(data)/len(data)
    std = stdDev(data)
    pylab.annotate('Mean = ' + str(round(mean, 2)) + \
                   '\nSD = ' + str(round(std, 2)), fontsize = 20,
                   xy = (0.1, 0.75), xycoords = 'axes fraction')

def getHighs():
    inFile = open('temperatures.csv')
    population = []
    for l in inFile:
        try:
            tempC = float(l.split(',')[1])
            population.append(tempC)
        except:
            continue
    inFile.close()
    return population


population = getHighs()
# makeHist(population, 'Daily High 1961-2015, Population of '+str(len(population)), 'Degrees C', 'Number Days')

sample = random.sample(population, 40)
# makeHist(sample, 'Daily High 1961-2015, Sample of '+str(len(sample)), 'Degrees C', 'Number Days')


def mean_std_of_means(population, sample_sizes = range(50, 2000, 200), num_sample = 20):
    """
    以不同样本大小从总体中随机提取20个样本，计算样本均值的均值和标注差
    :param population: list，总体数据
    :param sample_sizes: list类，样本大小的列表，默认range(50, 2000, 200)
    :param num_sample: int, 样本数量，默认20
    :return: 两个列表，不同样本大小对应的 样本均值的均值和方差
    """
    meanOfMeans, stdOfMeans = [], []
    for sampleSize in sample_sizes:
        sampleMeans = []
        for t in range(num_sample):
            sample = random.sample(population, sampleSize)
            sampleMeans.append(sum(sample)/sampleSize)
        meanOfMeans.append(sum(sampleMeans)/len(sampleMeans))
        stdOfMeans.append(stdDev(sampleMeans))
    return meanOfMeans, stdOfMeans


def sampling_errobar(population, sample_sizes = range(50, 2000, 200), num_sample = 20):
    """
    绘制总体中提取不同大小样本的误差条。
    :param population: list，总体数据
    :param sample_sizes: list类，样本大小的列表
    :return: 一个图表。
    """
    meanOfMeans, stdOfMeans = mean_std_of_means(population, sample_sizes, num_sample)
    pylab.figure('Estimates of Mean Temperature')
    pylab.errorbar(sample_sizes, meanOfMeans,
               yerr = 1.96*pylab.array(stdOfMeans),
               label = 'Estimated mean and 95% confidence interval')
    pylab.xlim(0, max(sample_sizes) + 50)
    pylab.axhline(sum(population)/len(population), linestyle = '--',
              label = 'Population mean')
    pylab.title('Estimates of Mean Temperature')
    pylab.xlabel('Sample Size')
    pylab.ylabel('Mean Temperature(Degrees C)')
    pylab.legend(loc = 'best')

# sampling_errobar(population, range(50, 2000, 200), 20)

# random.seed(0)
# population = getHighs()
# sample = random.sample(population, 100)
# getMeansAndSDs(population, sample, True)


def standard_error(population, sample_sizes = range(50, 2000, 200), num_sample = 20):
    """
    绘图说明"多个样本均值的标准差 收敛于 样本的标准误差"
    :param population: list，总体数据
    :param sample_sizes: list类，样本大小的列表
    :return: 一个图表。
    """
    stdOfMeans = mean_std_of_means(population, sample_sizes, num_sample)[1]
    population_deviation = stdDev(population)
    sem = population_deviation / pylab.array(sample_sizes)**0.5
    pylab.figure('SE vs. SD of ' + str(num_sample) + ' Means')
    pylab.plot()
    pylab.plot(sample_sizes, stdOfMeans, label = 'Standard Deviation of ' + str(num_sample) + ' Means')
    pylab.plot(sample_sizes, sem, label = 'Standard Error of the Mean')
    pylab.xlim(0, max(sample_sizes) + 50)
    pylab.title('SE vs. SD of ' + str(num_sample) + ' Means')
    pylab.xlabel('Sample Size')
    pylab.ylabel('Standard Deviation')
    pylab.legend(loc = 'best')

# standard_error(population, range(50, 2000, 200), 20)
# standard_error(population, range(50, 2000, 200), 200)


def sd_of_sample_vs_population(population, sample_sizes = range(50, 2000, 200), num_sample = 20):
    """
    绘图说明"样本标注差与整体标准差的差值随着样本大小增加而变小",
    可以用足够大的样本的标准差代替整体标注差。
    :param population: list，总体数据
    :param sample_sizes: list类，样本大小的列表
    :param num_sample: int, 样本数量
    :return: 一个图表。
    """
    population_deviation = stdDev(population)
    diffsMeans = []
    for sampleSize in sample_sizes:
        diffs = []
        for t in range(100):
            diffs.append(abs(population_deviation - stdDev(random.sample(population, sampleSize))))
        diffsMeans.append(sum(diffs) / len(diffs))
    pylab.figure('Sample SD vs Population SD with ' + str(num_sample) + ' Samples')
    pylab.plot(sample_sizes, diffsMeans)
    pylab.xlabel('Sample Size')
    pylab.ylabel('Abs(Pop. Std - Sample Std)')
    pylab.title('Sample SD vs Population SD with ' + str(num_sample) + ' Samples')

# sd_of_sample_vs_population(population, range(2, 200, 2), 100)

# pylab.show()

def check_sampling_error(population, sampleSize, numTrail):
    """
    验证用样本标准差估计标准误差的可靠性，看看是否能够达到期望的置信水平。
    :param population: list，总体数据
    :param sampleSize: int, 样本大小
    :return:
    """
    popMean = sum(population)/len(population)
    numGood = 0
    for t in range(numTrail):
        sample = random.sample(population, sampleSize)
        sampleMean = sum(sample)/sampleSize
        se = stdDev(sample)/sampleSize**0.5
        # 比较的是该样本均值落在真的均值1.96个标准差之内的概率
        if abs(popMean - sampleMean) <= 1.96*se:
            numGood += 1
    # 输出检查是否满足95%的置信水平
    print('Fraction inside 95% confidence interval =', numGood/10000)


# check_sampling_error(population, 200, 10000)
