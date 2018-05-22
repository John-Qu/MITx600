import numpy
import matplotlib.pyplot as plt

def minkowskiDist(v1, v2, p):
    """假设v1和v2是两个等长的数值型数组
       返回v1和v2之间阶为p的闵可夫斯基距离"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)


class Animal(object):
    def __init__(self, name, features):
        """假设name是字符串；features是数值型列表"""
        self.name = name
        self.features = numpy.array(features) #列表已经转换为数组

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self, other):
        """假设other是Animal类型的对象
           返回self与other的特征向量之间的欧氏距离"""
        return minkowskiDist(self.getFeatures(),
                             other.getFeatures(), 2)


def compareAnimals(animals, precision):
    """假设animals是动物列表，precision是非负整数
       建立一个表格，表示每种动物之间的欧氏距离"""
    #获取行标签和列标签
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    #计算动物之间的距离
    #对每一行
    for a1 in animals:
        row = []
        #对每一列
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    #生成表格
    table = plt.table(rowLabels = rowLabels,
                        colLabels = columnLabels,
                        cellText = tableVals,
                        cellLoc = 'center',
                        loc = 'center',
                        colWidths = [0.2]*len(animals))
    table.scale(1, 2.5)

    plt.savefig('distances')


def main():
    rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
    boa = Animal('boa\nconstrictor', [0,1,0,1,0])
    # dartFrog = Animal('dart frog', [1,0,1,0,4]) # 不应给legs更大的权重
    dartFrog = Animal('dart frog', [1,0,1,0,1])
    # animals = [rattlesnake, boa, dartFrog]
    
    # alligator = Animal('alligator', [1,1,0,1,4]) # 不应给legs更大的权重
    alligator = Animal('alligator', [1,1,0,1,1])
    
    # 把其他几种动物补全
    cobra = Animal('cobra', [1,1,1,1,0])
    salmon = Animal('salmon', [1,1,0,1,0])
    python = Animal('python', [1,1,0,1,0])
    animals = [cobra, rattlesnake, boa, alligator, dartFrog, salmon, python]
    
    compareAnimals(animals, 3)
    plt.show()
    
    
if __name__ == "__main__":
    main()

