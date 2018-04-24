# 10 SOME SIMPLE ALGORITHMS AND DATA STRUCTURES


### 上一章的目的不是让你设计高效程序，这一章的目的也不是设计厉害的算法，现实一点的目的是什么？

上一章的目的：介绍分析复杂性需要用到的基本概念。

这一章的目的：to develop some general intuitions about how to approach questions of efficiency.


### 傻傻的算法就不好吗？

简单直白、肯定正确的算法，常常是较好的路。搞什么聪明算法，可能是浪费时间。

simple and obviously correct.


### 为什么在第二章讲了穷举法、二分法和N-R切线法？

重点是想传达这样的认识：程序效率的关键在于算法高下，而不在于编码技巧。

The major point was that the key to efficiency is a good algorithm, not clever coding tricks.


### 科学工作者写程序的经验过程要走哪两步？

- 先写个简单的算法，用小数据集运行，验证假设。
- 结果积极的话。
- 再写高效算法，在大数据集上反复运行。


### 学习算法的目标是有朝一日发明算法吗？

大科学家一辈子有一次机会就很幸运了。

波利亚的观点类似：理解问题，拆解问题，等价问题。

> to learn to reduce the most complex aspects of the problems we are faced with to previously solved problems.

- 理解问题内在的复杂性在哪里；
- 想办法把问题分解为子问题；
- 帮这些子问题，找到对应的伙伴，后者已经有高效的算法可以解决。


### 对于算法，工程上实际的态度是怎样的？

> Keep in mind that the most efficient algorithm is not always the algorithm of choice.

并不总是在每处选择最高效的算法，因为那样的程序很难懂，没有必要搞得那么难懂needlessly difficult to understand。

实际的好策略是：
- 先用最直截了当的方式解题，
- 然后调试instrument程序，
- 发现计算不顺的瓶颈，
- 找出改善该处复杂度的办法。
- 依此往复改良。


## 10.1 Search Algorithms


### 什么是搜索算法？

一种寻找的方法

- 在哪里搜？搜索空间 search space，collection of items
- 搜什么？一个或一组元素, an item or group of items
- 依据什么？特征属性，with specific propertities


### 搜索空间一定是具体的吗？

具体：电子病例

抽象：整数集


### 说`e in li`的算法复杂度"至好"是线性的逻辑是什么？

```python
for i in range(len(L)):
    if L[i] == e:
        return True
return False
```

- 最坏输入数据情况下，e不在L里，执行O(len(L))次测试。
- 各次测试都是常数时间吗？如果是，那么才可以说复杂度与len(L)是线性关系。
- 各次测试分为找到Li与比较。
- 元素比较是常数时间。
- 找到各个L[i]是常数时间吗？
- 我们默认系统找到对应地址的内容（从某个地址里提取元素）这个动作是常数时间。
- 那么问题简化为：Python能否在常数时间内计算出下一个元素的地址。


### Python怎样实现在常数时间里顺序索引元素？

先假想一个理想情况：
- 一个list，每个元素都是int。
- 在内存中顺序存储。
- 因为每个整数是1字长byte占4个或8个字节bit（32位处理器或64位，硬件决定）
- 计算索引地址：start+4*i

真实情况类似：列表的表现方式是"长度+指针1+指针2+..."
- 指针就是固定长度的，有的32位，有的64位。
- 指针所指向的地址里，才是任意类型的元素。
- 计算索引地址：start+4+4*i。

