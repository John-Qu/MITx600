import pylab


def getTrajectoryData(fileName):
    """
    从弹道数据文件中提取位置与高度，并做格式转换，不做计算。
    :param fileName: string，弹道数据文件名。
    :return: 距离，[高度1 2 3 4]数据列表
    """
    dataFile = open(fileName, 'r')
    distances = []
    heights1, heights2, heights3, heights4 = [],[],[],[]
    dataFile.readline() # 跨过标题行
    for line in dataFile:
        d, h1, h2, h3, h4 = line.split() # tuple对应list赋值
        # str转float后，推入列表
        distances.append(float(d))
        heights1.append(float(h1))
        heights2.append(float(h2))
        heights3.append(float(h3))
        heights4.append(float(h4))
    dataFile.close()
    return (distances, [heights1, heights2, heights3, heights4])


def rSquared(measured, predicted):
    """ 计算线性回归模型的R2可决系数。
    假设measured为表示测量值的一维数组
        predicted为表示预测值的一维数组
    返回可决系数"""
    # 用数组，语句简洁。
    # 计算预测值与测量值差方和
    estimateError = ((predicted - measured)**2).sum()
    # 计算原始数据方差。这个值是很大，貌似是给均方误差一个上界。
    meanOfMeasured = measured.sum()/len(measured)
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimateError/variability


def getHorizontalSpeed(quadFit, minX, maxX):
    """计算弹丸落地时的水平速度，打印输出。
    假设quadFit是二次多项式的系数
        minX和maxX是用英寸表示的距离，抛物线与x轴的两个交点的坐标。
       返回以英尺/秒表示的水平速度"""
    inchesPerFoot = 12
    xMid = (maxX - minX)/2
    a,b,c = quadFit[0], quadFit[1], quadFit[2]
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*inchesPerFoot #accel. of gravity in inches/sec/sec
    t = (2*yPeak/g)**0.5 #从最高点到目标高度所需时间，单位为秒
    print('Horizontal speed =',
          int(xMid/(t*inchesPerFoot)), 'feet/sec')


def processTrajectories(fileName):
    """
    处理弹道数据，输出图形。
    :param fileName:
    :return: None，显示图形，用一次和二次多项式拟合弹道轨迹。
    """
    distances, heights = getTrajectoryData(fileName)
    numTrials = len(heights)
    distances = pylab.array(distances)
    #生成一个数组，用于存储每个距离的高度，并计算平均值
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    meanHeights = totHeights/len(heights)
    # 绘图
    title = 'Trajectory of Projectile (Mean of ' + str(numTrials) + ' Trials)'
    pylab.figure(title)
    pylab.title(title)
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    pylab.plot(distances, meanHeights, 'ko')
    fit = pylab.polyfit(distances, meanHeights, 1)
    altitudes = pylab.polyval(fit, distances)
    pylab.plot(distances, altitudes, 'b', label = 'Linear Fit')
    print('RSquare of linear fit =', rSquared(meanHeights, altitudes))
    fit = pylab.polyfit(distances, meanHeights, 2)
    # 用实验数据对应的点位distances来绘图，导致点少的区域上，曲线不够平滑。
    altitudes = pylab.polyval(fit, distances)
    pylab.plot(distances, altitudes, 'k:', label = 'Quadratic Fit')
    print('RSquare of quadratic fit =', rSquared(meanHeights, altitudes))
    pylab.legend()
    # 计算落地时的水平速度，打印输出。
    getHorizontalSpeed(fit, distances[-1], distances[0])


processTrajectories('launcherData.txt')
pylab.show()