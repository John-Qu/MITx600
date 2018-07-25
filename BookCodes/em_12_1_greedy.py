class Item(object):
    """将财物建立抽象概念，初始化它的三个属性，可以分别提取；同时定义打印输出的框架"""

    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
                 + ', ' + str(self.weight) + '>'
        return result


def value(item):
    """将item tpye的object映射为它的value值"""
    return item.getValue()


def weightInverse(item):
    """将item tpye的object映射为它的weight值的倒数"""
    return 1.0/item.getWeight()


def density(item):
    """将item tpye的object映射为它的value/weight值"""
    return item.getValue()/item.getWeight()


#greedy函数是greedy算法的核心
def greedy(items, maxWeight, keyFunction):
    """假设Items是列表，maxWeight >= 0
       keyFunctions是上面定义的三个函数之一，将item type映射到它的某个可衡量的data attribute"""
    itemsCopy = sorted(items, key=keyFunction, reverse = True) #这里用"什么是值得"把财物做了排序，最坏情况O(n*log(n))
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight: #看看还能不能再拿一个？
            result.append(itemsCopy[i]) #再装一个
            totalWeight += itemsCopy[i].getWeight() #更新总重
            totalValue += itemsCopy[i].getValue() #更新总额
    return (result, totalValue)


def buildItems():
    """初始化类实例，批量初始化后没有分别绑定一个变量名，而是顺手加入了一个列表，给这个列表一个变量名。"""
    names = ['clock','painting','radio','vase','book','computer']
    values = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items


def testGreedy(items, maxWeight, keyFunction):
    """计算与打印一种结果"""
    taken, val = greedy(items, maxWeight, keyFunction)
    print('Total value of items taken is', val)
    for item in taken:
        print(' ', item)


def testGreedys(maxWeight = 20):
    """在统一约束下，比较三种方式"""
    items = buildItems()

    print('Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)

    print('\nUse greedy by weight to fill knapsack of size',
          maxWeight)
    testGreedy(items, maxWeight, weightInverse)

    print('\nUse greedy by density to fill knapsack of size',
          maxWeight)
    testGreedy(items, maxWeight, density)


#testGreedys()