# 20 LIES, DAMNED LIES, AND STATISTICS

### 当我证明不了我想证明的东西？

“如果你想证明某事，却发现没有能力办到，那么试着解释其他事情并假装它们是一回事。在统计资料与人类思维冲撞所引起的耀眼光芒中，几乎没有人会发现它们的区别。”

If you can't prove what you want to prove, demonstrate something else and pretend they are the same thing. In the daze that follows the collision of statistics with the human mind, hardly anyone will notice the difference.

Darrell Huff, How to Lie with Statistics, 1954.


### 统计思维符合人的思维习惯吗？

人只对一些统计现象有直觉的认识，比如男人普遍比女人高，但是缺乏有效的数学工具。

人们更喜欢以定性的方式去评价事物，而不是以定量的方式。

- qualitatively vs quantitatively
- assess things


### 本章讲统计数据如何误导人得出不合适的推论，初衷是什么？

更好的消费者，更诚实的供应商。

to become a better consumer, and a more honest purveyor of statistical information


## 21.1 Garbage In Garbage Out(GIGO)


### 查尔斯·巴贝奇在国会遭遇过什么提问？

“我曾经有两次被（国会议员）问道：‘巴贝奇先生，如果你向计算机中输入了错误的数字，会得出正确结果吗？’我实在无法理解，思维该有多么混乱才能问出这种愚蠢的问题。”

On two occasions I have been asked [by members of Parliament], 'Pray, Mr. Barbbage, if you put into the machine wrong figures, will the right answers come out?' I am not able rightly to apprehend the kind of confusion of ideas that could provoke such a question.

——查尔斯·巴贝奇 Charles Barbbage

1791—1871，英国数学家、机械工程师，公认设计出了第一台可编程的计算机。他最终也没有成功制造出一台可以实际工作的机器。但是在1991年，一台可以运行的机械装置终于被制造出来了，用于求解多项式，所依据的就是他原初的计划。

注意到了吗？

Garbage 与 Barbbage


## 21.2 Tests Are Imperfect


### 做实验、做测验的时候要有什么心理准备？

a potentially flawed test

事实没有责任必须与实验结果一致。

例如：单词测试。
- 共100个词，某学生掌握了80个。
- 考20个词，学生答对16个。
- 上述事件的概率是1吗？


### 假阳性很有必要吗？

假阳性很高。

- 测试太灵敏，目标事件概率太高。
- 真实事件的概率其实没有这么高。罕见病。

the cost of a false negative is high.

- 结果严重。
- 早发现能治好。


## 21.3 Pictures Can Be Deceiving


### 柱状图怎么误导变动程度？

美国中西部房价

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/24.d21z.001.png)

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/24.d21z.002.png)

男女学生平均分差距

