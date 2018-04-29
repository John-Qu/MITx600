from em_12_1_greedy import Item
import random

def maxVal(toConsider, avail):
    """假设toConsider是一个物品列表list，avail表示背包还能再装的重量值。
       返回一个元组表示0/1背包问题的解，包括物品总价值和带走的物品元组。"""

    #典型二叉树判断：是否有子节点，如果有，是只有一个，还是两个？
    if toConsider == [] or avail == 0:
        #这是叶节点，是base case，它的解就是（0，空），返回。
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #如果如此，只能探索右侧分支，右侧分支的值作为返回值。
        result = maxVal(toConsider[1:], avail)
    else:
        #如果下一个物品可以装进去，两个分支都需要探索。
        nextItem = toConsider[0]

        #左侧分支的两个值写成
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getWeight())
        withVal += nextItem.getValue()

        #右侧分支写成
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        #选择更好（物品总价更大）的分支的值，作为函数返回值。
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def smallTest():
    #4个物品，二叉树叶节点最多16个。
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    #建立物品类
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    #求出最优解，背包最大重量是5。
    val, taken = maxVal(Items, 5)
    #打印结果
    for item in taken:
        print(item)
    print('Total value of items taken =', val)

def buildManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxWeight)))
    return items

def bigTest(numItems):
    items = buildManyItems(numItems, 10, 10)
    val, taken = maxVal(items, 40)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


def fastMaxVal(toConsider, avail, memo = {}):
    """假设toConsider是物品列表，avail表示重量
         memo进行递归调用
       返回一个元组表示0/1背包问题的解，包括物品总价值和物品列表"""

    #为什么toConsider列表的长度竟然就有代表性？
    #因为决策树上相同的层级有一样的待选列表，长度也一样，不同层级之间长度不同。
    #待选列表总是从一个方向剔除元素，所以其长度就成了它精简的代表。
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #探索右侧分支
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #探索左侧分支
        withVal, withToTake =\
                 fastMaxVal(toConsider[1:],
                            avail - nextItem.getWeight(), memo)
        withVal += nextItem.getValue()
        #探索右侧分支
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #选择更好的分支
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result


#smallTest()

bigTest(40)