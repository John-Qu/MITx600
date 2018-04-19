# 5 STRUCTURED TYPES, MUTABILITY, AND HIGHER-ORDER FUNCITONS

## 5.1 Tuples

### 为什么说tuples更像string，而不是list？

tuple和string都是

- 不可更改的
- 有序的
- 元素序列

tuple与string的区别仅仅在于

- tuple的元素可以是任何类型
- string的元素只可以是char

tuple与list的相同点

- 有序的
- 元素序列
- 元素可以是任何类型

tuple与list的区别在于

- tuple的元素不可变更
- list的元素可以变更

相比于元素类型，是否可变更这个属性更重要。

### 单个元素的tuple形式上怎么写？

为了与`(1)`区分，写成`(1,)`。

python的发明人说，`(1)`只是对整数1的废话描写，这了的括号是表达计算的先后顺序。加了逗号才是tuple的定义符号。

### tuple与多元素赋值相结合，用在哪里？

1 拆分绑定

```python
a, b, c = 'xyz'
```
2 函数返回值

调用函数是一个expression，只能evaluate成一个object，所以打包成tuple类型。

```python
...
def ...
    return (minVal, maxVal)
...
```

## 5.2 Ranges

### range只有一个参数时怎么理解？

当作stop，它不可缺省。

### range与tuple有什么异同？

同：都immutable。

异：range占用空间与长度无关，只由`start, stop, step所定义，只占很小的空间。

### range的应用场景？

最常用在`for`语句中。

```python
for i in range(3, 20, 5):
    ...
```

也可以用在其他需要整数序列的代码中。

## 5.3 List and Mutability

### list的`[]`可能有歧义吗？要紧吗？

式`[1,2,3,4][1:3][1]`中的`[]`分别是三个含义：

- 定义list
- 提取slice
- index元素

不要紧，因为通常情况下，list都是增量定义使用，很少有形式上一次定义完整。

### 两种equality？

- value equality `print(Univs == Univs1)`
- object equality`print(id(Univs) == id(Univs1))`

The sementics of Python says that no twe objects have the same identifier.

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fq8l0ee7ebj30i60ewdif.jpg)

### 什么是mutablity和side effect？

list的元素可以被改变，有时是被某个操作所改变，这种性质被称作是mutability。

并不是将改变之后的内容创建为一个新对象返回，而是直接更改原始对象，这种操作被称为有side effect。

`['MIT', 'Caltech'].append('RPI')`

而`+`就没有side effects，它会创建一个新list。

### 什么是aliasing别名使用？

同一个对象，有多个varialbe指向途径。

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fq8l7v3bh5j30pk0niwje.jpg)

### 这个程序为什么有semantic错误？

```python
def remove_duplicates(L1, L2):
    """Assumes that L1 and L2 are lists.
       Removes any element from L1 that also occurs in L2."""
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)


def test_remove_duplicates():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_duplicates(L1, L2)
    print("L1 =", L1)


test_remove_duplicates()
```

结果不是
```commandline
L1 = [3, 4])
```
而是
```commandline
L1 = [2, 3, 4])
```
因为`for e1 in L1`是按L[0] L[1] L[2] L[3]的顺序来提取L1中的元素，赋给e1。但是当L1的第一个元素被删除，2成为L[0]之后，for语句仍然提取L[1]，那是"3"。

怎么办呢？

给L1做个clone，让for语句从L1的不变clone里面提取元素。

有三种写法
- cloneL1 = L1[:]
- cloneL1 = list(L1)
- cloneL1 = copy.deepcopy(L1) 当L1中元素mutable，也需要clone的时候。

然后写

`for e1 in cloneL1:`

### 什么是list comprehension？

把list中的每个元素都做一个操作或者筛选，写在一句话里。

比如：

```python
L = [x**2 for x in range(1, 7)]
print(L)
mixed_list = [1, 2, 'a', 3, 4.0]
print([x**2 for x in mixed_list if type(x) == int])
```

### 为什么提倡慎用list comprehension这种聪明？

> in marvelous and subtle ways

别人还要读呢，"显得聪明"不是目的。

## 5.4 Functions as Objects

### function也是对象吗？

是头等对象，first-class objects。

有自己的类型`<type 'built-in_function_or_method'>`。

可以像其他类型一样，用在各种地方。

### function作为arguments有什么特别称呼？

higher-order programming

采用function作为arguments的函数，被称为higher-order，因为它的一个参数本身就是函数。

举个例子，类似与内置函数`map`

```python
import em_4_3_factorial
import em_4_3_fibonacci


