import math, pylab


def createData(f, xVals):
    """假设f是一个单参数函数
                xVals是一个数组，其中的元素可以作为f的参数
       返回一个数组，其中的元素为将f应用于xVals中元素的结果。"""
    yVals = []
    for i in xVals:
        yVals.append(f(xVals[i]))
    return pylab.array(yVals)


def fitExpData(xVals, yVals):
    """假设xVals和yVals是两个数值型数组，满足yVals[i]=f(xVals(i))，这里的f是指数函数。
       返回a、b、base，使得log(f(x), base)==ax+b"""
    logVals = []
    for y in yVals:
        logVals.append(math.log(y, 2.0)) #求出以2为底的对数值
    fit = pylab.polyfit(xVals, logVals, 1)
    return fit, 2.0


xVals = range(10)
f = lambda x: 3**x
yVals = createData(f, xVals)
pylab.plot(xVals, yVals, 'ko', label = 'Actual values')
fit, base = fitExpData(xVals, yVals)
predictedYVals = []
for x in xVals:
    predictedYVals.append(base**pylab.polyval(fit, x))
pylab.plot(xVals, predictedYVals, label = 'Predicted values')
pylab.title('Fitting an Exponential Function')
pylab.legend(loc = 'upper left')
#预测一个不在初始数据中的x值
print('f(20) =', f(20))
print('Predicted value =', int(base**(pylab.polyval(fit, [20]))))

pylab.show()