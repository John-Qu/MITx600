# 6 TESTING AND DEBUGGING

### 测试和改错是什么？

测试是一个过程，尝试和确认程序按照预定想法运行。

改错也是一个过程，尝试修好程序，当确认它没有按照预定想法运行时。

### 测试和改错都是写好程序后要做的过程吗？关键在哪里？

不是。

好的程序员从一开始就想怎么更容易地测试和改错。

关键点在于，把程序分解为独立部分，可以分别实现、测试和改错，不依靠其他部分。

### 为实现模块化modularizing，有什么机制？

写函数是一个，目前我们只知道这个。后续学了其他，再回头看这章。



## 6.1 Testing


### testing的目的是证明没有bug吗？

> Program testing can be used to show the presence of bugs, but never to show their absence! -- Edsger Dijkstra

> No amount of experimentation can prove me right; a single experiment can prove me wrong. -- Albert Einstein


### 做testing的关键是找到什么？

testing suite, that has a high likelihood of revealing bugs, yet does not take too long to run.


### 找到testing suite的关键是什么？

把输入的可能空间分区。space of all possible inputs. partitioning


### 做分区要保证什么？

原始集合的任意元素准会落在一个分区内。


### 找合适的分区容易吗？有什么途径？

说说容易，做起来难。

- 在specification里找启发，黑箱测试。
- 在code里找启发，玻璃测试。


### 黑箱测试有什么积极意义？

- 由于是两拨人做，避免了编程者的盲区也被带入测试。比如忽略负数输入。
- 鲁棒，不依赖于实现方式。


### 举一个黑箱测试的例子？考虑边界情况。

平方根的例子

```python
def sqrt:
    """Assumes x, epsilon floats
               x >= 0
               epsilon > 0
       Returns result such that        
               x - epsilon <= result*result <= x + epsilon"""
               
```

两个区间（x=0 x>0）还不够，还要测试边界情况（比如空数组），极小和极大的值。

测试用例

| x           | epsilon     | discrption         |
| ----------- | ----------- | ------------------ |
| 0.0         | 0.0001      | 等于零             |
| 25.0        | 0.0001      | 大于零，标准平方数 |
| 0.5         | 0.0001      | 小于1的数          |
| 2.0         | 0.0001      | 无理数结果         |
| 2.0         | 1.0/2.0**64 | 正常x，极小的e     |
| 1.0/2.0**64 | 1.0/2.0**64 | 极小x，极小e       |
| 2.0**64     | 1.0/2.0**64 | 极大x，极小e       |
| 1.0/2.0**64 | 2.0**64     | 极小x，极大e       |
| 2.0**64     | 2.0**64     | 极大x，极大e       |

极小e的情况下，预期不会有合理结果。

数组复制的例子

```python
def copy(l1, l2):
    """Assumes l1, l2 are lists
       Mutates l2 to be a copy of l1"""
    while len(l2) > 0:  # remove all elements from l2.
        l2.pop()  # remove last element of l2.
    for e in l1:  # append l1's elements to initially empty l2
        l2.append(e)


l1 = [1, 2, 3]
l2 = l1
copy(l1, l2)
print(l2)

```

如果没做这个测试`copy(l, l)`，就不能发现这个bug：
结果是`[]`


### 为什么要做玻璃箱测试？

- 知道测试什么情况才能提供更多信息。
- 评估黑箱测试是否完备。
  
比如这个验证素数的函数

```python
def is_prime(x):
    """Assumes x is a nonnegative int.
       Returns True if x is prime; False otherwise."""
    if x <= 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True
```

2被当作特殊情况对待，但是2应该是素数。


### 如何客观衡量测试是否完备？

有软件工具做这个事，考察"路径完备"。

但是每个路径都走到了，也不代表就对了。

```python
def abs(x):
    """Assumes x is an int.
       Returns x if x >= 0 and -x otherwise."""
    if x < -1:
        return -x
    else:
        return x
```

用`{2, -2}`就可以走遍两个路径，但是它不会体现这个bug：`abs(-1)`返回值是`-1`。


### 玻璃箱测试有哪些必要动作？

注意，不保证充分。

- 检查if的各个分支。
- 每个except从句都执行过。
- 对for循环，经历如下情况：
    - 没有进入循环；
    - 只循环一次；
    - 循环不只一次。
- 对while循环，经历如下情况：
    - 同for的三个要求。
    - 离开while的条件都经历到。
- 对递归函数，没有递归，递归一次，递归不只一次，经历这三种情况。


### 测试有哪两个阶段？

单元测试和综合测试。循环交替两个阶段。


### 为什么综合测试通常比单元测试难？

1 单元的功能明确，综合测试更难定义性能。

2 综合测试面对的代码更多，运行时间可能很长。


### 工业软件公司里哪个部门做什么测试？

SQA - software quality assurance通常独立于实现软件的人。

开发组做单元测试，QA做综合测试。


### 工业届的软件是手工测试吗？

自动化测试，设置好test driver和stubs(单元测试时)。


### test drivers自动化设置好什么？

- 准备环境。
- 启动程序。
- 存储结果。
- 检验结果。
- 准备报告。


### Stubs是什么？做什么？

Stubs是树桩、烟蒂、存根。计算机程序中，用stubs来模拟哪些还不存在的软件部分，甚至是硬件。程序员团队就可以开发和测试多个系统了。

