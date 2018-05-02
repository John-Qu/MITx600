class Location(object):
    def __init__(self, x, y):
        """x和y为数值型，可以做加减乘除"""
        #成对的变量，用tuple格式做赋值。
        self.x, self.y = x, y

    def move(self, deltaX, deltaY):
        """deltaX和deltaY为数值型，可以是浮点数。
        返回的是另一个Location"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        """other是另一个Location"""
        ox, oy = other.x, other.y
        xDist, yDist = self.x - ox, self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):
    """场地的本质是关系：谁在哪里，怎么活动。
    数据属性：
    drunks字典，将Drunk者映射到他的Location。
    方法属性：
    addDrunk, 添加Drunk者.
    moveDrunk, 让drunk者用他的方式走到新的Location，更新字典。
    getLoc, 从字典中提取drunk者的当前位置。"""
    def __init__(self):
        """初始化Field不需要参数。
        返回一个字典drunks，绑定Drunk者和他的Location位置。
        注意不只一位drunk者，location也可以重合。"""
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        """只有drunk一个参数。其中移动的步长和方向，是某类drunk的数据属性"""
        #调用Drunk子类中的takeStep方法，让他以自己的方式给出移动向量。
        #调用Location类中的move方法，从原位置经移动向量变为新位置。
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        #某Drunk子类中，定义着对应的takeStep方法，返回的是tuple格式的向量坐标。
        xDist, yDist = drunk.takeStep()
        #从drunks字典中提取drunk者的当前位置。
        currentLocation = self.drunks[drunk]
        #使用Location的move方法获得一个新位置，更新drunks字典中drunk者的位置。
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random, pylab, math

class Drunk(object):
    def __init__(self, name = None):
        """假设name是字符串
        返回一个只有名字的drunk者"""
        self.name = name

    def __str__(self):
        """匿名者？没有初始化过的drunk者? 怎么用？"""
        #是不是 self.name != None ?
        if self != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    """drunk者的特征是步态，就是定义如何takeStep。
    正常的drunk向各个方向迈一步的概率一致，步长相同。
    返回的是一个向量的坐标元组。"""
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    """假设f是一个Field对象，d是f中的一个Drunk对象，numSteps是正整数。
       将d移动numSteps次；返回这次游走最终位置与开始位置之间的距离"""
    #记住d的初始位置。
    start = f.getLoc(d)
    #请d按照他自己的步伐走numSteps步。
    for s in range(numSteps):
        f.moveDrunk(d)
    #返回初始位置到终止位置的距离。
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """模拟dClass者的numTrials次游走，每次游走numSteps步。
    假设：
    numSteps是非负整数，
    numTrials是正整数，
    dClass是Drunk的某一个子类。
    返回：
    一个列表，表示每次模拟的最终距离"""
    #注意dClass是形式参数，实际参数可能是UsualDrunk, ColdDrunk, EWDrunk.
    Homer = dClass() #dClass是Drunk的子类，没有给name实际参数，默认name = None。
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        #distances.append(round(walk(f, Homer, numTrials), 1))
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    """假设walkLengths是非负整数序列
         numTrials是正整数，dClass是Drunk的一个子类
       对于walkLengths中的每个步数，运行numTrials次simWalks函数，并输出结果"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))


class ColdDrunk(Drunk):
    """这位醉鬼向四个方向的概率都是一样的，但是如果是迈向南方，步子就大一倍。"""
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-2.0), (1.0, 0.0),\
                       (-1.0, 0.0)]
        return random.choice(stepChoices)


class EWDrunk(Drunk):
    """这是个只向东西两侧走的醉鬼。"""
    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def simAll(drunkKinds, walkLengths, numTrials):
    """把各种醉鬼drunkKinds的情况都模拟出来，请他们各自通过drunkTest打印输出平均距离和最大最小距离.
    要求：
    drunkKinds是元组或列表，元素Drunk的几个子类。
    walklengths是元组或列表，走多少步的各种情况。
    numTrials是正整数，表示尝试多少次，以便算取平均值和最大最小值。
    返回：
    None。动作和输出都在drunkTest里实现。
    """
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)

#模拟三种醉鬼在两种步长情况下的移动距离，打印结果。
simAll((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)


class styleIterator(object):
    """为打印样式不重样，专门建了一个类。"""
    def __init__(self, styles):
        """styles是打印样式的字符串的元组。"""
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        """返回当前index指向的styles元组中的字符串，
        同时将index向后移动一格，如果到底就从头再来。"""
        result = self.styles[self.index]
        #如果到底，就从头再来。
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def simDrunk(numTrials, dClass, walkLengths):
    """为了绘图，计算不同步数对应的出走平均距离。
    要求：
    numTrails是正整数；
    dClass是Drunk的某一个子类；
    walkLengths是各种步数情况的元组。
    返回：
    一个列表，表示与各种步长一一对应的出走平均距离。"""
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances


class oddField(Field):
    """这是一个特别场地，它有虫洞。"""
    def __init__(self, numHoles, xRange, yRange):
        """初始化虫洞特别场地。
        要求：
        numHoles是正整数值，表示场地内虫洞的数量。
        xRange和yRange都是正数值，正负xy和起来表示场地的范围。
        建立：
        drunks字典, 继承Field类，将drunk者映射到他们各自的位置。
        wormholes字典，将位置(x, y)的虫洞映射到新位置上Location(newX, newY)"""
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            #在范围内随机找一个点。
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            #在范围内随机找另一个点。
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            #把另一个点的数据集成入一个Location抽象类。
            newLoc = Location(newX, newY)
            #注意字典的键是(x, y)元组，键值是Location类。
            self.wormholes[(x, y)] = newLoc

    def moveDrunk(self, drunk):
        """请drunk者移动一步，如果他踩到了虫洞，那就他的位置更新为虫洞彼岸的位置。"""
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]


