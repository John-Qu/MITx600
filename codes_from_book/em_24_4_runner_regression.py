# -*- coding: utf-8 -*-
# 没有找到波士顿马拉松成绩单文件，代码没有在本机运行。

#建立男性和女性的训练集
ageM, ageW, timeM, timeW = [], [], [], []
for e in training:
    if e.getLabel() == 'M':
       ageM.append(e.getAge())
       timeM.append(e.getTime())
    else:
       ageW.append(e.getAge())
       timeW.append(e.getTime())
#通过下采样使图形更加美观易读
ages, times = [], []
for i in random.sample(range(len(ageM)), 300):
     ages.append(ageM[i])
     times.append(timeM[i])
#生成样本的散点图
pylab.plot(ages, times, 'yo', markersize = 6, label = 'Men')
ages, times = [], []
for i in random.sample(range(len(ageW)), 300):
    ages.append(ageW[i])
    times.append(timeW[i])
pylab.plot(ages, times, 'k^', markersize = 6, label = 'Women')
#学习两个一阶线性回归模型
mModel = pylab.polyfit(ageM, timeM, 1)
fModel = pylab.polyfit(ageW, timeW, 1)
#绘制出对应于模型的直线
xmin, xmax = 15, 85
pylab.plot((xmin, xmax), (pylab.polyval(mModel,(xmin, xmax))),
           'k', label = 'Men')
pylab.plot((xmin, xmax), (pylab.polyval(fModel,(xmin, xmax))),
           'k--', label = 'Women')
pylab.title('Linear Regression Models')
pylab.xlabel('Age')
pylab.ylabel('Finishing time (minutes)')
pylab.legend()


truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
for e in testSet:
    age = e.getAge()
    time = e.getTime()
    #判断更接近男性模型 
    if abs(time - pylab.polyval(mModel,age)) <\
       abs(time - pylab.polyval(fModel, age)):
        if e.getLabel() == 'M':
            truePos += 1
        else:
            falsePos += 1
    else:
        if e.getLabel() == 'F':
            trueNeg += 1
        else:
            falseNeg += 1
getStats(truePos, falsePos, trueNeg, falseNeg)