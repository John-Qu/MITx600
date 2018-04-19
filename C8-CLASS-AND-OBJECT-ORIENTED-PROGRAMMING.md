# 8 CLASSES AND OBJECT-ORIENTED PROGRAMMING


### 在Python里，用class做什么？

> to organize programs around modules and data abstraction.

- 在modules和data层次。
- 是组织程序的一种方式。
- abstraction的是data。


### class只有一种用法吗？

很多种用法，其他是什么？

主要是"面向对象编程"。object-oriented programming.


### OOP有多久历史？

1970年代，提出这个思想，有Xerox PARC和CLU语言上支持。

当C++和Java出现后，才真正实用。


### modulization的方法之一是functioning，另一种是什么？

另一种是用class定义type。


### 什么是Objects？

> Objects are the core things that Python programs manipulate. Every object has a type that defines the kinds of things that programs can do with that object. 


## 8.1 Abstract Data Types and Classes


### 什么是abstract data type?



> An abstract data type is a set of objects and the operations on those objects. 

- 是一些对象，是复数的对象。
- 不只是对象，还有操作。
- 写成class、实现abstract data type的过程也称为：type abstraction, data abstraction或简称abstraction。


### 在class里method的specification是什么作用？

> The specifications of those operations define an **interface** between the abstract data type and the rest of the program. 
The interface defines the behavior of the operations—what they do, but not how they do it. 
The interface thus provides an **abstraction barrier** that isolates the rest of the program from the data structures, algorithms, and code involved in providing a realization of the type abstraction.

- 是operation的specification，而不是class的，也不是class attributes的。
- 谁和谁的接口？abstract data type与调用它的程序。
- 函数的specification是一个合同，这里的也一样。
- interface设计得好的话，应该形成一道屏障，让使用者不必关心实现方式，只要看specification就够了。


### abstraction在编程中处于什么地位/有什么价值？

> Programming is about managing complexity in a way that facilitates change. There are two powerful mechanisms available for accomplishing this: decomposition and abstraction. Decomposition creates structure in a program, and abstraction suppresses detail.

- 编程就是管理复杂。
- 管理手段要让变化造成的困难尽可能少，因为必然有变化。
- decomposition和abstraction就是两个有力的手段。
- decomposition让程序有了结构。
- abstraction抑制掉不必要的细节。


### 抑制细节的关键是什么？

合适appropriate

这正是data abstracion的存在价值。

> One can create domain-specific types that provide a convenient abstraction. Ideally, these types capture concepts that will be relevant over the lifetime of a program. If one starts the programming process by devising types that will be relevant months and even decades later, one has a great leg up in maintaining that software.

- 特定领域内的具体类型。
- 抽象的目的是方便。
- 理想是抓住概念的本质，软件整个生命周期都相关，都有所使用。
- 构建的type生命越长，编程者的责任越长。


### class定义的对象，对内对外都是什么类型？

```python
s = IntSet()
print(type(IntSet), type(IntSet.insert))
print(type(s), type(s.insert))
```

在Python2里返回
```commandline
(<type 'type'>, <type 'instancemethod'>)
(<class '__main__.IntSet'>, <type 'instancemethod'>)
```

在Python3里返回
```commandline
<class 'type'> <class 'function'>
<class '__main__.IntSet'> <class 'method'>
```

从Python3这里看出

- class对象的类型是type，名称是IntSet。
- s = IntSet()后，s的类型才是IntSet。
- method的类型，对IntSet来说是function，对s来说才是(instance)method。


### class下面的docstring写什么？#comments写什么？

docstring描述了class提供的abstraction，不含怎么实现。

comments才讲如何实现，给通过它建立subclass的人看。


### class的attributes有哪几种？

1. method attributes
- 例如`IntSet.member`，是这个class的attribute。
- 只有`s = IntSet()`后，**instance attributes**`s.member`才被创建。
- 二者是不同对像。甚至可以替换掉原功能`s.member = IntSet.insert`(不应该)
2. data attributes
- class内部专用的data attributes叫做class variables.
- instance的data attribute称为instance variables.
- 每个instance都有一个独立的这个data attribute，各个不同.