理想情况下，stubs应该：

- 检验环境和输入的合理性。
- 调整arguments和global variable，满足specification。
- 给出符合specification的返回值。


### 做stubs为什么难？怎么办？

有的任务复杂，建一个stub，几乎等同于实现它的功能了。

回避这个难题有个办法：

- 限制stub能接受的arguments。
- 建一个表，对每种arguments组合，给输出值。


### 自动化测试给编程者什么帮助？

有助于regression testing。

> It is all too common to install a "fix" and breaks something that used to work.



## 6.2 Debugging


### "bug"这个词坊间传闻与历史沿革

坊间传闻，1947年9月9日的Mark II工作日志里，记录者抓到一只飞蛾，导致使用debugging这个词。
"First actual case of bug being found."可见bug早已是通用词了。至少在二战时，就用于电子系统问题。

1896年出版的电气工程手册，里面有bug词条。

英文中bugbear是anything causing seemingly needlessor excessive fear or anxiety.

哈姆雷特也曾经抱怨bugs and goblins in my life.


### bug这个词有什么误导意像？

bug可以动，自己飞进去的。

程序中的bugs都是人弄的，并不会自主移动。


### runtime bugs可以用哪两个维度分类？

公然的Overt - 隐蔽的Covert

总有Persistent - 时有Intermittent

- 公然、总有：最好。
- 隐蔽、时有：最坏。
- 公然、时有：**正确计算飞机航线，在大多数情况下** vs **在特定情况下，肯定计算失误** 哪个更危险？
- 隐蔽、总有：没有发现bug就发布了。比如受到信任的基金操盘软件，一朝犯错，上亿美元的损失。


### 什么是defensive programming？

写程序的时候，就想着让程序的错误公然显现，要有就总是有。

不要心存幻想，用发布程序来让bugs显现。那可能已经造成了无可挽回的损失。

> Developers can be under no illusion about the advisabilty of deploying the program.


### debugging可以学吗？

debugging是习得技能，没人天生就能做好。它可传授，也不难。

复杂系统的debugging技巧是相通的，比如计算机软件，实验室设备，生病的人。


### 有什么好用的debugging工具？

debugging工具开发了40年，其实帮助不大，重要的是你如何思考问题。很多有经验的人，干脆不费心在那上面了。

大多数程序员会说，最重要的debugging工具就是`print`了。


### 做好debugging的关键词是什么？

behavior - search - systematic

The key to being consistently good at debugging is being systematic in conducting the search for an explanation of the undesirable behaviors.


### 什么是systematic式的debugging？

1. 从研究数据开始
    - 程序——你其实并不理解程序
    - 输入数据
        - 造成问题的数据
        - 正常的数据
        - 二者为何有别
2. 形成假设——与所有数据表现一致
    - 具体的
    - 宽泛的
3. 可重复的实验——以便推翻假设
    - 事先想好如何解读各种可能结果
    - 事后落入"一厢情愿"的陷阱fall prey to wishful thinking
4. 做好记录——免得遭遇鬼打墙
    - insanity is doing the same thing, over and over again, but expecting different results.
    

### 如何设计debugging实验？

把debugging看作一个搜索过程，逐步缩小搜索范围。有两类做法。

1. 排除某段代码对造成错误的责任；
2. 逐渐减少测试数据量。


### 就是debug不出来怎么办？

遇到难题才是强者显身手的时候？
> When the going gets tough, the tough get going. - Joseph P. Kennedy

几个务实的pragmatic建议.

- 在经常可能犯错的地方找找看
    - 给函数的arguments放错了顺序；
    - 拼错了名字，比如大小写；
    - 重新初始化一个参数失败；
    - 比较两个浮点数是否相等，而不是比较二者差值是否足够小；
    - 比较两个对象是否数值相等，而不是id相等；
    - 忘记了有些built-in函数有side effect；
    - 忘记了`()`，造成只是引用了一个函数对象，而没有激活函数；
    - 创建了一个假名引用；
    - 其他正好是你常犯的错误。
- 别再追问它为什么不按你说的做，想想它为什么要那么做。
- Bug可能不在你认为的地方，否则你早就找到了不是？实用的方式是排除法，确认bug不可能在哪里。福尔摩斯说：排除其他，剩下的就是答案。
- 向别人解释问题，尤其是bug不可能在哪里，你的根据是什么。
- 别拿document和comment太当真，程序也许并不是那么走的。
- 暂停debugging，开始写documentation。有助于从另一个侧面看问题。
- 走开做别的，明天再来试。这是用时间换效率，前提是动手得早，还有时间。


### 找到bug就动手吗？要想想什么？

找到bug不容易，马上就动手，谁都有这个冲动。

我们的目的不是抓一个bug，而是快速有效地得到没有bug的程序，所以最好先想一想：

- 它能解释所有观察到的症状吗？或者它只是冰山一角。比如list被mutated，与其就地clone，不如全局都换成tuple。
- 做了这个fix动作，有什么连带影响？破坏了其他东西吗？导致过于复杂吗？有可能弄脏其他代码吗？
- 确保你能回到原点。
- 如果有很多解释不清的错误，最好考虑一下这个问题：一个一个debug还是明智之举吗？也许有更好的方式组织程序，也许有更容易的算法来正确实现功能。


以上，2018-04-13 15:40笔记。
