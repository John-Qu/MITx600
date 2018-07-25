# 9 A SIMPLISTIC INTRODUCTION TO ALGORITHMIC COMPLEXITY


### 为什么关心计算复杂度？什么情况下关心程序效率？

程序正确当然第一重要。在正确的前提下，就要讲究性能。

有实时性要求：
- 飞机在碰到障碍前必须发出预警。
没有实时性要求，但是影响生活：
- 评价数据库系统，每分钟完成多少事。
- 智能手机app的启动时间。
- 生物学家的进化系统模拟。

### 要直来直去还是要程序效率？少想还是少做？这是个权衡。

> The most straightforward solution is often not the most efficient.

> Computational efficient algorithms often employ subtle tricks that make them difficult to understand. Consequently, programmers often increase the **conceptual complexity** of a program in an effect to reduce the **computational complexity**.

- 多想一点，少算一点。
- 多算一点没关系，可以少想一点。


### 为什么要找到衡量比较算法的方法？

让比较与权衡建立在一个sensible way上面。

权衡：
- 多想一点，还是，多算一点。
- 概念复杂性 vs 计算复杂性。


## 9.1 Thinking About Computational Complexity


### 用比较时间的办法评价计算复杂度可以吗？

测量程序运行时间受三方面因素影响：

- 运行程序的计算机性能；
- 计算机上Python系统的效率；
- 输入值。

而前两项与算法无关。测量时间不靠谱，得想办法绕过前两项。


### 比测量程序运行时间更抽象的方式是测量什么？

测量程序的基本步数。

随机存取机random access machine作为计算的模型。
- 一步一步顺序执行。
- 一步是一个基本动作：赋值、运算、比较、访问。

注意：对现代计算机的模拟应该是"并行"的随机存取机。但是这对分析算法复杂度没有够大的影响。


### 算法的实际运行时间依赖于输入值的什么？

算法的实际运行时间不仅依赖于输入规模，还依赖于具体的输入值。

```python
def linearSearch(L, x):
   for e in L:
      if e == x:
         return True
   return False
```

- best-case，常量。
- worst-case, 正比于len(L)，与输入规模成线性关系。
- average-case，要考虑进来先验信息（priori information）计算平均值。


### 各种输入值可能性，为什么聚焦在最坏情形？

所有工程师都相信墨菲定律：如果事情可能出错，那它就一定会出错。（很小的出错概率 x 无限大的输入集合 = 肯定出错）

最差情形给出了运行时间的上界。
- 飞机改变航向规避碰撞，至少需要这么多时间，最坏的情况也不能超过它。


### 考察一个算法的步数时，为什么可以忽略加法项？

n很大时，固定的加法项就微不足道了。

而我们总是要考虑n很大的情况。

### 比较不同算法时，为什么可以忽略乘法常数项？

乘法常数项来自于循环内部一次走多少步。

当两种不同算法，循环的次数相差很多时，一次循环相差多少就不重要了。

例如，squareRootExhaustive(100, 0.0001)大概需要while循环的10亿次迭代才能求出结果。

相反，squareRootBi(100, 0.0001)只需20次稍微复杂的while循环迭代就可以求出结果。


## 9.2 Asymptotic Notation

### 为什么用渐近表示法？

对于规模较小的输入，几乎所有算法都足够高效，所以通常对于规模特别大的输入，我们才会担心算法的效率，这是我们研究算法复杂度的基本动机。

作为一种对“特别大”的表示方法，渐近表示法描述了输入规模趋近于无穷大时的算法复杂度。

### 可以用哪两条规则描述算法的渐近复杂度，为什么？

- 如果运行时间是一个多项式的和，那么保留增长速度最快的项，去掉其他各项；
    - 当输入规模足够大，只有增长最快的项占用绝大多数的步数。
- 如果剩下的项是个乘积，那么去掉所有常数。
    - 乘法常数项并不影响量级，无关于本质，不影响决策（是否应该找更好的算法）。
    

### Big O notation是什么意思？