### 给class variable举个例子？

注意class的data attributes的写法。nextIdNum.

```python
class MITPerson(Person):
    
    nextIdNum = 0 # identification number
    
    def __init__(self, name): 
        Person.__init__(self, name) 
        self.idNum = MITPerson.nextIdNum # 使用class variable
        MITPerson.nextIdNum += 1 # 并及时更新。
```


### class支持哪两种操作？

1. Instantiation 
   - s = IntSet()
2. Attribute references 
   - s.member


### method的第一个形式参数一定写成self吗？

不一定。但全宇宙都约定了这么写。


### 为什么说data abstraction获得了representation-independence?

实现一个abstract type，包含三部分：

1. 实现应用于这个type的方法。
2. data structure，包含这个type的values。
3. 一些规定，限制了在1的method如何使用2的data structure。


### 什么是representaion-independence？

外部调用它，只能看到它的interface。里买怎么实现不用管，将来有更好的方式实现，改成效率更高的实现方式发，也不会影响外部调用的方式。

这里有一篇印第安纳大学的[讲座笔记](https://www.cs.indiana.edu/usr/local/www/classes/c311/a3/ri_interpreter.pdf)


### 实现abstract date时，关键的规定是什么？

representation invariant

- 表现不变量？
- 表达形式中的前后一致共同守则。
- 到底是"量"？还是"规则"？在video中再听一听。

在IntSet例子中

The representation invariant defines which values of the data attributes correspond to valid representations of class instances. 

The representation invariant for IntSet is that vals contains no duplicates. The implementation of __init__ is responsible for establishing the invariant (which holds on the empty list), and the other methods are responsible for maintaining that invariant. That is why insert appends e only if it is not already in self.vals.

The implementation of remove exploits the assumption that the representation invariant is satisfied when remove is entered. It calls list.remove only once, since the representation invariant guarantees that there is at most one occurrence of e in self.vals.


### 在class定义中的__str__方法怎么调用？

str是构建了一个str，传递这个class的信息。

四种调用方式 s = IntSet()

- print(s)
- print(s.__str__())
- print(IntSet.__str__(s))
- print(str(s))


### Abstraction是我们组织对世界的知识的方式吗？对组织程序有什么启发？

Abstract data types are a big deal. They lead to a different way of thinking about organizing large programs. 

When we think about the world, we rely on abstractions. In the world of finance people talk about stocks and bonds. In the world of biology people talk about proteins and residues. When trying to understand these concepts, we mentally gather together some of the relevant data and features of these kinds of objects into one intellectual package. For example, we think of bonds as having an interest rate and a maturity date as data attributes. We also think of bonds as having operations such as “set price” and “calculate yield to maturity.” 

Abstract data types allow us to incorporate this kind of organization into the design of programs.

把对世界的观察结果提炼成了一些概念。一旦提起这些概念，脑中就会浮现出它背后的对象和数据，还有针对这些概念可能做的动作。


### abstraction与function谁是核心？

> Data abstraction encourages program designers to focus on the centrality of data objects rather than functions. 

centrality 中心地位

设计者以数据对象为中心，而不是函数。


### data abstraction和function，谁的functionality更强？

> Thinking about a program more as a collection of types than as a collection of functions leads to a profoundly different organizing principle. Among other things, it encourages one to think about programming as a process of combining relatively large chunks, since data abstractions typically encompass more functionality than do individual functions. 

functionality 机能性，实现一个完整功能

function只是一个动作，而不是一项功能。


### 程序设计者怎么看编程？核心是什么？

> This, in turn, leads us to think of the essence of programming as a process not of writing individual lines of code, but of composing abstractions.

编程的核心不是写一行行代码，而是把抽象对象综合起来。像作曲，把一个个乐思前后衔接成全曲。


### 可以重用的abstraction给程序累积带来哪两个好处？

> The availability of reusable abstractions not only reduces development time, but also usually leads to more reliable programs, because mature software is usually more reliable than new software. For many years, the only program libraries in common use were statistical or scientific. Today, however, there is a great range of available program libraries (especially for Python), often based on a rich set of data abstractions, as we shall see later in this book.

1. 当然是避免重复开发的时间。
2. 久经考验的代码更可靠。


### 怎样才是获得instance attribute的合适姿态？

有两种。

1. 写一个方法，给这个attribute套上一层外衣。
him.getLastName() v.s. him.lastname.
2. 写一个方法，从这个attribute中推导出其他信息。
print him.getName(), 'is', him.getAge(), 'days old'


### overload掉__lt__还有什么好处？

好处之一很明显，可以直接写<号了。

另一个好处是用到<的地方，也更新了算法。

> this overloading provides automatic access to any polymorphic method defined using __lt__. The built-in method sort is one such method.


## 8.2 Inheritance


### "继承"给程序带来什么好处？

> **Inheritance** provides a convenient mechanism for building groups of related abstractions. It allows programmers to create a type hierarchy in which each type inherits attributes from the types above it in the hierarchy.

这是模拟了真实世界的概念层次关系。

在真实世界中，留意这种属性继承，方法光大的概念层次结构。


### 子类的init要怎么初始化超类的数据属性？

```python
class MITPerson(Person):

    def __init__(self, name):
        Person.__init__(self, name)
```

要知道这个init做的什么，必须去Person看？


### 子类除了继承它的超类的属性，还能做什么？

- 添加新的属性（包括类变量，实例变量和实例方法）。
- 覆盖超类中的属性。


### 类变量与实例变量有什么区别？

类变量是属于这个类，而不是属于类的某一个实例，它是创建类的时候被初始化，可以在每次执行类中的某一个方法时被更新。

实例变量是在创建类的实例时产生，只在这个实例中存在。

看写法：
```python
class MITPerson(Person):

    nextIdNum = 0 #在方法外面初始化，类似全局变量。

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum #注意类变量的写法，与全局变量不同。
        MITPerson.nextIdNum += 1 #更新类变量，保证id不重复。
```


### 在两种不同类型对象之间比较，会调用哪个方法？

p1 = MITPerson('Mark Guttag')
p4 = Person('Billy Bob Beaver')

print('p4 < p1 =', p4 < p1)

输出
p4 < p1 = True

因为p4是Person类型，其中

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName


Print('p1 < p4 =', p1 < p4)

输出
AttributeError: 'Person' object has no attribute 'idNum'

因为p1是MITPerson类型，其中

    def __lt__(self, other):
        return self.idNum < other.idNum


### 如何创建没有新属性的类，形成多重继承？

```python
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass
```


![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/11.d08z.001.png)


### 为什么要创建没有新属性的类，形成多重继承？

以下图为例，有两种情况。

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/11.d08z.001.png)

