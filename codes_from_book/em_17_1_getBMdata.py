# -*- coding: utf-8 -*-
import pylab

def getBMData(filename):
    """读取给定文件内容。假设文件是逗号分隔的形式，每个条目中有6个元素：
    0. 姓名（字符串），1. 性别（字符串），2. 年龄（整数），3. 分组（整数），
    4. 国家（字符串），5. 整体时间（浮点数）
    返回一个字典，包含分别由6个变量组成的列表。"""

    data = {}
    f = open(filename)
    line = f.readline()
    data['name'], data['gender'], data['age'] = [], [], []
    data['division'], data['country'], data['time'] = [], [], []
    while line != '':
        split = line.split(',')
        data['name'].append(split[0])
        data['gender'].append(split[1])
        data['age'].append(int(split[2]))
        data['division'].append(int(split[3]))
        data['country'].append(split[4])
        data['time'].append(float(split[5][:-1])) #remove \n
        line = f.readline()
    f.close()
    return data

def makeHist(data, bins, title, xLabel, yLabel):
    pylab.hist(data, bins)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    mean = sum(data)/len(data)
    std = stdDev(data)
    pylab.annotate('Mean = ' + str(round(mean, 2)) +\
              '\nSD = ' + str(round(std, 2)), fontsize = 20,
              xy = (0.65, 0.75), xycoords = 'axes fraction')

times = getBMData('bm_results2012.txt')['time']
makeHist(times, 20, '2012 Boston Marathon',
            'Minutes to Complete Race', 'Number of Runners')