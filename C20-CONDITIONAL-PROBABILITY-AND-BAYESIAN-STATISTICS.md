# 20 CONDITIONAL PROBABILITY AND BAYESIAN STATISTICS


### 什么是统计学中的频率论方法？它的优点是？

我们从样本中得出的结论完全基于数据的频率frequency或比例proportion。这是最常用的一种推理框架inference framework，已经发展成为一种非常成熟的套路the well-established methodologies，主要内容包括本书前面介绍过的假设检验statistical hypothesis testing和置信区间confidence intervals。

从原则上说，这种方法的优点是无偏性unbiased，结论仅仅建立在观测到的数据之上。

### 概率主义者和贝叶斯统计学家怎么判断太阳是否爆炸了的问题？

![](https://ws4.sinaimg.cn/large/006tNc79gy1frdaka3qx7j30d00jpwfk.jpg)

图画中是什么情况呢？频率论统计学家很清楚，只有两种可能：探测器掷出一对6，表示它说了谎；或者掷出其他的数，表示它说的是真的。因为没有掷出一对6的概率是35/326（97.22%），所以频率论统计学家得出结论，探测器可能说的是真话。因此，太阳真的可能爆炸了。

贝叶斯统计学家在建立概率模型probability model时会加入额外的信息utilize addtional information。他也认为探测器不太可能掷出一对6，然而，他主张要将探测器说真话的概率与太阳没有爆炸的先验概率a priori进行比较。这位贝叶斯统计学家最终认为，太阳没有爆炸的概率比97.22%还要大，并决定赌“太阳明天照常升起”。


## 20.1 Conditional Probabilities


### 构成贝叶斯推理bayesian reasoning 基础的核心思想是什么？

条件概率conditional probability。

扔硬币事件有独立性，但生活并不总是这样。在很多实际情况中，独立性是个糟糕的假设。

P(A|B)表示当B为真时，A为真的概率，它经常读作“给定B时，A的概率the probabilty of A, given B”。

如果P(A)和P(B)是独立的，那么P(A|B) = P(A)。

一般地，如果P(B) ≠ 0，则：

![](https://ws3.sinaimg.cn/large/006tNc79gy1frdb1s51zij30be040dfy.jpg)

{\rm P}({\rm A|B})=\frac{{\rm P(A and B)}}{{\rm P(B)}}

与一般的概率一样，条件概率也位于0和1之间。而且，如果Ā表示not A，那么P(A|B) + P(Ā|B) = 1。

人们经常错误地认为P(A|B)等于P(B|A)，但这种想法是完全站不住脚的。例如，P(male|Maltese)的值大约等于0.5，但P(Maltese|male)只有大约0.000064。

公式P(A|B,C)表示当B和C同时成立时，A成立的概率。假设B和C是互不相关的，那么通过条件概率的定义和独立概率的乘法法则可知：

![](https://ws2.sinaimg.cn/large/006tNc79gy1frdbengcf6j30bw03eaa7.jpg)

{\rm P(A|B,C)}=\frac{{\rm P(A,B,C)}}{{\rm P(B,C)}}

这里的P(A,B,C)表示A,B和C同时为真的概率。

同样地，P(A,B|C)表示当C为真时，A和B同时为真的概率。

假设A和B是互不相关的，那么：

![](https://ws1.sinaimg.cn/large/006tNc79gy1frdbf4hi0wj30h602yt8w.jpg)

{\rm P(A,B|C)=P(A|C)*P(B|C)}


## 20.2 Bayes's Theorem


### 贝叶斯定理讲什么？

贝叶斯定理Bayes' Theorm（通常称为贝叶斯定律Law或贝叶斯法则Rule）

贝叶斯定理是以英国牧师托马斯·贝叶斯（1701—1761）的名字命名的，在他去世两年之后才第一次发表。拉普拉斯普及了这个定理，他在1812年发表的《概率分析理论》一书中，提出了这个定理的现代表示方法。

![](https://ws3.sinaimg.cn/large/006tNc79gy1frdbqq0gqwj30bs030mxa.jpg)

$$ {\rm P(A|B)}=\frac{{\rm P(A)*P(B|A)}}{{\rm P(B)}} $$

在贝叶斯统计中(In the Bayesian world)，概率测量的是可信度(probability measures a **degree of belief**)。贝叶斯定理表明了不考虑证据的可信度和考虑了证据的可信度之间的关系(Bayes' Theorem links the degree of belief in a proportion before and after accounting for evidence)。

公式等号左边的部分P(A|B)是后验posterior概率，即考虑了B之后的A的可信度(the degree of belief in A, having accounted for B)。后验概率定义为先验概率P(A)与证据B对A的支持度的乘积。(The posterior is defined in terms of the **prior**, P(A), and the **support** that the evidence, B, provides for A.)支持度是A成立的情况下B成立的概率与不考虑A时B成立的概率的比值(The support is the ratio of the probability of B holding if A holds and the probability of B holding independently of A)，即 \frac{{\rm P(B|A)}}{{\rm P(B)}}。
 
 ![](https://ws1.sinaimg.cn/large/006tNc79gy1frdbr61y2kj30dc0380sw.jpg)


### 一个年过不惑的女性应该如何面对阳性的乳腺X光检查结果呢？她确实罹患乳腺癌的概率是多少？

假设一个四十多岁的没有临床症状的女性做了一次乳腺X光检查，然后收到了一个坏消息：检查结果是“阳性”。

患有乳腺癌的女性通过乳腺X光检查确诊的真阳性概率为0.9。

而没有患乳腺癌的女性通过乳腺X光检查误诊为乳腺癌的假阳性概率为0.07。

对于四十多岁的女性来说，患有乳腺癌的比例是0.008（1000个人中有8个）。

定义三种情况

- Canc = has breast cancer 有癌症
- TP = true positive 真阳性，真有癌症
- FP = false positive 假阳性，没有癌症

表达上面三个已知概率

- P(TP | Canc) = 0.9
- P(FP | not Canc) = 0.07

- P(Canc | woman in her 40s) = 0.008
    - (P(not Canc | woman in her 40s) = 0.992)

要问的是，一个年过40的女性，X光检查阳性，她真有乳腺癌的概率是多少？

可以表述为 P(Cans|Pos)  

![](https://ws2.sinaimg.cn/large/006tNc79gy1frdcttg7qbj30ic038q38.jpg)

其中，Pos = X光检查结果为阳性
```commandline
P(Pos) = P(Pos|Canc) * P(Canc) + P(Pos|not Canc) * (1-P(Canc))
       = P(TP|Canc) * P(Canc | woman in her 40s) + P(FP|not Canc) * P(not Canc|woman in her 40s)
       = 0.9 * 0.008 + 0.07 * 0.992
       = 0.07664

P(Canc) = P(Canc | woman in her 40s) = 0.008

P(Poc|Canc) = P(TP|Canc) = 0.9
```
      
所以，一个年过40的女性，X光检查阳性，她真有乳腺癌的概率是多

P(Cans|Pos) = 0.008 * 0.9 / 0.07664 = 0.0994

大约90%的乳腺X光检查阳性结果都是假阳性！


### 有多大把握不会用蘑菇把丈夫毒死？

你正在森林中漫步，突然发现一片看上去非常鲜美的蘑菇。你采了满满一篮蘑菇，准备回家为丈夫准备一顿丰盛的晚餐。但是，在烹制蘑菇之前，丈夫建议你找本关于本地蘑菇种类的书参考一下，看看它们是否有毒。这本书说，在本地的森林中，80%的蘑菇都是有毒的。然而，你将你采的蘑菇与书中图片里的蘑菇对比了一下，确定有95%的把握可以认为你的蘑菇是安全的。那么你是否应该将蘑菇做给丈夫吃（如果你不想成为寡妇的话）？

定义

- badmush：书中的毒蘑菇
- P(badmush) = 0.8

此蘑菇不属于书中的毒蘑菇
P(not bad | badmush)

此蘑菇有毒


## 20.3 Bayesian Updating


### 什么过程是贝叶斯更新？

通过应用贝叶斯定理，贝叶斯推理提供了一种理论方法，可以使用新的证据修正先前的可信度。(Bayesian inference provides a pricipled way of combining new edvidence eith prior beliefs, through the application of Bayes' theorem.)

贝叶斯定理可以迭代iteratively使用：观测到一些新证据之后，可以将原来的后验概率作为先验概率，并根据新的证据计算出新的后验概率。这使得贝叶斯定理可以应用在各种类型的证据上，无论是一下子同时出现的证据，还是随着时间推移逐渐出现的证据。这个过程就称作贝叶斯更新。


### 一个贝叶斯更新的代码？

假设你有一个袋子，其中装有相同数量的三种骰子，每种骰子掷出6的概率都不一样。A类型的骰子掷出6的概率是1/5，B类型的骰子掷出6的概率是1/6，C类型的骰子掷出6的概率是1/7。把手伸进袋子，抓出1个骰子，并估计这个骰子是A类型的概率。甚至不需要很多概率知识你就可以知道，这个概率的最优估计值是1/3。然后，掷两次骰子，并根据结果修正你的估计。如果每次都掷出6，那么很明显这个骰子是A类型的可能性要更大一些。那么这个更大的可能性是多少呢？

根据贝叶斯定理，第一次掷出6后，这个骰子是A类型的概率为：

![](https://ws3.sinaimg.cn/large/006tNc79gy1frddx126c7j30bc02yq32.jpg)

其中：

![](https://ws2.sinaimg.cn/large/006tNc79gy1frddxc1gutj30me042wer.jpg)

```python
import random
def calcBayes(priorA, probBifA, probB):
    """priorA：A独立于B时的初始概率估计值
       probBifA：A为真时，B的概率估计值
       probB：B的概率估计值
       返回priorA*probBifA/probB"""
    return priorA*probBifA/probB

# priorA = 1/3
priorA = 0.9
prob6ifA = 1/5
prob6 = (1/5 + 1/6 + 1/7)/3

# postA = calcBayes(priorA, prob6ifA, prob6)
# print('Probability of type A =', round(postA, 4))
# postA = calcBayes(postA, prob6ifA, prob6)
# print('Probability of type A =', round(postA, 4))

# postA = calcBayes(priorA, 1 - prob6ifA, 1 - prob6)
# print('Probability of type A =', round(postA, 4))
# postA = calcBayes(postA, 1 - prob6ifA, 1 - prob6)
# print('Probability of type A =', round(postA, 4))

numRolls = 200
postA = priorA
for i in range(numRolls+1):
    if i%(numRolls//10) == 0:
       print('After', i, 'rolls. Probability of type A =',
             round(postA, 4))
    isSix = random.random() <= 1/7 #用1/7，因为其实是C类型的骰子。
    if isSix:
        postA = calcBayes(postA, prob6ifA, prob6)
    else:
        postA = calcBayes(postA, 1 - prob6ifA, 1 - prob6)
```

- 每次迭代，用新的postA更新priorA。
- 初始先验值不好也没关系，它会根据每次的新证据，逐渐向真相逼近。

---
以上，2018-05-16 19:08:20
