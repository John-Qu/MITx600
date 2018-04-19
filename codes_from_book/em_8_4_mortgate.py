def findPayment(loan, r, m):
    """假设loan和r是浮点数，m是整数
       返回一个总额为loan，月利率为r，期限为m个月的抵押贷款的每月还款额"""
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))


class Mortgage(object):
    """用来建立不同种类抵押贷款的抽象类"""

    def __init__(self, loan, annRate, months):
        """假设loan和annRate为浮点数，month为整数
        创建一个总额为loan，期限为months，年利率为annRate的新抵押贷款"""
        self.loan = loan
        self.rate = annRate / 12 #简单分成12份就可以了，不用想复利。
        self.months = months
        # 以上的属性定义了条件，每次计算时基本不变

        self.paid = [0.0] # 第一个月不用付，以后追加。
        self.outstanding = [loan] # 第m个月残余的本金额，第一个月是贷款额
        self.payment = findPayment(loan, self.rate, months) # 算出第m个月的还款额，按照等额还款的定义，基本是不变的值。
        # 以上是计算的值

        self.legend = None  # 某种类型按揭贷款的说明

    def makePayment(self):
        """支付每月还款额"""
        # 正常计算当月还款额，并更新两个数组：月底还款，月底残留本金。
        self.paid.append(self.payment) # 当月还款额，追加到数组里。
        reduction = self.payment - self.outstanding[-1] * self.rate # 当月偿还本金的数量
        self.outstanding.append(self.outstanding[-1] - reduction) # 当月残留本金的值，追加到残余数组里。

    def getTotalPaid(self):
        """返回至今为止的支付总额"""
        return sum(self.paid)

    def __str__(self):
        return self.legend


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%'

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100)] # 替换Mortgage类里的0.0，初识时要付一笔手续费，并且不能抵扣本金。
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%, '\
                      + str(pts) + ' points'

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months) # 注意是用引诱利率初始化的Mortgage，但是用的总月份数初始化self.months。也就是说，用便宜的利率算到底，然后在中间重新核算。
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12
        self.legend = str(teaserRate*100)\
                     + '% for ' + str(self.teaserMonths)\
                     + ' months, then ' + str(round(r*100, 2)) + '%'
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
           self.rate = self.nextRate
           self.payment = findPayment(self.outstanding[-1],
                                   self.rate,
                                   self.months - self.teaserMonths)
        # 以上这段判断，是在teaser到期时，更新Mortgage的条件值：更新了利率，也按照那个时点的残留本金，重新计算了每月定额还款额。
        Mortgage.makePayment(self) # 正常计算当月还款额，并更新两个数组：月底还款，月底残留本金。


def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                     varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):# 逐月
        for mort in morts: # 核算每种还款方式的
            mort.makePayment() # 还款额 残余本金，添加入数组
    for m in morts: # 打印每种还款方式的
        print(m) # 还款方式
        print(' Total payments = $' + str(int(m.getTotalPaid()))) # 最终加总还款额

compareMortgages(amt=200000, years=30, fixedRate=0.07,
                 pts = 3.25, ptsRate=0.05, varRate1=0.045,
                 varRate2=0.095, varMonths=48)
