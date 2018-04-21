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

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/13.d10z.001.png)


### Python对List的表示方式体现什么计算机技术？

间接引用, indirection




### 