def simAll1(drunkKinds, walkLengths, numTrials):
    """模拟各种醉鬼的情况, 绘图输出在各种步数情况下的平均出走距离。
    相比于simAll，不是分别打印，而是分别绘图。
    要求：
    drunkKinds是元组或列表，元素Drunk的几个子类。
    walklengths是元组或列表，走多少步的各种情况。
    numTrials是正整数，表示尝试多少次，以便算取平均值和最大最小值。
    返回：
    一张图表, 各种醉鬼各种步数的平均移动距离.png"""
    styleChoice = styleIterator(('m-', 'r:', 'k-.'))
    #循环样式，分别绘图。
    pylab.figure('simAll1')
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        #调用为了绘图的simDrunk，返回的是数组。
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle,
                   label = dClass.__name__)
    #下面这几句是绘制正常的醉汉步数与距离的规律用的。
    #curStyle = styleChoice.nextStyle()
    #refs = [math.sqrt(x) for x in walkLengths]
    #pylab.plot(walkLengths, refs, curStyle,
               label = 'Square root of steps')
    #给这张图整体做装饰。
    pylab.title('Mean Distance from Origin ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
    #坐标轴调整为对数标度
    pylab.semilogx()
    pylab.semilogy()
    pylab.savefig("各种醉鬼各种步数的平均移动距离")


#模拟三种醉鬼在各种步长情况下的平均距离，绘图输出。
simAll1((UsualDrunk, ColdDrunk, EWDrunk),
       (10,100,1000,10000), 100)

#下面这句是绘制正常的醉汉步数与距离的规律用的。
#simAll1((UsualDrunk,), (10,100,1000,10000,100000), 100)


def getFinalLocs(numSteps, numTrials, dClass):
    """模拟某类醉鬼从原点出发多次游走的停止位置。
    要求：
    numSteps，正整数，步数。
    numTrials，正整数，尝试次数。
    dClass，Drunk的某个子类，醉鬼的特征。
    返回：
    locs，列表，numTrials次游走的最终位置。"""
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0, 0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs


def plotLocs(drunkKinds, numSteps, numTrials):
    """绘制各种醉鬼走相同步数后的各种最终位置图。
    要求：
    drunkKinds是元组或列表，元素Drunk的几个子类。
    numSteps是正整数，表示步数。
    numTrials是正整数，表示尝试多少次，以便看到最终位置的分布趋势。
    返回：
    一张图表, 各种醉鬼走相同步数后的多次最终位置.png。
    """
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    #循环各中醉鬼的情况。
    pylab.figure("plotLocs")
    for dClass in drunkKinds:
        #模拟出这种醉鬼多次尝试的最终位置。
        locs = getFinalLocs(numSteps, numTrials, dClass)
        #将Locations的信息拆出来
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        #算取平均位置
        meanX = sum(xVals)/len(xVals)
        meanY = sum(yVals)/len(yVals)
        #绘图并标注
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                      label = dClass.__name__ + ' mean loc. = <'
                      + str(meanX) + ', ' + str(meanY) + '>')
    #整体修饰图表
    pylab.title('Location at End of Walks ('
                + str(numSteps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'lower left')
    pylab.savefig("各种醉鬼走相同步数后的多次最终位置")


#描绘最终位置图表，三种醉鬼，走100步，尝试200次。
plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)


def traceWalk(drunkKinds, numSteps):
    """绘制各种醉鬼一次漫步的轨迹。
    要求：
    drunkKinds是元组或列表，元素Drunk的几个子类。
    numSteps是正整数，表示步数。
    返回：
    一张图表。
    """
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    #f = Field()
    #替换为有1000个虫洞的场地，场地内有正负100*正负200，共80000个点。虫洞占比1/80。
    f = oddField(1000, 100, 200)
    pylab.figure("traceWalk")
    for dClass in drunkKinds:
        d = dClass()
        f.addDrunk(d, Location(0, 0))
        #把每一步的位置存入locs列表。
        locs = []
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        #拆分出xy信息。
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        #各种醉鬼分别绘图
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                  label = dClass.__name__)
    #整体修饰标注
    pylab.title('Spots Visited on Walk ('
                + str(numSteps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'best')
    pylab.savefig("各种醉鬼一次漫步的轨迹")


#绘制三种醉鬼各走200步的轨迹图表。
traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 500)


