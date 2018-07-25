import random, pylab

def successfulStarts(successProb, numTrials):
    """假设successProb是一个浮点数，表示单次尝试成功的概率。numTrials是个正整数。
       返回一个列表，其中的元素是每次实验成功之前的尝试次数。"""
    triesBeforeSuccess = []
    for t in range(numTrials):
        consecFailures = 0
        # 随机数大于成功的概率，就是失败。
        # 直到成功，才退出while循环。
        while random.random() > successProb:
            consecFailures += 1
        # 将循环的次数作为失败次数添加进列表。
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

probOfSuccess = 0.5
numTrials = 5000
distribution = successfulStarts(probOfSuccess, numTrials)
# 直方图，横轴是成功之前的失败次数，纵轴是在集合中出现的个数。
pylab.hist(distribution, bins = 14)
pylab.xlabel('Tries Before Success')
pylab.ylabel('Number of Occurrences Out of ' + str(numTrials))
pylab.title('Probability of Starting Each Try = '\
            + str(probOfSuccess))
pylab.show()