- Grad, 做同层区分。
- Student, 形成总括方便归类。


### 判断是否是学生，直接写type == 学生类1 / 学生类2不是就可以了吗？

如果将来增加"学生类3"，就要回头去改代码。

```python
p6 = UG('Billy Beaver', 1984)
```

有Student类，可以这样写，增加学生类3之后不需要改。：

```python
def isStudent(self):
    return isinstance(self, Student)
```
    
    
没有Student类，只能这样写，而增加学生类3之后需要回头改。

```python
def isStudent(self):
     return type(self) == Grad or type(self) == UG
```

注意区分

isinstance(p6, Student) 返回 True
type(p6) == Student 返回 False


> It is not unusual during the creation and later maintenance of a program to go back and add new classes or new attributes to old classes. Good programmers design their programs so as to minimize the amount of code that might need to be changed when that is done.

- 追加东西是常态。
- 为常态的不确定性预先铺摊子。


### 爸爸能干的事，儿子必须也能干？

儿子可以继承并发扬爸爸的本领，也就是用不同的方法来做事情。但是爸爸能干的活，儿子必须也能干。

相反，儿子可以做的事，不能要求爸爸也能做到。

这不是天经地义吗？

称为substitution principle.


## Encapsulation and Information Hiding


### 什么是封装？举例说明。

