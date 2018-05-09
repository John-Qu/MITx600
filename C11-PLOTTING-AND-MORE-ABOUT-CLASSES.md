# 11 PLOTTING AND MORE ABOUT CLASSES


### 图形的有很大意义吗？为什么很多程序都用语言输出？

一张图可以表达很多意思。中国有这个谚语，一图胜千言？

非不想也，实不便也。

在Python生态里，很幸运，可以方便画图。


## 11.1 Plotting using Pylab


### pylab的官方资源？

PyLab绘图能力的完整用户指南参见
https://matplotlib.org/users/index.html

完整的颜色和线型标识符列表，参见
http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

rcParams中有很多设置项目，完整的列表参见
http://matplotlib.org/users/customizing.html

如果你不想花费精力对这些参数进行单独设置，可以使用一个预定义的样式表，具体介绍参见
http://matplotlib.org/users/style_sheets.html#style-sheets

### pylab.show()怎么用好？

放在代码的最末尾。因为它会导致程序挂起，直到关闭窗口。这有时候很麻烦。

生成图片不show出来？并不傻，可以保存啊。

```python
pylab.figure(2)                    #创建图2
pylab.plot([1,4,2,3], [5,6,7,8])   #在图2上绘图
pylab.savefig('Figure-Addie')      #保存图2
```


### pylab默认保存为什么格式？

扩展名会是.png，表示文件的格式是可移植网络图形（Portable Network Graphics）这是一种表示图形的公共领域标准。


### 画图出来要做到什么礼貌？

图都有标题，坐标轴都有标注。不能让看的人自己猜。


### 排版typography中"点point"是什么概念？

1点是1/72英寸，0.3527mm


### 绘图颜色很重要吗？

很重要，不能忽视。

too important to ignore


## 11.2 Plotting Mortgages, an Extended Example


### pylab与matplotlab官方网站上的例子好像不大合。

但是可以运行。


### array比list更方便？

更多线性代数工具。

比如
```python
a1 = pylab.array([1, 2, 4])
print('a1 =', a1)
a2 = a1*2
print('a2 =', a2)

print('a1 + 3 =', a1 + 3)
print('3 - a1 =', 3 - a1)
print('a1 - a2 =', a1 - a2)
print('a1*a2 =', a1*a2)
```

输出
```commandline
a1 = [1 2 4]
a2 = [2 4 8]
a1 + 3 = [4 5 7]
3 - a1 = [ 2 1 -1]
a1 - a2 = [-1 -2 -4]
a1*a2 = [ 2 8 32]
```

### pylab对list做了什么处理？

把list转成array，nam = pylab.array(lis)只不过是明说了一次。


### 每月还款额 怎么画，什么样？

```python
    #每个月的还款额，等额还款，基本是水平线
    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend) #第一个月是0，不必画出来，y轴不从0开始。
```

![](https://ws1.sinaimg.cn/large/006tNc79gy1fqnwcoi5mtj30hs0dcdgj.jpg)


### 待还本金 怎么画，什么样？

```python
    #每个月看一眼待还本金，总是在减少，但是速度不同哦
    def plotBalance(self, style):
        pylab.plot(self.outstanding, style, label = self.legend)
```

![](https://ws4.sinaimg.cn/large/006tNc79gy1fqnweom3dnj30hs0dcq43.jpg)


### 已付总额 怎么画，什么样？

```python
    #截止到每个月的已经付给银行的总额
    def plotTotPd(self, style):
        totPd = [self.paid[0]] #用0月金额初始化
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i]) #上月结算额 + 本月新增额 = 本月结算额

        pylab.plot(totPd, style, label = self.legend)
```

![](https://ws2.sinaimg.cn/large/006tNc79gy1fqnwfixvtnj30hs0dcgml.jpg)

初始五年放大看

![](https://ws4.sinaimg.cn/large/006tNc79gy1fqnwj7c8ivj30zk0qo76u.jpg)


### 净成本 怎么画，什么样？

```python
    #本金当然要还，除去还本金，付的利息总额是净成本
    def plotNet(self, style):
        #算一遍每月累积总额totPd
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        #用outstanding待还本金数组的长度初始化equityAcquired
        equityAcquired = pylab.array([self.loan] * \
                         len(self.outstanding))
        #初始本金 - 待还本金 = 已还本金总额
        equityAcquired = equityAcquired - \
                         pylab.array(self.outstanding)
        #总净成本 = 已付总额 - 已还本金总额
        net = pylab.array(totPd) - equityAcquired

        pylab.plot(net, style, label = self.legend)
```

![](https://ws3.sinaimg.cn/large/006tNc79gy1fqnwk30c3bj30hs0dct9q.jpg)

放大一点看消长变化

![](https://ws3.sinaimg.cn/large/006tNc79gy1fqnwkrhgm2j30zk0qo0vh.jpg)


### 如何批量绘图，分别标注？

用for循环分别激活各张图，分别画入三条线。

用labelPlot函数分别给四张图做标注。

```python
    #建一个给图做标注的函数，顺便存档
    def labelPlot(figure, title, xLabel, yLabel):
        pylab.figure(figure)
        pylab.title(title)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.legend(loc = 'best')
        pylab.savefig(title)

    styles = ['b-', 'g-.', 'r:']

    #给图编号赋名，方便理解和区分
    payments, cost, balance, netCost = 0, 1, 2, 3

    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(netCost)
        morts[i].plotNet(styles[i])

    labelPlot(payments, 'Monthly Payments of $' + str(amt) +
                ' Mortgages', 'Months', 'Monthly Payments')
    labelPlot(cost, 'Cash Outlay of $' + str(amt) +
              'Mortgages', 'Months', 'Total Payments')
    labelPlot(balance, 'Balance Remaining of $' + str(amt) +
              'Mortgages', 'Months', 'Remaining Loan Balance of $')
    labelPlot(netCost, 'Net Cost of $' + str(amt) + ' Mortgages',
              'Months', 'Payments - Equity $')
 
```

---
以上，2018-04-24。