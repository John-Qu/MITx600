---
layout: post
title:  "INTRODUCTION TO COMPUTATION AND PROGRAMMING WITH PYTHON"
date: 2018-04-04 10:03:11 +0800
categories: notes
description: What have I get in learning this book?
---

# 计算与编程入门-以Python为工具

@(Note)[未完结, 进行中]


## 前言

### 课程从何而来

MIT是2006。MIT的OCW-Open CourseWare从2008年起，有2008，[2011](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/index.htm)（Guttag全程），[2016](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/index.htm)（Bell Grimson Guttag三人）三个版本。那里有给MIT学生的随堂习题、测验的PDF。

[edX](https://www.edx.org/)的MOOC-Massive Online Open Courses是2012起，目前的版本是2017年[8月](https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017_2/course/)和10月上线的，三人讲课。上下两门课的认证通道还有两个月关闭，费是49+49美元。

在“[学堂在线](http://www.xuetangx.com/courses/course-v1:MITx+6_00_1x+sp/courseware/Week_1/)”上面，是2016年版，中文字幕，不用翻墙即可播放。认证通道已关闭。

### 内容定位在哪里？

对少数人，它是进一步学习计算机科学的起步点。对大多数人，这可能是与计算机科学的唯一接触机会。所以，重广度而不是深度。

目的是：需要借助计算机时，知道可能做到什么。

不是“计算机欣赏”课；要投入大量的时间精力，才能学会如何让计算机为我所用。

主要目标：有产出的使用计算机技术，不是玩玩。`To became skillful at making productive use of computational techniques.`

走向目标的两条腿：用计算机的思维模式构造问题，主导从数据中提取信息的过程。`To use computaional modes of thoughts to frame problems and to guide the process of extracting information from data.`

带走的最主要的知识：一种艺术，计算机式解决问题的艺术。`the art of computional problem solving.`

### 怎么安排的篇章大结构？

1～11是基础篇，12～14是提高篇，15～24是数据篇。

### 为什么说是糅合？

在基础篇，糅合5方面材料：

1. 编程基础
2. Python3编程语言
3. 计算机式解决问题技巧
4. 计算复杂性
5. 用图形呈现信息

为什么说是糅合？就是要把学习编程经验和语言常识，放在让学生们在解决有趣的问题的活动中来做。

### 为什么在第二学期讲数据处理？

对大部分学生来书，更利益攸关。替代数据结构。

只需要高中数学知识即可。但是需要缜密的思考能力和面对数学概念时的镇定。`be comfortable with rigorous thinking and be not intimated by mathematical concepts.`

### 为什么不设章末习题？

#### 练习难度有三个层次：

1. 随堂确认学生理解；
2. 难一点可作课程测试；
3. 更有挑战性可作为家庭作业。

这就不适合一股脑都放在章节末尾了。我需要区别对待，并做好标记：哪个没做，哪个做到什么程度。

### 预期学完课程后，我会有什么变化？

#### 三个弥散性主题，类似于内功：
1. 讲系统地解决问题；
2. 抽象的力量；
3. 计算——作为一种思考世界的方式。

#### 七个具体收获，类似于招法：
1. 学得一种语言，Python，用来表达计算；
2. 学得一种系统方式，来组织、撰写、纠错中等规模的程序。
3. 发展了一种理解，对计算复杂性的非正式理解。
4. 发展了一种眼力，从模糊的问题陈述，到构建出可计算的方法，以解决问题，有眼力看穿这个过程。
5. 学到了一系列算法和简化问题的技巧。
6. 学到了如何用随机性和模拟，来解决传统封闭解法不容易解决的问题。
7. 学会了如何用计算机工具（包括简单统计，可视化和机器学习），来梳理和消化数据。

### 怎么检验是否学好了？

没有捷径。

做OCW或edX的习题。我选择edX，那里做完习题有实时打分，还有证书。

## 感谢哪些人

### 哪几位帮助很大？

Ana Bell的[LinkedIn](https://www.linkedin.com/in/anabell/)，[学校主页](http://www.mit.edu/~anabell/)，她是普林斯顿的博士，在普利斯顿当助教的时候发觉自己喜欢教学。

Eric Grimson，[wiki](https://en.wikipedia.org/wiki/Eric_Grimson)，在MIT教过好多年6.00课程。

学堂在线的[6002课程](http://www.xuetangx.com/courses/MITx/6_00_2x/2014_T2/about)里有三位老师的介绍。

Srinivas Devadas
Fredo Durand
Ron Rivest
Chris Terman

Guttag的大儿子David Guttag克服了对计算机的抵触，试读了此书。

### 学生中很多中国人？

十个学生对手搞的各个版本有建设性评论，其中三个人的名字像是来自于中国。

Jen Gong，Yun Liu，Amy Zhao。

### 要编辑有什么用？

从学生的角度，提出“建议”：需要做什么，应该做什么，可以做什么。

## 1. 怎么准备出发？

### 计算为什么要借助机器，靠人不行吗？

计算 = 运算 + 存储

人的能力很有限：大脑的运算速度和手的记录速度。

计算机擅长快速计算和大量存储。

快到什么程度？这台Mac Pro的CPU2.6GHz，每秒2.6*10^9次/秒，这是多块呢？光速是0.3*10^9米/秒，二者一比，就是9次/米，光走一米，计算机已经运算了9次！

存储量大到什么程度？这台Mac Pro是250GB，一个Byte约是8bits。2.5 * 10^11B，这相当于多少本书呢？

### 怎样才是“可计算地思考”？

知识按照是否可以操作分成两种：
1. 不可操作——Declarative Knowledge，宣称。
2. 可以操作——Imperative Knowledge，命令。

可计算地思考，就是寻找和构建命令式知识的过程。

### 为什么“算法algorithm”这个词有点怪？

它不是来自于希腊语或拉丁文，它来自一位波斯数学家的姓：`Muhammad ibn Musa al-Khawarizmi`

算法是菜谱。

算法是一有限句指示，描述一种计算，在一组输入的基础上，通过明确定义的状态转换，最终产出一个结果。

### 用机器实现算法走了哪两条路线？

固定程序计算器：弹道，线性方程组，密码破解，计算器。

存储程序计算器：Manchester Mark I。

### 可以存储的计算机必须加上哪两个辅助功能？

编译器和控制流。

### 程序员和厨师有什么相似？

基础的食材/动作，组合出无限可能。

### 编程语言有什么基本要求？

#### 用什么方式组织计算？是否可以编程？

用图灵机`Universal Turing Machine`组织计算：假想的计算装置：包含1. 无限长的纸带；2. 一个读写头；3. 一套控制规则表；4. 一个状态寄存器。注意这个机器的每一部分都是有限的，但它有一个潜在的无限长的纸带，因此这种机器只是一个理想的设备。图灵认为这样的一台机器就能模拟人类所能进行的任何计算过程。参考[博客](https://blog.csdn.net/godblessmyfamily/article/details/11635677)

图灵证明了，如果某个功能可计算，就可以用图灵机编程计算它。

这个“如果”有玄机。举个例子，停机问题halting problem。[据说](https://www.zhihu.com/question/20081359)它类似于集合论中的“自指”问题，罗素的理发师悖论。

好消息是：越来越多的现实问题，进入有能力有方法计算的范围了！

#### 图灵完备性`Turing completeness`？

别操心这个，现代所有语言都是完备的，也就是底层一致，彼此可以替换。

### 编程语言由什么构成？

语素`literals` `tokens`和符号`infix operators`。

### 什么是语法和语义？

三个层次。

语法`syntax`——在什么位置上该放哪类东西？

静态语义`static semantic`——前后关系是否合理？

语义`semantic`——含义是否明确准确？

### 一个程序可能出什么错？

最轻的：崩溃掉。
中间的：无限循环。程序员不知道程序需要运行多久时，很难判断。
最严重：给出了像样的结果，缺可能对，也可能不对。

如果不对，后果严重：病人误诊，飞机相撞。

所以，程序要能自证清白。

### 动手：写一个指路说明，看看他会得多少交通罚单？

## 2 INTRODUCTION TO PYTHON

### 编程语言的差别，可以用哪几对天平衡量？

低层*low-level* v.s. 高层*high-level*

通用*General* v.s. 定向特定领域 *targeted to an application domain* 

解释型 v.s. 编译型

### Python是什么类型的语言，有什么缺点和优点？

Python是比较高层的通用语言，属于解释型。

缺点有三：

1. 可以编写几乎任何程序，只要不需要直接与计算机硬件打交道。
2. 不对高可靠性做优化，因为静态语义检查比较弱。
3. 不适合很多人长期维护，也是因为静态语义检查弱。

有点

1. 相对容易学，因为解释器给出的运行反馈，对新手很有帮助。
2. 大量的免费库，扩展了功能。

### 通过此书学python，可以预期多少，有什么补救？

打个预防针：本书不是全面介绍Python的书。用多少讲多少，用到什么讲什么。

建议去看其他更全面的网络资源。

### Python的发展历史怎样，我们现在的版本可靠吗？

1990年，Guido von Rossum介绍Python给世界，起初很少人用。直到2000年Python2.0面世，很多人加入了python生态圈，作出很多无缝衔接的库。2008年，python3发布，清除了python2种很多不一致的地方，也造成与python2不兼容。

过去几年里，绝大多数公开领域的库完成了向python3的迁移，并用python3.5测试过。本书也是基于python3.5的。

### 一段`script`由什么组成？

一段程序*program*也称为代码*script*，是由一系列定义*definition*和命令*command*组成。

### 程序在哪里运行？

在shell里运行。一般一个程序打开一个shell，一个shell对应一个窗口。

### `object`是什么？定义类型`type`有什么意义？类型大体分为哪两种？

对象*object*是Python程序操作的核心。每个object都有自己的一个类型*type*，它定义了可以对它做什么种类的操作。

### 所有`type`都能从字面上看出来吗？

如果打出它的定义形态，一般可以从字面上看出来，比如`3`，`'abc'`。

### 有哪四种标量类型？

1. 整数
2. 浮点数
3. 布尔
4. None

### 为什么不把`float`类型干脆叫做`real`？

实数*real number*在现代编程系统中都用浮点数*floating point number*形式来存储。它有很多优点，但是在某些情况下，也造成浮点运算与实数运算有所不同。

### 表达式`expression`由什么构成，有什么归宿？

> Objects and operators can be combined to form expressions, each of which evaluates to an object of some type. We will refer to this as the value of the expression.

### 给`int`和`float`可以加什么操作符？

`i + - * j` either one is float, the result is float

`i / j` i divided by j

`i // j`  interger division

`i % j` i mod j, i modulo j;

`i ** j` i raised to the power j

`i == != > >= < <= j`

### 变量*variable*和赋值*assignment*仅仅是什么？

Variable is just a name.

Assignment associates a name with an object. An object can have one, more than one, or no name associated with it.  

### 为什么要给变量起个合适*apt*的名字？

帮助读程序的人进入思考/反省模式：

读一段程序：

```
a = 3.14159
b = 11.2
c = a*(b**2)
```
这段程序有什么问题吗？

再看这段：

```
pi = 3.14159
diameter = 11.2
area = pi*(diameter**2)
```

发现什么问题了吗？

### python 3 的保留字都有什么？

`and, as, assert, break, class, continue, def, elif, except, False, finally, for, from, global, if, import, in, is, lambda, nonlocal, None, not, or, pass, raise, return, True, try, while, with, yield`

### 怎样实现变量调换值？利用了赋值的什么性质？

`x, y = y, x`

赋值时，先计算`=`右边的表达式。

### 推荐哪些Python的IDE？

IDE：Integrated Development Environment

IDLE
anaconda
canopy

我用的是PyCharm

### 缩进有意义吗？“行”的概念重要吗？

缩进在语义上有意义，表达block关系。

正因为缩进有意义，line的概念在Python中才重要。

### 怎样尽量避免nested condition？

用复合布尔表达式。

### 只有分支结构的程序，有什么特性？

得到执行的语句一定比语句总数要少。 

### 恒定时间*constant time*的程序有什么特点？

这里的恒定，是说可以找到一个常数，时间不会超过它。

### 什么是过载*overloaded*？

针对运算符或函数来说的。运算符会检测它操作的对象类型，执行功能类似，然而有所不同（大同小异）的操作。

### 在python的版本演化中，类型检查的强弱有变化吗？

Python2中，类型检查不强。Python3中，禁止了一些没啥意思的类型容错。

例如: `'a' < 2` 在python2中认为一切字母都小于数字，但是在Python3中，静态语法检查会报错，因为这种比较没什么实际意义。

### 输入函数input在python2和python3中有什么不同？

Python3的`input`相当于Python2的`raw input`。它把用户输入的内容都转化成字符串。程序需要用特定代码，把字符串转换*type conversion or type cast*成相应的类型。

Python2里的`input`，会根据输入内容自动决定函数返回对象的类型。

### 编码的两个大系统里，现在最常用哪套编码？占多少比例？

过去曾经使用ASCII系统（128个），现在多使用Unicode（12万个）。

全世界的网站，截至2016年，有85%以上使用UTF-8编码。

`# -*- coding: utf-8 -*-`

## 3 SOME SIMPLE NUMERICAL PROGRAMS

### 用`while`的时候必须想好什么？

decrement function，什么时候停下来。

### decrementing function有哪四个属性？

从问题中提取一组变量，把它映射到一个变量；
这个变量的初始值非负；
每次运算这个变量都会变小；
小于等于零，就停止循环。

### 可以使用猜试法的问题，有什么特征？

猜试系：猜一个结果，试一下对不对，不对就再猜。

前提
* 试起来很容易。
* 错了没惩罚。
* 以可以接受的成本，有望得到答案。

### 猜试法中有一种什么有效的"笨"办法？

穷举法——把答案空间中的所有可能都试一下，要么找到答案，要么证明没有。

为什么有效呢？

* 方法简单粗暴，相对于手工推演等算法，实现更容易。
* 节省了想算法的时间。
* 计算机的速度很快。

### `range(start, stop, step)`的三个参数怎么理解，输出什么结果？

start是砖，肯定能踩准；stop是墙，以step来走，永远不会触碰。

### 在python3里，`range(100000)`会占用很多空间吗？

不会。

> be generated on an "as needed" basis.

这个功能在Python2中需要使用`xrange()`。

### 用计算机解平方根，与手工解法一样吗？

手工一步步试商；计算机小步走，乘方后检验是否足够接近。 

计算机的解题方法经常与手工不一样。

### 什么样就算是一个好答案？

按照问题定义的程度，足够接近，就是好答案。

更接近，或者完全吻合，并不会更好*no better than*。

### 二分查找与齐步走查找本质区别在哪里？

步长不同。
* 齐步走每次迈一小步，保证不漏过真正的正确值。
* 二分法每次排除一半的空间，越来越接近正确值。

这就带来几个不同的表现。
* 齐步走可能漏过；二分法不会漏过。
* 齐步走的计算量可以估计，二分法变动比较大。

二分法有个前提：可能空间和比较空间都是有序的。

### 二分查找法仅仅限于解平方根吗？它属于哪个系列？

不限于解平方根，也可以解立方根，只要结果空间的大小比较，可以用来指导选择可能空间的哪一半，就可以使用。也就是说，"大了，就往小里找"，或者相反。

它属于猜试法。