有了类型定义：
```python
class MITPerson(Person):

    nextIdNum = 0 #identification number

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
```

就可以写一行代码，把一个人的名字、学号这样的数据，以及读名字，读学号这样针对数据的方法，打包在一个实例名里，通过dot形式来调用。


```python
Rafael = MITPerson('Rafael Reif')
print(Rafael.getName())
print(Rafael.getIdNum())
```

这就是封装。


### 什么是信息隐藏information hiding？正面说法如何？

它是模块化的关键。

类的使用者不需要知道类是如何实现的，使用者也不能够破坏类的实现方式以及类的结构和数据。

这样类的实现者就可以随便修改类的实现方式，而不用担心因为实现方式的更新，而影响了使用者。

前提是累的使用者和实现者达成共识，遵守合同specification约定。


### Python如何实现和保证类的内部信息不被外部更改？

Python做得不好。

Java和C都有强制隐藏信息的机制，程序员可以使类的属性成为私有，这样类的客户代码只能通过对象方法访问数据。。

#### Python使用命名惯例隐藏属性和方法，但是在子类中也无法继承。

```python
class subClass(infoHiding):
   def __init__(self):
        print('from subclass', self.__invisible)

testSub = subClass()
```

会输出：

Error: 'subClass' object has no attribute '_subClass__invisible'

这是AttributeError异常。


#### Python可以在类定义之外，通过实例来增加类属性。

```python
me.age = Rafael.getIdNum()
```

python竟然不会报错。

怎么办？

- 不用__命名方法来隐藏属性，而是约束自己。
- 不在客户代码中直接访问类的数据属性。


### 为什么要在getStudents中返回实例变量数据属性的一个副本，而不是直接返回数据属性本身？

self.students是list，可能引发副作用。虽然复制一个有点麻烦，但是有必要。

```python
allStudents = course1.getStudents()
allStudents.extend(course2.getStudents())
```

如果getStudents返回self.students，那么第二行代码就可能产生一个（意料之外的）副作用，修改course1中的学生集合。


### 怎样克服隐藏信息造成的复制数据的效率损失？

不直接复制，而是用yield把函数做成一个生成器generator。

一次返回一个值，次与次之间，迭代器会往下走。

for 语句配合着使用。

```python
def getStudents(self):
    for s in self.students:
        yield s
        
for s in course.getStudents():
    print(s)
```


## 8.2 Mortgages, an Extended Example


### 网上查来的公式，要确认一下什么？

- 公式来源值得信赖。对比多个来源，公式是否等价。
- 充分理解公式中每个变量的含义。
- 用其他可信来源的数据测试自己的代码。

### 每月固定金额还款的计算公式推导过程？

x：当月还款额，定额还款的话，每个月都是x。
loan：贷款额。
r：月利率，只要把年利率除以12即可。
m：第几个月。

推导思想是——钱的时间价值

- 第m个月还的钱x，折算到借款发生时，只考虑利率的话，其价值是x/(1+r)**m。
- 它形成一个等比数列，初始值是x/(1+r)，公比是1/(1+r)。
- 各期还款折算到当下借款时的价值，求和后应该等于借款总额，否则有一方就可以套利了。

loan = x/(1+r) * (1 - (1/(1+r))**m) / (1 - 1/(1+r))

x = loan*((r*(1+r)**m)/((1+r)**m - 1))


### 为什么称Mortgage为base class？

它的属性和方法可以供每个子类使用，但是没有实例通过它直接初始化。也就是说，不会建立任何Mortgage类型的对象。


### 有没有读懂Mortgage这个例子的代码？

```python
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

```

运算输出

```commandline
Fixed, 7.0%
 Total payments = $479017
Fixed, 5.0%, 3.25 points
 Total payments = $393011
4.5% for 48 months, then 9.5%
 Total payments = $551444
```

以上，2018-04-19。
