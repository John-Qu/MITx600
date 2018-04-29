from em_9_3_6_gempowerset import genPowerset, getBinaryRep

from em_12_1_greedy import *

def chooseBest(pset, maxWeight, getVal, getWeight):
    #计算复杂度是n*2^n, n = len(items)
    bestVal = 0.0
    bestSet = None
    for items in pset: #pset的长度是2**len(items)
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items: #最长len(items)
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
           bestVal = itemsVal
           bestSet = items
    return (bestSet, bestVal)

def testBest(maxWeight = 20):
    items = buildItems()
    pset = genPowerset(items) #pset的长度是2**len(items), 计算复杂度是O(2**len(items))
    taken, val = chooseBest(pset, maxWeight, Item.getValue,
                            Item.getWeight)#计算复杂度是n*2^n, n = len(items)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)

testBest()