def apply_to_each(l, f):
    """Assumes l is a list, f a function.
       Mutates l by replacing each element, e, of l by f(e)"""
    for i in range(len(l)):
        l[i] = f(l[i])


def test_apply_to_each():
    l = [1, -2, 3.33]
    print('l =', l)
    print('Apply abs to each element of l.')
    apply_to_each(l, abs)
    print('l =', l)
    print('Apply int to each element of l.')
    apply_to_each(l, int)
    print('l =', l)
    print('Apply factorial to each element of l.')
    apply_to_each(l, em_4_3_factorial.factRecursion)
    print('l =', l)
    print('Apply Fibonnaci to each element of l.')
    apply_to_each(l, em_4_3_fibonacci.fib)
    print('l =', l)

```

### lambda expression的用武之地？

作为高阶函数的argument，用lambda表达式，构建一个未命名函数。如下例所示。

```python
li = []
for i in map(lambda x, y: x**y, [1, 2, 3, 4], [3, 2, 1, 0]):
    li.append(i)
print(li)
```

结果是：
```commandline
[1, 4, 3, 1]
```

## 5.5 Strings, Tuples, Ranges, and Lists

### Strings, Tuples, Ranges, and Lists的异同之处

相同之处：都是有序集合，可以做下列操作。

```python
seq[i]
len(seq)
seq1 + seq2
n*seq
seq[start:end]
e in seq
e not in seq
for e in seq
```

类似与不同之处

| Type  | Type of elements |     Examples of literals     | Mutable |
| :---: | :--------------: | :--------------------------: | :-----: |
|  str  |    characters    |       `'', 'a', 'abc'`       |   No    |
| tuple |     any type     |    `(), (3,), ('abc', 4)`    |   No    |
| range |     integers     | `range(10), range(1, 10, 2)` |   No    |
| list  |     Any type     |    `[], [3], ["abc", 4]`     |   Yes   |

### list与tuple相比，各自优点？

list可以变更，方便追加元素。

tuple不可变更，就不必担心aliasing，还可以作为dict的key。

### string的好处？

虽然不像list和tuple那样灵活，但是有很多method处理string，让生活更美好。况且他们都没有side effect，他们都有返回值。

```python
s.count(s1)
s.find(s1) # return -1, if s1 not in s.
s.rfind(s1)
s.index(s1) # raise an exception, if s1 not in s.
s.rindex(s1)
s.lower()
s.replace(old, new)
s.rstrip()
s.split(d) # default with arbitary strings of whitespace characters.
```

## 5.6 Dictionaries

### dict与list有什么异同？

dict类似于list，values可以是任何类型。

dict通过keys索引，list通过index索引。

dict查找不需要遍历，与容量无关。

### dict的keys是hashtable type的对象，必须满足哪两点？

- 这个对象可以用__hash__方法映射到一个整数对象，在它的整个生命周期里，__hash__返回的值都不变。
- 这个对象可以用__eq__验证唯一性。

所有Python内置类型中，immutalbe都是hashtable，mutable都不是hashtable。

### d.keys() d.values()返回的是什么对象？

a view object, 是 dict_keys 和 dict_values类型。

动态的，原始对象变了，它也有所显示。

### 常用dict操作？

```python
len(d)
d.keys()
d.values()
k in d
d[k]
d.get(k, v) # returns d[k] if k in d, and v otherwise.
d[k] = v
del d[k]
for k in d
```