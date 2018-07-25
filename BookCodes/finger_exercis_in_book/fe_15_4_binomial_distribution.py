import pylab


def two3():
    """实际练习：实现一个函数，计算扔k次骰子时正好扔出两个3的概率，
    并绘制出k从2~100时的概率变化。
    :k int, rolls of a fair die"""
    vals = []
    for k in range(2, 100):
        val = k * 1/36 * (35/36)**(k-1)
        vals.append(val)
    pylab.plot(vals)
    pylab.title("The probability of rolling exactly two 3's in k rolls")
    pylab.xlabel("times of rolls")
    pylab.ylabel("Probability of exactly two 3's")

two3()
pylab.show()