# -*- coding: utf-8 -*-
# 通过牙齿形态和体重，区分哺乳动物的食性。


import pylab, random, em_23_1_cluster, em_23_2_k_means_clustering, em_15_3_flip


def zScaleFeatures(vals):
    """
    将列表数据做标准正态分布（Z分布）归一化处理
    :param vals: 浮点数列表/数组
    :return: z分布归一化后的浮点数数组
    """
    result = pylab.array(vals)
    mean = sum(result)/len(result)
    result = result - mean
    return result/em_15_3_flip.stdDev(result)


def iScaleFeatures(vals):
    """
    将列表数据线性映射到[0, 1]区间做归一化处理
    :param vals: 浮点数列表/数组
    :return: [0,1]区间内的浮点数数组
    """
    minVal, maxVal = min(vals), max(vals)
    # 用头尾两个点，找一阶线性回归模型
    fit = pylab.polyfit([minVal, maxVal], [0, 1], 1)
    # 返回输入数组对应的模型上的输出数据
    return pylab.polyval(fit, vals)


def readMammalData(fName, scale):
    """
    从源文件中读取哺乳动物信息，打包输出。
    :str fName: 原始信息文件名
    :param scale: 函数，归一化每一种特征向量
    :return: 特征向量列表，标签列表，物种名称列表
    """
    dataFile = open(fName, 'r')
    numFeatures = 0
    #处理文件开头的那些行
    for line in dataFile: #找出特征数量
        if line[0:3] ==  '#标签': #表示特征行结束
            break
        if line[0:3] != '#名称': #看原始数据，只要不是"名称"那一行，就对应着一种特征
            numFeatures += 1

    #生成featureVals、speciesName和labelList
    featureVals, speciesNames, labelList = [], [], []
    # featureVals是各种特征列表的列表，长度是特征的数量
    for i in range(numFeatures):
        featureVals.append([])

    #继续处理文件中的行，从注释后面开始
    for line in dataFile:
        #去掉换行符，然后对行进行拆分
        dataLine = line[:-1].split(',')
        #物种名，加入列表。
        speciesNames.append(dataLine[0])
        #已有分类标签，加入列表。
        classLabel = dataLine[-1]
        labelList.append(classLabel)
        #为每一个物种，建立纵向的特征列表（注意不是某个物种的横向特征向量），加入特征列表。
        for i in range(numFeatures):
            featureVals[i].append(float(dataLine[i+1]))

    #使用featureVals建立包含每个哺乳动物特征向量的列表
    # 对于每个哺乳动物，按照设定的缩放方式对特征进行缩放
    for i in range(numFeatures):
        # 纵向的相同特征，统一刷一遍。
        featureVals[i] = scale(featureVals[i])
    featureVectorList = []
    # 从纵向的相同特征列表的列表，构建出横向的特征向量的列表
    for mammal in range(len(speciesNames)):
        # 构建某个物种的特征向量
        featureVector = []
        for feature in range(numFeatures):
            featureVector.append(featureVals[feature][mammal])
        # 加入特征向量的列表
        featureVectorList.append(featureVector)
    return featureVectorList, labelList, speciesNames


    #for each mammal
    # featureVectorList = []
    # for mammal in range(len(speciesNames)):
    #     featureVector = []
    #     for feature in range(numFeatures):
    #         featureVector.append(featureVals[feature][mammal])
    #     featureVectorList.append(featureVector)
    # return featureVectorList, labelList, speciesNames

def buildMammalExamples(featureList, labelList, speciesNames):
    examples = []
    for i in range(len(speciesNames)):
        features = pylab.array(featureList[i])
        example = em_23_1_cluster.Example(speciesNames[i], features, labelList[i])
        examples.append(example)
    return examples


def testTeeth(numClusters, numTrials, scale = lambda x: x):
    """
    读数据，做运算
    :param numClusters: 分成几个簇
    :param numTrials: k-means相似聚簇做几次尝试
    :param scale: 缩放函数，默认identity function不做处理
    :return: 打印结果
    """
    # 提取信息
    features, labels, species =\
              readMammalData('dentalFormulas.txt', scale)
    # 创建实例
    examples = buildMammalExamples(features, labels, species)
    # k-means相似聚簇
    bestClustering = em_23_2_k_means_clustering.trykmeans(examples, numClusters, numTrials)
    # 打印输出结果
    for c in bestClustering:
        # 为每一个簇打印内部对象
        names = ''
        for p in c.members():
            names += p.getName() + ', '
        print('\n' + names[:-2]) #除去末尾的逗号和空格
        # 检验同一个簇中的实例是否真的是同类
        herbivores, carnivores, omnivores = 0, 0, 0
        for p in c.members():
            if p.getLabel() == '0':
                herbivores += 1
            elif p.getLabel() == '1':
                carnivores += 1
            else:
                omnivores += 1
        print(herbivores, 'herbivores,', carnivores, 'carnivores,',
          omnivores, 'omnivores')



def main():
    random.seed(0)
    print('Clustering without scaling')
    testTeeth(3, 40)
    random.seed(0)
    print('\nClustering with z-scaling')
    testTeeth(3, 40, zScaleFeatures)
    random.seed(0)
    print('\nClustering with i-scaling')
    testTeeth(3, 40, iScaleFeatures)
    

if __name__ == "__main__":
    main()