![ @列表的实现方式 | center | 600x0 ](http://www.ituring.com.cn/figures/2017/PythonIntroduction/13.d10z.001.png)


### Python对List的表示方式体现什么计算机技术？

间接引用, indirection不直接：想要接触一个东西，先接触另一个东西，后者包含引用前者。

上面的写法有点生硬，我是不是可以翻译成下面这样。

托关系：不直接递红包，找认识人，建立信任保留回旋余地。

1950年代开始，计算机科学家发现，这种方法可以解开很多问题。

用variable与index都是indirection的方式之一。


### 在集合中查找元素至少是线性复杂度吗？

一般来说，O(len(L))是最好的程度，因为必须遍历每个元素。

但是如果有附加信息，可以做的更快。

比如：集合中的元素排列有序，比如说升序排列。

- 从头开找，直到发现比e大的元素，就可以结束查找比较了，因为后面的元素也必定比e大，没有必要继续了。
    - 它可以改善平均运行时间；
    - 而不能改善最坏情况。
- 用二分查找，每次缩小一半可能空间。
    - 可以改善最坏情况。
    

### 二分查找建立在什么假设的基础上？

可能空间有序。
- 实数空间天然全盘有序。比如求平方根的算法。
- 在specification里要求函数调用者承担保证list集合有序的责任。
    - 可以在函数内校验实际参数给的集合是否有序；
    - 但是校验有序性的动作，是O(len(L))复杂度，失去用二分法降低复杂度的意义了。
    

### 干嘛要在search函数内还写函数？结果架空了search函数。

search函数是wrapper包装 function，bSearch是helper辅助 function。

因为bSearch的形式参数low，high只是实现方式，应该对使用者隐藏。


### 在bSearch这个递归函数里，递减函数有什么性质？在哪里体现？

类似于while循环的递减函数，这里：

1. 把行参对应的值映射为一个非负整数；
2. 这个值为0，递归结束；
3. 递减函数的值随着每次递归都减小。

```python
def search(L, e):
    """假设L是列表，其中元素按升序排列。
       如果e是L中的元素，则返回True，否则返回False"""

    def bSearch(L, e, low, high):
        #Decrements high - low
        if high == low: # 这里保证递减函数性质2，到0停止递归。
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #整数除法向下取整，m可能等于l，而不可能等于h，所以最后else：L[mid] < e的分支里，不用写if了。
                return False
            else:
                return bSearch(L, e, low, mid - 1) # 递减函数性质3，递减。
        else:
            return bSearch(L, e, mid + 1, high) # 递减函数性质3，递减。

    if len(L) == 0: # 这里保证递减函数的性质1，非负。
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)
```


### 在bSearch的后半递归函数里，为什么要写mid+1？

保证能够踩到递减函数为0的点，结束递归。仅此而已？仅此而已就不简单。

如果不做-1和+1，看个实例
```python
L = [0 1 2 3 4 5]
e = 2.5

1.
l = 0, h = 5
m = (0 + 5)//2 i.e 2
L[m=2] = 2 < e=2.5

2.
l = 2, h = 5
m = 3
L[m=3] = 3 > e=2.5

3.
l = 2, h = 3
m = 2
L[m=2] = 2 < e=2.5

4.
l = 2, h = 3
与上步相同，死循环。。。
```

可见，由于求m值的//向下取整，m可能等于l，如果在下一轮递归时m不加1，就会陷入死循环。

---
但是前半递归函数的上限参数mid-1就没有那么复杂。
e在【L[low]，L[mid]）区间内，那么下一轮检验空间就可以写成L[low:mid],实际上末尾元素的index就是mid-1。


```python
def search(L, e):
    """假设L是列表，其中元素按升序排列。
       如果e是L中的元素，则返回True，否则返回False"""

    def bSearch(L, e, low, high):
        #Decrements high - low
        if high == low: # 这里保证递减函数性质2，到0停止递归。
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #整数除法向下取整，m可能等于l，而不可能等于h，所以最后else：L[mid] < e的分支里，不用写if了。
                return False
            else:
                return bSearch(L, e, low, mid - 1) # 递减函数性质3，递减。
        else:
            return bSearch(L, e, mid + 1, high) # 递减函数性质3，递减。

    if len(L) == 0: # 这里保证递减函数的性质1，非负。
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)
```


## 10.2 Sorting Algorithms


### 为什么要费事做排序？

排序之后可以用更简单的搜索算法，前提是：

(排序+二分查找)比(直接查找)节省。

sortComplexity(L) + log(len(L))  <  len(L)

但是，排序不可能比len(L)还小，因为至少要遍历各个元素。

如果查找很多次呢？

sortComplexity(L) + k*log(len(L)) 小于 k*len(L)呢？

可以分摊成本。
> It might make sense to pay the overhead of sorting the list once, and then **amortize** the cost of the sort over many searches.


### 选择排序的工作原理是什么？

维持一个循环不变量/式，loop invariant，满足：
- 列表分成前缀部分prefix（`L[:i]`）和后缀部分suffix（L[i+1:]）；
- 前缀部分已经排好序；
- 前缀的每一个元素都不大于后缀部分中的最小元素。

```python
def selSort(L):
    """假设L是列表，其中的元素可以用>进行比较。
         compared using >.
       对L进行升序排列"""
    suffixStart = 0
    while suffixStart != len(L):
        #检查后缀集合中的每个元素
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #交换元素位置
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
```
归纳法可证上述代码能够保证循环不变式。


### 分而治之算法的特征是什么？

1. 递归基本情况。达到这个规模就好处理了，就不用再分化了。
2. 拆分的子问题的规模和数量。规模越小，数量越多。
3. 有办法合并子问题的解。


### 怎么描述归并排序的递归算法？

1. 如果列表的长度是0或者1，那么它就不用排序了。
2. 如果列表的长度大于1（至少是2），那就将其分成两个列表，分别用归并排序处理。
3. 逐级合并排序好的结果。


### 为什么冯诺伊曼发现归并排序更快更好？

关键发现是：两个排好序的列表可以高效地合并为一个列表。

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fqmn7h5lk8j315q0f0tbp.jpg)


比较的次数是O(len(L))，这里的L是两个列表中较长的那个。复制操作的次数是O(len(L1) + len(L2))，因为每个元素都正好复制一次。


### 归并排序算法的实现? 其计算复杂度分析？