![](https://ws3.sinaimg.cn/large/006tNc79gy1free6ok3yqj31e212ijw3.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79gy1free74kcjoj31kw11f799.jpg)

Moral: Look carefully at the axes labels and scales


## 21.4 相关当成了因果Cum Hoc Ergo Propter Hoc


### 举几个"相关当成了因果"的例子？

1）经常上课的学生的成绩更好。

2）美国学校开学与流感爆发。潜在变量lurking variable

3）多进口墨西哥柠檬能降低公路死亡率。

4）接受HRT的女性因心血管疾病死亡的比例会降低。


## 21.5 Statistical Measures Don't tell the Whole Story


### 为什么要亲自看原始数据？

There are an enormous number of different statistics that can be extracted from a data set. Be carefully choosing among these, it is possible to convey a variaty of different impressions about the same data.

- 同一组数据，不同的印象。
- 各种各样的统计量。

The moral is simple: if possible, always take a look at some representation of the raw data.

Four groups each containing 11 x, y pairs


### 统计量完全相同的四组数据，其实真的相像吗？

![](https://ws4.sinaimg.cn/large/006tNc79gy1free3ec1obj315g12uwvr.jpg)

Summary statistics for groups identical ◦ Mean x = 9.0
◦ Mean y = 7.5
◦ Variance of x = 10.0
◦ Variance of y = 3.75
◦ Linear regression model: y = 0.5x + 3

Are four data sets really similar?

![](https://ws3.sinaimg.cn/large/006tNc79gy1free38x1hsj31by10g0xy.jpg)

Moral: Statistics about the data is not the same as the data

Moral: Use visualization tools to look at the data itself


## 21.6 Sampling Bias


### 抽样偏差有什么表现形式？

non-response bias

- 用不来上课投票的人，不会参加结课调查。
- 真正关键部位被击中的飞机，不会飞回来检修。

convenience (or accidental) sampling

- 心理学研究的样本多是大学本科生。


## 21.7 Context Matters


### 举几个上下文语境信息很重要的例子？

- 墨西哥猪流感2500人感染，159人死亡。美国每年季节性流感死亡36000例。
- 多数车祸发生在家的10英里范围内。
- 美国大约99.8%的枪支都没有用于暴力犯罪。据美国步枪协会报道，该国大约有3亿私人枪支，3亿的0.2%就是600,000！


## 21.8 Beware of Extrapolation


### 美国互联网用户比例会超过100%？

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/24.d21z.005.png)

Extrapolation should be done only when one has a sound theoretical justification for doing so.


## 21.9 The Texas Sharpshooter Fallacy


### 446位厌食症女性中有48人出生在六月份，说明初夏出生的女性更容易患厌食症吗？

```python
import random


def juneProb(numTrials):
    june48 = 0
    for trial in range(numTrials):
      june = 0
      for i in range(446):
          if random.randint(1,12) == 6:
              june += 1
      if june >= 48:
          june48 += 1
    jProb = round(june48/numTrials, 4)
    print('Probability of at least 48 births in June =', jProb)


juneProb(10000)


def anyProb(numTrials):
    anyMonth48 = 0
    for trial in range(numTrials):
      months = [0]*12
      for i in range(446):
          months[random.randint(0,11)] += 1
      if max(months) >= 48:
          anyMonth48 += 1
    aProb = round(anyMonth48/numTrials, 4)
    print('Probability of at least 48 births in some month =',aProb)


anyProb(10000)
```

```commandline
Probability of at least 48 births in June = 0.0423
Probability of at least 48 births in some month = 0.4468
```

可见
- 六月里出生超过48位而不是37位，确实是很小概率的事件。
- 任意一个月出生超过48位，就不是什么小概率事件了。
- 可以在那场分配中说那个月是患者多发月吗？
- 这是典型的多重检验？


## 21.10 Percentage Can Confuse


### 股价先降又升，赚了还是赔了？

“在我看来，”他说，“我的投资组合的价值下降了8%，可你却告诉我每月上涨了0.5%。”

“我没这么说，”投资顾问答道，“我告诉你的是平均每月变动为+0.5%。”

客户查看每月结算单时，发现投资顾问没有撒谎，但是误导了他。

客户的投资组合的价值在前半年每月下降了15%，在后半年则每月提高了16%。

考虑百分比时，我们一定要注意计算百分比时使用的基数。在本例中，相对于16%的提高速度，以15%的速度下降时的基数更大。


## 21.11 Statistically Significant Difference Can Be Insignificant


### MIT的男女入学成绩之间真的有显著差别吗？

统计学上的significant，不是普通语境下的meaningful.

如果2500男生，2500女生，GPA分别是3.5和3.51，这个差别在2%水平上显著。

样本足够多，不大的差别也可以很"显著"。

另：样本太少也会出现怪现象：两次硬币正面的p值竟然是0.


## 21.12 The Regressive Fallacy


### 什么是回归假象Regressive Fallacy？

人们没有考虑到事件的正常波动natural fluctuations of events。

- 运动员的表现有波动。低谷期喜欢多做改变，回归平均值的规律下，表现确实有上升，错误地以为有treatment effect.
- 飞行员飞得好，表扬了反而变差；飞得差，大骂一顿果然表现变好。


### 臆想出根本不存在的处理效应很危险吗？

它可以使我们相信
- 疫苗接种对身体有害、
- 蛇油可以包治百病、
- 为上一年“击败市场”的共同基金倾注全部投资是一种好的策略。


## 21.13 Just Beware


### 本章标题LIES, DAMNED LIES, AND STATISTICS的意思是？

用numbers撒谎，就像用words撒谎一样容易。


### 得知统计数字会撒谎之后，我们如何自处？

Make sure that you understand 

what is actually being measured and

how those "statistically significant" results were computed

before you jump to conclusions. 


### 关于数据，Huff和Coase说过什么类似而相反的话？

If you torture the data long enough, it will confess to anything.

科斯在1960s年代说过：

If you torture the data enough, nature will always confess.

不相反，nature坦白/屈服于施刑者。

参考
https://en.wiktionary.org/wiki/if_you_torture_the_data_long_enough,_it_will_confess_to_anything

https://en.wikiquote.org/wiki/Ronald_Coase

https://www.barrypopik.com/index.php/new_york_city/entry/if_you_torture_the_data_long_enough_it_will_confess

---
以上，2018-05-17 17:21:07