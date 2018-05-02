import pylab


def findPayment(loan, r, m):
    """假设loan和r是浮点数，m是整数
       返回一个总额为loan，月利率为r，期限为m个月的抵押贷款的每月还款额"""
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))


class Mortgage(object):
    """建立不同种类抵押贷款的抽象类"""
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate/12.0 #月利率用年利率平均一下就可以。
        self.months = months
        self.paid = [0.0] #每月还款额，初始为零。
        self.outstanding = [loan] #剩余本金，初始为原始本金。
        self.payment = findPayment(loan, self.rate, months) #某个期间内每月固定还款额
        self.legend = None #还款方式的说明文字

    def makePayment(self):
        self.paid.append(self.payment)
        #当月还掉的本金 = 当月还款额 - 上月剩余本金*月利率
        reduction = self.payment - self.outstanding[-1]*self.rate
        #当月剩余本金 = 上月剩余本金 - 当月还掉的本金
        self.outstanding.append(self.outstanding[-1] - reduction)

    def getTotalPaid(self):
        #每月偿还额加总
        return sum(self.paid)

    def __str__(self):
        return self.legend

    #每个月的还款额，等额还款，基本是水平线
    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend) #第一个月是0，不必画出来，y轴不从0开始。

    #每个月看一眼待还本金，总是在减少，但是速度不同哦
    def plotBalance(self, style):
        pylab.plot(self.outstanding, style, label = self.legend)

    #截止到每个月的已经付给银行的总额
    def plotTotPd(self, style):
        totPd = [self.paid[0]] #用0月金额初始化
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i]) #上月结算额 + 本月新增额 = 本月结算额

        pylab.plot(totPd, style, label = self.legend)

    #本金当然要还，除去还本金，付的利息总额是净成本
    def plotNet(self, style):
        #算一遍每月累积总额totPd
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        #用outstanding待还本金数组的长度初始化equityAcquired
        equityAcquired = pylab.array([self.loan] * \
                         len(self.outstanding))
        #初始本金 - 待还本金 = 已还本金总额
        equityAcquired = equityAcquired - \
                         pylab.array(self.outstanding)
        #总净成本 = 已付总额 - 已还本金总额
        net = pylab.array(totPd) - equityAcquired

        pylab.plot(net, style, label = self.legend)


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%'

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend = 'Fixed, ' + str(r*100) + '%, '\
                   + str(pts) + ' points'

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12.0
        self.legend = str(teaserRate*100)\
                      + '% for ' + str(self.teaserMonths)\
                      + ' months, then ' + str(r*100) + '%'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1],
                                     self.rate,
                                     self.months - self.teaserMonths)
        Mortgage.makePayment(self)


def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                    varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    plotMortgages(morts, amt)


def plotMortgages(morts, amt):
    """建一个给图做标注的函数，顺便存档
    要求：
    morts是列表，集合各类还款方式；
    amt是数值，表示贷款额。
    输出：
    四张图，分别表示各种还款方式的每月信息：
    1 还款额；
    2 以付总额；
    3 待还本金；
    4 除去本金的净成本。"""
    def labelPlot(figure, title, xLabel, yLabel):
        pylab.figure(figure)
        pylab.title(title)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.legend(loc = 'best')
        pylab.savefig(title)

    #三种还款方式，各自有颜色、线型特征。
    styles = ['b-', 'g-.', 'r:']

    #给图编号赋名，方便理解和区分
    payments, cost, balance, netCost = 0, 1, 2, 3

    #在各种还款方式之间循环，三种方式分别画四张图，带自己的颜色、线型特征。
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(netCost)
        morts[i].plotNet(styles[i])
    #分别给四张图标注名称和X、Y坐标轴。
    labelPlot(payments, 'Monthly Payments of $' + str(amt) +
                ' Mortgages', 'Months', 'Monthly Payments')
    labelPlot(cost, 'Cash Outlay of $' + str(amt) +
              'Mortgages', 'Months', 'Total Payments')
    labelPlot(balance, 'Balance Remaining of $' + str(amt) +
              'Mortgages', 'Months', 'Remaining Loan Balance of $')
    labelPlot(netCost, 'Net Cost of $' + str(amt) + ' Mortgages',
              'Months', 'Payments - Equity $')
    pylab.show()


compareMortgages(amt=200000, years=30, fixedRate=0.07,
                 pts = 3.25, ptsRate=0.05,
                 varRate1=0.045, varRate2=0.095, varMonths=48)