```python
def merge(left, right, compare):
    """假设left和right是两个有序列表，compare定义了一种元素排序规则。
       返回一个新的有序列表（按照compare定义的顺序），其中包含与
        （left+right）相同的元素。"""

    result = []
    i,j = 0, 0
    # 两两比较，复制走一个，移动一个index而已。
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 谁还有元素，就复制谁。        
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def mergeSort(L, compare = lambda x, y: x < y):
    """假设L是列表，compare定义了L中元素的排序规则（默认小于号）
       返回一个新的具有L中相同元素的有序列表。"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
```

一个len(L)的列表，被分割log(len(L))次，每次合并的复杂度至多是O(len(L))，所以mergeSort的时间复杂度是O(n*log(n))。


### 归并排序与选择排序相比的优缺点？

优点是快。1万个元素，一个是1亿，一个是13万。

缺点是占用空间。每次合并都需要复制一份，而选择排序只需要一个位子。


### 快速排序有什么特点？

1960年代Hoare提出。

运行时间不确定，依赖于被排序列表中元素的相对顺序。最坏情况下的运行时间是O(n^2)，但是期望运行时间是O(n*log(n))，与归并排序相同。

空间复杂度低，只需要log(n)大小的额外空间。


### Python现在用的排序算法是什么？

timsort，由Tim Peters在2002年提出。最坏情况下，时间复杂度与归并排序相同，但是平均情况下，相当好。performs considerably better.


### Python的两个排序函数怎么用？

list.sort(key = ?, reverse = ?)
sorted_keys = sorted(dict, key = ?, reverse = ?)


## 10.3 Hash Tables


### 在n个元素的数据集里搜索出k个元素，如果允许做一下预处理，比如先用归并排序，我们能做到的最好情况就是O(n*log(n))+k*O(log(n))吗？

不是。还可以把数据存成字典，检索时间与n无关。


### dict用什么技术实现检索时间与n无关？

a technique called hashing，散列技术。

- hash table，散列表。一个列表list。用index找到元素，是常数时间。
- hash function，散列函数。把key转换为hash table这个list的index值。
- hash bucket，散列桶。作为散列表list的一个元素，本身是一个列表list。多个元素落入同一个hash bucket的话，添加作为此list的元素。


### 为什么称为散列表table？

纵向是可以通过hash function算出index值的hash buckets，横向是在每个hash bucket内的重合collision元素。

形式类似：

```commandline
The buckets are:
  []
  [(99740, 6), (61898, 8)]
  [(15455, 4)]
  []
  [(99913, 18), (276, 19)]
  []
  []
  [(63944, 13), (79618, 17)]
  [(51093, 15)]
  [(8271, 2), (3715, 14)]
  [(74606, 1), (33432, 3), (58915, 7)]
  [(12302, 12), (56723, 16)]
  []
  [(27519, 11)]
  [(64937, 5), (85405, 9), (49756, 10)]
  []
  [(17611, 0)]
```


### 解读用`%`作为散列函数的一个例子代码。

```python
class intDict(object):
    """键为整数的字典"""

    def __init__(self, numBuckets):
        """创建一个空字典"""
        
        #numBuckets是散列桶的数量，是一个整数，跟dict元素数量相关。
        # 不能太小，太小了容易重合得多，降低时间效率；
        # 也不能太他，太大了空list多，降低空间效率。
        
        #先把hash table这个空楼房搭起来
        self.buckets = []
        
        #盖numBuckets层。
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])


    def addEntry(self, key, dictVal):
        """假设key是整数。添加一个字典条目。"""
        
        #hashBucket是一个列表，是hash talbe这个楼房的某一层。
        #求余%，多大的数，都映射到[0～numBuckets)区间内的整数
        hashBucket = self.buckets[key%self.numBuckets]
        
        #确认在本层里有没有这个key，有则替换，没有就什么都没干。
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i] = (key, dictVal)
                return
                
        #确认过没有这个key，没有return，会执下面的追加动作。   
        hashBucket.append((key, dictVal))


    def getValue(self, key):
        """假设key是整数。
           返回键为key的字典值"""
        
        #先通过hash function换算出楼层号   
        hashBucket = self.buckets[key%self.numBuckets]
        
        #再搜寻此楼层的各个房间，有则告知，无则None
        for e in hashBucket:
           if e[0] == key:
               return e[1]
        return None
        

    def __str__(self):
        """构造成字典的字面样子。"""
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}' #result[:-1] omits the last comma
```


### 怎样减少collision？

让hash function的many-to-one mapping做到各各输出值的机会均等，充分利用各楼层。

uniform distribution


### 被hash function映射到同一楼层怎么办？

楼层有房间，顺序排进去。


### dict中的元素真的没有顺序吗？

有顺序，可以按照楼层号和房间顺序打印。

但是突破了abstraction barrier，严重违反information hiding。


### 在dict中搜索的时间复杂度分析？

把key通过hash function找到楼层号，是O(1)，在楼层内搜索元素，是O(层内房间数)。所以，楼层越多，重合越少，越接近O(1)。

trade space for time.

如何取舍？


---
以上，2018-04-24