大O表示法可以给出一个函数渐近增长（通常称为增长级数）的上界。例如，从渐近的意义上说，公式f(x)∈O(x2)表示函数f的增长不会快于二次多项式x2。

注意是 上界。


### 怎样明确地使用in和be O(x2)？

f(x) in O(x2) i.e. f(x)∈O(x2)  

- 函数f的增长不会快于二次多项式x2。
- 在最差情形下，f会运行O(x2)步。
- f的最差情形运行时间也可以明显小于O(x2)。

f(x) is O(x2) i.e. f(x)∈Θ(x2)

- 在暗示x2既是渐近最差情形运行时间的上界，也是其下界。
- 这被称为紧界tight bound。
- 不理解。


## 9.3 Some Important Complexity Classes

### 常用的大O表示法实例

- O(1)表示常数运行时间。
- O(logn)表示对数运行时间。
- O(n)表示线性运行时间。
- O(n logn)表示对数线性运行时间。
- O(n^k)表示多项式运行时间，注意k是常数。
- O(c^n)表示指数运行时间，这时常数c为底数，复杂度为c的n次方。


### 常数复杂度的代码没有意义吗？一定没有迭代或循环吗？

不是没意义，是没意思。few interesting programs

还是有意义，比如单纯的算list长度，简单代数运算。

也可以有迭代循环，只是与输入规模无关。


### 有序数列的二分查找算法的复杂度在O(logn)内，怎么推得？

list有n个元素，经过t次1/2，取值空间里只剩一个元素。

n * (1/2)**t = 1

t = log2(n)


### 为什么不用关心对数复杂度里的对数的底？

换底公式。

O(log2(x)) = O(log2(10)*log10(x))

那只是一个常数乘积因子。


### 下面intToStr为什么是对数复杂度？

```python
def intToStr(i):
   """假设i是非负整数
      返回一个表示i的十进制字符串"""
   digits = '0123456789'
   if i == 0:
      return '0'
   result = ''
   while i > 0:
      result = digits[i%10] + result
      i = i//10
   return result
```

10**t ~= x

t in O(log10(x))


### 处理序列的操作为什么一般具有线性复杂度？

它们对序列中的每个元素都进行常数（大于0）次处理。


### 为什么人们很少关注算法的空间占用情况？

因为看不见，感受不明显。


### 对数线性复杂度的例子？

归并排序法。参见吴军·谷歌方法论058

全世界所有的算法专家经过了十多年，终于发现从经验出发的排序速度慢的原因，就是做了无数的无用功。要提高效率，就需要让计算机少做事情。

以冒泡排序为例，之所以慢，是因为每一次选出一个最大的数，都要和其它所有的数字相比，其实并不需要这么麻烦，要想提高效率，就要减少数据之间的相互比较。最早对冒泡排序的改进是一种叫做归并排序的算法，它就利用了少做事情的思想，归并排序的思想大致如下：

首先，科学家们发现，如果我们把全班同学分成两组，分别排序，那么从每一组中挑选出一个最大的，就能省去一半的相互比较时间。于是他们就先将整个班级一分为二，先分别进行排序，再把两个排好序的组，合并成为一个有序的序列。相比排序，对有序的序列合并是很快的。归并排序这个词就是这么来的。这样做大约可以节省一半时间。当然，我们在前面也讲过，节省一半时间意义不大，但是别着急，因为对一个班级分出来的两个小组，排序时也可以采用上述技巧。

第二步，就是对两个组的排序。显然我们不应该再用冒泡排序。聪明一点的人马上会想到，既然能分成两组，就能把每个小组再分为两组，即分成四组，重复上面的算法，分别排序再合并。这样就能省3/4的时间。

再接下来，四组可以分为八组，能省7/8的时间，八组可以分为十六组，时间就不断省得越来越多。分到最后每个小组只剩下两个人的时候，其实就不用排序了，只要比较一次大小即可。

这种方法其实可以理解为两个过程，先是自顶向下细分，再自底向上合并。那么这种算法的复杂度等于多少呢？它相当于N乘以log（N），log（N）就是N的对数函数，大家不必在意N乘以log（N）是什么东西，只要记住它和N平方不一样，而且这个复杂度比前面的N平方小很多就行了。

