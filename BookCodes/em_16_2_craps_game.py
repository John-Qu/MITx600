import random, pylab

# 引用stdDev就够了。stdDev引用的variance不用单独提出来。
# 注意引用module中的可执行命令都会得到执行，最好先行注释掉。
from em_15_3_flip import stdDev


def rollDie():
    """
    正常的单骰子，随机得到1～6之间的一个正整数。
    :return: 正整数，在1～6之间
    """
    return random.choice([1,2,3,4,5,6])
    # return random.choice([1,1,2,3,3,4,4,5,5,5,6,6])


class CrapsGame(object):
    """
    给双骰子赌博建抽象类，特殊目的是比较pass和dp的投资回报率。
    因此，没有区分game是pass line还是don't pass line.
    而是分别建立instance attibutes。
    """
    def __init__(self):
        self.passWins, self.passLosses = 0, 0
        self.dpWins, self.dpLosses, self.dpPushes = 0, 0, 0

    def playHand(self):
        # 记录双骰子结果
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else: # throw = 2或3
                self.dpWins += 1
        else: # throw = 4 5 6 8 9 10
            # 上次throw存为point点数
            point = throw
            while True:
                # 再扔一把
                throw = rollDie() + rollDie()
                if throw == point: # 先达到了点数
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7: # 先达到了7线
                    self.passLosses += 1
                    self.dpWins += 1
                    break

    def playHand_with_dict(self):
        """playHand函数的另外一种更快的实现方式"""
        pointsDict = {4: 1 / 3, 5: 2 / 5, 6: 5 / 11, 8: 5 / 11, 9: 2 / 5, 10: 1 / 3}
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpPushes += 1
            else:
                self.dpWins += 1
        else:
            # 下面比的是出现的相对概率，道理如下：
            # 比如8点，两个骰子组合出8点有5种情况，组合出7点有6种情况。掷出11种情况中的任何一种，游戏结束。
            # 只看这11种可以让游戏结束的组合，那么8点相对于7点，出现的相对概率是5/11。
            # 上面那句也可以理解成：把[0, 1)区间均匀分成了11份。生成一个[0,1)间的随机数，如果它落在左边5份，则认为是8点，如果它落在了右边6份，则认为是7点。
            if random.random() <= pointsDict[throw]:  # 在掷出7之前掷出点数
                self.passWins += 1
                self.dpLosses += 1
            else:  # 在掷出点数之前掷出7
                self.passLosses += 1
                self.dpWins += 1

    # 把pass line的信息打包输出。
    def passResults(self):
        return (self.passWins, self.passLosses)

    # 把don't pass line的信息打包输出。
    def dpResults(self):
        return (self.dpWins, self.dpLosses, self.dpPushes)


def crapsSim(handsPerGame, numGames):
    """假设handsPerGame和numGames是正整数
       玩numGames次游戏，每次handsPerGame手；输出结果。"""
    games = []

    #玩numGames次游戏，为了取平均值。
    for t in range(numGames):
        c = CrapsGame()
        for i in range(handsPerGame):
            c.playHand_with_dict()
        games.append(c)

    #为每次游戏生成统计量
    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        # Return on Investment
        wins, losses = g.passResults()
        pROIPerGame.append((wins - losses)/float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins - losses)/float(handsPerGame))

    #生成并输出摘要统计量
    # 先乘100，再做round，不然会出尾数。
    meanROI = str(round((100*sum(pROIPerGame)/numGames), 4)) + '%'
    sigma = str(round(100*stdDev(pROIPerGame), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev. =', sigma)
    meanROI = str(round((100*sum(dpROIPerGame)/numGames), 4)) +'%'
    sigma = str(round(100*stdDev(dpROIPerGame), 4)) + '%'
    print('Don\'t pass:','Mean ROI =', meanROI, 'Std Dev =', sigma)


# crapsSim(20, 10)
# Pass: Mean ROI = 2.0% Std. Dev. = 14.6969%
# Don't pass: Mean ROI = -6.0% Std Dev = 14.9666%

# crapsSim(20, 10)
# Pass: Mean ROI = -0.0% Std. Dev. = 26.8328%
# Don't pass: Mean ROI = -3.5% Std Dev = 25.7924%

# crapsSim(20, 10)
# Pass: Mean ROI = -14.0% Std. Dev. = 19.5959%
# Don't pass: Mean ROI = 11.0% Std Dev = 18.8149%

# crapsSim(100000, 10)
# Pass: Mean ROI = -1.463% Std. Dev. = 0.3025%
# Don't pass: Mean ROI = -1.3021% Std Dev = 0.2844%

# crapsSim(20, 100000)
# Pass: Mean ROI = -1.3093% Std. Dev. = 22.3475%
# Don't pass: Mean ROI = -1.4659% Std Dev = 22.0177%

crapsSim(2000, 10000)
