# 4 FUNCTION, SCOPING, AND ABSTRACTION

### 只有分支与循环的程序能做什么？

理论上说，它图灵完备，能做所有可计算的题目了。

### 只有分支与循环的程序有什么不足？

缺乏通用性和代码重用性。

为什么？以二分法求平方根为例。

``` python
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
```

- 依赖于初始值`x`, `epsilon`。每次使用都得重新复制粘贴，也许还得改一下变量名字。这就难以使用在某些更复杂的计算中。
- 算立方根，算二次方程的双根，相同相似的代码段多次多处重复：
    - 代码越多可能出错越多；
    - 难维护，改一处漏其他。

### 通用和重用代码的手段之一是？

函数，最重要的手段。

## 4.1 Functions and Scoping

### Function这个称呼与数学中的function一样吗？

Programming里的function比数学中的定义更广。

从1950s的Fortran 2开始。

### 在function定义格式中的名称？

- formal parameters
- actual parameters, arguments
- function invocation, function call (is an expression)
- return, None
- point of execution

### lambda abstraction是什么意思？

函数代码不操作特定对象，而允许函数使用者选择任何对象，作为实际参数。

### 函数的arguments有几种给法？

两种。

- positional
- keyword arguments，可以不顾先后顺序，可以给缺省默认值。

### 使用keyword arguments时注意什么格式？

定义函数时，formal parameters里把keyword arguments放在后面。

调用函数时，actual parameters用keyword arguments虽然可以不顾先后，但是ka不能出现在posisional arguments之前。

### symbol table做什么事情?

跟踪记录在这个层次上的变量名和他们的绑定对象。

> keeps tracks of all names defined at that level and their current bendings.

### 什么是stack frame？

一种通俗称呼。

当一个函数被调用时，它会创建一个新的symbol table，通常被叫做stack frame，因为是末进先出，类似stack of trays.

在函数返回后，这个stack frame就消失了，popped off，像气泡破掉。

### 给一个stack frame分析的例子？