为了便于你理解它小了多少，我们看看当N分别是100，1万，1百万，1亿时，两种算法的复杂度的情形：

第一种：即N平方，当N是100，1万，1百万，1亿时，它对应1万，1亿，1万亿，1亿亿。

第二种：即N乘以log（N），它对应700，13万，2000万，23亿。

你可以看出N比较大了以后，N乘以log（N）比N平方要小很多，即23亿和1亿亿的差别，相差大约400万倍。400万是什么概念呢？大约是一支毛笔的长度和北京到上海距离的差别，或者是你和我两个人的重量和瓦良格号航空母舰重量的差别。


### 多项式复杂度的例子多是循环嵌套？

是的。

两层循环嵌套的例子
```python
def isSubset(L1, L2):     # O(len(L1))*O(len(L2))
   """假设L1和L2是列表。
      如果L1中的每个元素也在L2中出现，则返回True
      否则返回False。"""
   for e1 in L1:           # O(len(L1))
      matched = False
      for e2 in L2:        # O(len(L2))
         if e1 == e2:
            matched = True
            break
      if not matched:
         return False
   return True
```

注意在数组中查找也是循环。
```python
def intersect(L1, L2):
   """假设L1和L2是列表
      返回一个不重复的列表，为L1和L2的交集"""
   #建立一个包含相同元素的列表
   tmp = []
   for e1 in L1:         # O(len(L1))
      for e2 in L2:      # O(len(L2))
         if e1 == e2:
            tmp.append(e1)
            break
   #建立一个不重复的列表
   result = []
   for e in tmp:        # O(len(tmp))
      if e not in result:   # O(len(result))
         result.append(e)
   return result
```
O(len(L1))*O(len(L2)) + O(len(tmp))*O(len(result))

tmp是L1与L2的交集，肯定比L1和L2中最短的还短；result又是tmp的子集。

在
O(len(tmp))*O(len(result)) < O(len(L1))*O(len(L2)) 
的比较中，前者可以忽略。

这个函数整体的计算复杂度为O(len(L1)*len(L2)) 


### 一个指数复杂度的例子？

```python
def getBinaryRep(n, numDigits): # O(log2(n))
   """假设n和numDigits为非负整数
      返回一个长度为numDigits的字符串，为n的二进制表示"""
   result = ''
   while n > 0:
      result = str(n%2) + result
      n = n//2
   if len(result) > numDigits:
      raise ValueError('not enough digits')
   for i in range(numDigits - len(result)):
      result = '0' + result
   return result

def genPowerset(L): # O(2**len(L))*O(len(L))
   """假设L是列表
      返回一个列表，包含L中元素所有可能的集合。例如，如果
      L=[1, 2]，则返回的列表包含元素[1]、[2]和[1, 2]"""
   powerset = []
   for i in range(0, 2**len(L)): # O(2**len(L))区分先后的组合
      binStr = getBinaryRep(i, len(L))
      subset = []
      for j in range(len(L)): # O(len(L))
         if binStr[j] == '1':
            subset.append(L[j])
      powerset.append(subset)
   return powerset
```

Subtle在哪里？
- 所有子集 == 遍历所有二进制数
- 用01做旗帜。
- 填补空0。


### 本质上就是指数复杂度的难问题，就一定无解了吗？

- 想办法求近似解
- 特殊情况可以求完美解。


### 怎么理解几种计算复杂度的曲线对比图？

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/12.d09z.001.png)

- 对数增长很慢。（它的逆函数指数增长很快）
- 线性比对数增长快太多。

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/12.d09z.002.png)

- 对数线性比线性要快，但是也差不太多。
- 平方已经比对数线性快太多，立方就更不用提了。

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/12.d09z.003.png)

- 平方贴着下边框，指数贴着右边框，说说为什么。
- 对数坐标可以这么写。如果写成2 4 6 8...，它是log10(y)/11。

---
以上，2018-04-20记。

以下，2018-06-27记。

---


