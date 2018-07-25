import pylab


def clear(n, p, steps):
    """假设n和steps都是正整数，p是个浮点数
         n：分子的初始数量
         p：一个分子被清除的概率
         steps：模拟的时间长度"""
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.semilogy()
    pylab.title('Clearance of Drug')


clear(1000, 0.01, 1000)
pylab.show()