``` python
def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    def h():
        z = x
        print('z =', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x =', x)
    return g
    
x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()
```
![](https://ws4.sinaimg.cn/large/006tKfTcgy1fq6dikygh0j30ru0h8417.jpg)

- 一列是一个时态。
- 越下级，越基础。
- 从顶部开始气泡破掉。

## 4.2 Specifications

### 为什么要写测试函数？

值得投资
> Tesf function seems to be a waste of effort, but an investment in writing testing code often pays big dividends股息.

- 不必反复在shell里敲数据来测试；
- 迫使自己思考，什么测试最能凸显问题。

### Specification是什么，包含什么？

一个合同，函数实现者与使用者（顾客）之间的合同。

它包含两方面：

- 假设Assumption。要求顾客保证提供这样的输入。
- 保证Guarrantee。承诺提供给顾客这样的结果。

### Specification对软件工程师哪两方面帮助？

without worrying unduly about

- what the other programmmers on the team were doing;
- how that module is to be implemented.

### 怎样理解Function对编程方式的帮助？

Function创造了计算用的元素。我们可以把它看作原初物质。

从两个方面有帮助：

- Decomposition creates structure. 程序分解成独立的小块，可以重复使用。
- Abstraction hides detail. 黑箱内部：看不到，不必看，应该不想看。

### Abstraction有什么意义？

它是真正的编程艺术。

为什么？

Abstraction的核心，是保留特定语境中的相关信息，而隐去不相关的东西。
但什么才是相关，这个概念的把握，就是艺术了。

> "Where ignorance is bliss, 'tis folly to be wise." - Thomas Gray

遗忘——不理解。

多对一 *many-to-one* 的过程——不理解。

### docstring通常包含哪些内容？

举个例子：

``` python
def findRoot(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
            epsilon > 0 & power >= 1
       Returns float y such that y**power is within epsilon of x.
            If such a float does not exist, it returns None."""
```

## 4.3 Recursion

### 会Recursion很牛逼吗？

> You may heard of recursion, and in all likelihood think of it as a rather subtle programming technique. That's a charming urban legend spread by computer scientists to make people think that we are smarter than we really are.

NOT so subtle. (a robust and subtle mind)

### Recursion的逻辑构成？

两部分：

- base case，直接指定答案。
- recursive(inductive) case, 问题的答案定义在另一个问题的基础上，它与原问题类似，但是换了另一组输入。

举个例子
To be natural born American citizen.

### 自然数natural numbers的定义是什么？如何明确使用？

- positive integer, or
- nonnegative integer.

不要直接用natural numbers的说法，那可能有不同的理解。明说explicit：`n an int > 0`。

### 阶乘的定义和两种代码实现方法？

factorial function's 
classic inductive definition:

- 1! = 1
- (n+1)! = (n+1)*n!

``` python
def factIteration(n):
   """Assumes n an int > 0
      Returns n!"""
   result = 1
   while n >= 1:
       result = result * n
       n -= 1
   return result
```

``` python
def factRecursion(n):
   """Assumes n an int > 0
      Returns n!"""
   if n == 1:
       return 1
   else:
       return n*factRecursion(n-1)
```

### 佩波那契数列是他发明的吗？

佩波那契Fibonacci是把印度和阿拉伯数学介绍到欧洲的人，这个问题不是他发明的。印度-阿拉伯数字和十进制，就是在他的著作中引入欧洲的。


### 怎样用语言描述佩波那契的兔子？

神奇的兔子。

- 一公一母两只刚出生的小兔子。
- 一个月后性成熟，可以交配。
- 怀孕一个月，生出一公一母两只小兔子。
- 兔子不死，从第二月性成熟之后，就可以每月产下一公一母两只小兔子。

问：母兔子的数量规律？


### 实现佩波那契数列的算法，有哪三部曲？那步最简单？

1 列出前面几个数，看规律；
2 从规律中发现背后的原理；
3 把原理写成代码。

第三步写代码最简单。把模糊的问题，提炼成抽象的答案，这最难。

| Month | Females |
| :---: | :-----: |
|   0   |    1    |
|   1   |    1    |
|   2   |    2    |
|   3   |    3    |
|   4   |    5    |
|   5   |    8    |
|   6   |    13   |

发现规律：前两个数之和等于本数

解释：本月的母兔子 = 一个月前的母兔子都活着 + 两个月前的母兔子都生了小母兔子

```python
def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
```

### Test a str是否回文palindrome的程序怎么写？程序中体现了什么思想？哪里体现出来的？

```python
def isPalindrome(s):
    """Assumes s is a str
       Returns True if letters in s form a palindrome; False otherwise.
           Non-letters and capitalization are ignored."""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters += c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1]) # short-circuit evaluation is not relevant here
    
    return isPal(toChars(s))
```

分而治之，divide-and-conquer
- 子问题更容易解决
- 子问题的解的集合可以综合出原问题的解

历史上的例子
- 凯撒
- 英国统治印度
- 富兰克林签署独立宣言时说：We must hang together, or assurely we shall all hang seperatedly.

这里的代码
- 比较头尾两个字符`s[0] == s[-1] `
- 验证更小的字符串`isPal(s[1:-1]) `
- 用`and`把二者和为整体


### TestPalindrome的测试程序怎么写？

```python
def isPalindrome(s):
    """Assumes s is a str
       Returns True if letters in s form a palindrome; False otherwise.
           Non-letters and capitalization are ignored."""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters += c
        return letters

    def isPal(s):
        print('  isPal called with', s)
        if len(s) <= 1:
            print('  About to return True from base case')
            return True
        else:
            answer = s[0] == s[-1] and isPal(s[1:-1]) 
            # short-circuit evaluation is not relevant here
            print('  About to return', answer, 'for', s)
            return answer

    return isPal(toChars(s))

def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrome("dogGod"))
    print('Try doGood')
    print(isPalindrome("doGood"))

testIsPalindrome()
```

输出

```commandline
$ python3 4-3-2-Palindrome.py 
Try dogGod
  isPal called with doggod
  isPal called with oggo
  isPal called with gg
  isPal called with 
  About to return True from base case
  About to return True for gg
  About to return True for oggo
  About to return True for doggod
True
Try doGood
  isPal called with dogood
  isPal called with ogoo
  isPal called with go
  About to return False for go
  About to return False for ogoo
  About to return False for dogood
False
```

## 4.4 Global Variables

### 为什么要求慎用全局变量？

> It is with some trepidation that we introduce the topic of global variables. Since the 1970s, card-carrying computer scientists have inveighed against them.

程序可读 <= 一次只读一块 <= 上下文环境必要信息少 <= 局部性locality

## 4.5 Modules

### 用modules有什么好处？

- 避免一个文件过大。
- 类似的定义放在一个文件里。
- 减少多人更新同一个文件的可能性。
- 有效避免变量名冲突。

### 全import有什么不好？为什么反对？

```python
from module import *
```

- 引入了module.py中所有的bindings，除了mudule本身，所以不能写`module.functionName()`。
- 大多数时候引入Module，并不熟悉它所有的变量定义，有可能造成命名冲突。
- 虽然不用写`module.functionName()`之类，但是程序可读性差，不清楚函数在哪里定义的。

### 在module里只有函数定义吗？也有可执行的陈述吗？

可执行的陈述用于初始化module，比如定义`pi = 3.14159`。

注意module只在shell启动时被引入一次，修改module文件，并不会改变运行结果。需要新开一个shell。

### 在哪里找Python的modules？

官网https://docs.python.org/3/library/。

## 4.6 Files

### 怎样不打印隔行？

```python
for line in nameHandle:
    print(line[:-1])
```

### 为什么要注意关闭文件手柄？

因为打开文件手柄时给予的权限不同。读`r`，写`w`，续`a`，不能混用。

### 文件的常用操作怎么写？

```python
fh = open(fn, `w`)
fh = open(fn, `r`)
fh = open(fn, `a`)
strContent = fh.read()
nextLine = fh.readline()
listOfLines = fh.readlines()
fh.write(s)
fh.writeLines(S)
fh.close()
```

以上，2018-04-11。