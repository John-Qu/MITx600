# 22 A QUICK LOOK AT MACHINE LEARNING


### 为什么有必要让机器学会学习？

数据量太大，人类理解跟不上。

the amount of digital data

the human comprehension

数据存储量3年翻一番

需要从大量数据中拧出有用的信息

to wring more information from "big data"

方法之一，就是统计的机器学习 statistical machine learning


### 什么是机器学习？

广义的：任何有用的程序都学出了一点东西。

狭义的：自动的学习，学习生产有用的推理，推理出隐含的模式，模式出自数据。


### 人类通过什么方式学习？

记忆和推广 memorization and generalization

记忆个案，推导出一般法则，推广到其他情况。


### 机器学习的基本范式paradigm？

以线性回归为例。

1. 观察数据
    - 观察对象是一组数据，a set of examples, i.e. training data。
    - 数据表现的信息肯定是不完整的，imcomplete information。
    - 能做统计的现象，about some statistical phenomenon。
2. 推导模型
    - inference techniques
    - a model of a process
    - a process that can have generated the observed examples
3. 预测未知
    - to make predictions
    - about previously unseen examples

### 机器学习出一个模型来的过程包括哪三个部分？

1 模型的样子
- representation

2 评价的目标
- objective function
- to assess the goodness of the model

3 优化的方法
- optimization method
- to maximize of minimize the value of the objective function


### 什么是特征向量？


在一类群体中，每个对象，都有一些可以独立描述的方面aspects，或者称为特征features。把这些打包在一起，从多个角度描绘一个对象，就是它的特征向量。

比如：为每个姓名关联一个特征向量

* Abraham Lincoln: [American, President, 193 cm tall]
* George Washington: [American, President, 189 cm tall]
* Charles de Gaulle: [French, President, 196 cm tall]
* Benjamin Harrison: [American, President, 168 cm tall]
* James Madison: [American, President, 163 cm tall]
* Louis Napoleon: [French, President, 169 cm tall]


### 机器学习算法有那两个大方向？

#### 有监督地学习 supervised learning

有完整的（特征向量，特征值）向量/值 对。 feature vector/value pair
有特征值，或有特征标签。

目的是：
以特征向量/值对为基础，推理出一个模型，能用于求没见过的特征向量的特征值。

例如：
- 信用卡欺诈
- 推荐电影

#### 无监督地学习 unsupervised learning

不完整的（特征向量，特征值）向量/值 对。

没有值，没有标签。

目的是：

从特征向量集合中挖掘隐含的结构。to uncover latent structure in the set of feature vectors


### 有监督地学习的两种模型？

回归模型Regression Model：与特征向量对应的是一个特征值（实数）

分类模型Classification Model: 与特征向量对应的是一个标签label（来自于有限数量的标签集）


### 无监督地学习的两种模型？

隐含变量 a latent variable：从明说的值里可以推导出来的没明说的值。
- 比如：是成功的学生的概率，从高中成绩和标转化考试成绩中。

相似聚簇 clustering：同簇中的个体更相似。
- 比如：相关基因。
  

## 22.1 Feature Vector


### 特征工程的目标是什么？

信噪比，signal-to-noise ratio
- useful input
- irrelevant input
- a noise can be a distraction that obscures the truth

目标是：挑选特征，对信号有用的特征，而不是噪声
- to seperate those features in the available data
- that contribute to the signal
- from those (features) that are merely noise.


### 特征工程碰到什么数据情况比较棘手？

数据有很多维度，但是相比之下，样本的量却不够多。 
- dimensionality of the data (i.e., the number of different features)
- the number of samples

例如

| 名称   | 产卵 | 鳞片 | 有毒 | 冷血 | 腿   | 爬行动物 |
| ------ | ---- | ---- | ---- | ---- | ---- | -------- |
| 眼镜蛇 | 是   | 有   | 有   | 是   | 0    | 是       |
| 响尾蛇 | 是   | 有   | 有   | 是   | 0    | 是       |
| 巨蚺   | 否   | 有   | 无   | 是   | 0    | 是       |
| 短吻鳄 | 是   | 有   | 无   | 是   | 4    | 是       |
| 箭毒蛙 | 是   | 无   | 有   | 否   | 4    | 否       |
| 鲑鱼   | 是   | 无   | 无   | 是   | 0    | 否       |
| 蟒蛇   | 是   | 无   | 无   | 是   | 0    | 是       |

特征貌似很多，有五个特征。

如果只有眼镜蛇和响尾蛇两个样本，那么是爬行动物的有用特征就是：产卵、有鳞片、有毒、冷血、无腿。

但是它显然被巨蚺推翻了，因为它不产卵，也没毒，是爬行动物。

所以，样本数量很重要。


### 成功的特征工程工作做了什么？

抽象，从可获得的海量信息中抽取出有生产力的信息，以便归纳。
- abstraction process
- the vast amount of information that might be available
- information from which it will be productive to generalize.

不是能获得什么，而是想归纳出什么。

为了产出，而不是可得。


### 有什么技术帮助特征工程？

特征消除技术 feature eliminination techniques
- 与标签相关的特征。
- 特征之间高度相关，可能很多冗余。

领域专家设计特征 the design of features by those domain expertise
- BMI body mass index


### 无监督地学习，选择特征靠什么？

靠直觉吗？

如何评价直觉好不好？


### 特征不够完美区分怎么办？

放弃吗？

例如

| 名称   | 产卵 | 鳞片 | 有毒 | 冷血 | 腿   | 爬行动物 |
| ------ | ---- | ---- | ---- | ---- | ---- | -------- |
| 眼镜蛇 | 是   | 有   | 有   | 是   | 0    | 是       |
| 响尾蛇 | 是   | 有   | 有   | 是   | 0    | 是       |
| 巨蚺   | 否   | 有   | 无   | 是   | 0    | 是       |
| 短吻鳄 | 是   | 有   | 无   | 是   | 4    | 是       |
| 箭毒蛙 | 是   | 无   | 有   | 否   | 4    | 否       |
| 鲑鱼   | 是   | 无   | 无   | 是   | 0    | 否       |
| 蟒蛇   | 是   | 无   | 无   | 是   | 0    | 是       |

鲑鱼和蟒蛇的特征向量完全一样，但是他们一个不是爬行动物，而一个是。这是典型的特征向量维度不够。

这个实例中，还可以添加一个没在初始特征集合中的特征，就是如果有卵，卵上有羊膜。这样就可以区分鲑鱼和蟒蛇了。

很多实际应用中，都不可能构建出能做完美区分的特征向量。

不要放弃，至少可以找到必要条件。

冷血和有鳞片两个特征，是爬行动物的必要条件，虽然不充分。也就是说，用这两个特征组成特征向量，只会造成假阳性 false positive, (说它是，其实不是)，而不会造成假阴性 false negatives。


## 22.2 Distance Metrics


### 比较各特征向量的相似性，有什么办法？

evaluate the similarity of two object

第一步是先量化，把一串特征转化成一串数字。

比较由数字组成的向量的相似性，有很多办法。

如果两个向量的长度相同，办法之一是闵可夫斯基距离，这是大小magnitude。

还有一个办法是测量两个向量的夹角，就像三角形余弦定理中那样，这是角度angle. 多用于高维向量。


### 闵可夫斯基距离公式怎么写？

![](https://ws1.sinaimg.cn/large/006tKfTcly1frg8swvieej30oo02kwev.jpg)

$$ {\rm distance}(V,W,p)=(\sum^{{\rm len}}_{i=1}{\rm abs}(V_i-W_i)^p)^{1/p} $$

这里的len是向量长度(维度？)。

参数p至少为1，它定义了度量向量V和W之间距离时要经过的路径类型。(如果允许p小于1，比如p=0.5，那么会违背三角形两边之和大于第三边的定律。) 

向量的长度为2时，p的作用是最容易表示的，因为可以使用笛卡儿坐标系表示。

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/25.d22z.001.png)

p=2的闵可夫斯基距离，是欧氏距离Euclidean distance。

p=1的闵可夫斯基距离，是曼哈顿距离Manhattan distance。


### 对爬行动物之间的相似性代码？

```python
import pylab

def minkowskiDist(v1, v2, p):
    """假设v1和v2是两个等长的数值型数组
       返回v1和v2之间阶为p的闵可夫斯基距离"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)


class Animal(object):
    def __init__(self, name, features):
        """假设name是字符串；features是数值型列表"""
        self.name = name
        self.features = pylab.array(features) #列表已经转换为数组

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self, other):
        """假设other是Animal类型的对象
           返回self与other的特征向量之间的欧氏距离"""
        return minkowskiDist(self.getFeatures(),
                             other.getFeatures(), 2)


def compareAnimals(animals, precision):
    """假设animals是动物列表，precision是非负整数
       建立一个表格，表示每种动物之间的欧氏距离"""
    #获取行标签和列标签
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    #计算动物之间的距离
    #对每一行
    for a1 in animals:
        row = []
        #对每一列
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    #生成表格
    table = pylab.table(rowLabels = rowLabels,
                        colLabels = columnLabels,
                        cellText = tableVals,
                        cellLoc = 'center',
                        loc = 'center',
                        colWidths = [0.2]*len(animals))
    table.scale(1, 2.5)

    pylab.savefig('distances')


rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa\nconstrictor', [0,1,0,1,0])
# dartFrog = Animal('dart frog', [1,0,1,0,4]) # 不应给legs更大的权重
dartFrog = Animal('dart frog', [1,0,1,0,1])
# animals = [rattlesnake, boa, dartFrog]

# alligator = Animal('alligator', [1,1,0,1,4]) # 不应给legs更大的权重
alligator = Animal('alligator', [1,1,0,1,1])

# 把其他几种动物补全
cobra = Animal('cobra', [1,1,1,1,0])
salmon = Animal('salmon', [1,1,0,1,0])
python = Animal('python', [1,1,0,1,0])
animals = [cobra, rattlesnake, boa, alligator, dartFrog, salmon, python]

compareAnimals(animals, 3)
pylab.show()
```

![](https://ws4.sinaimg.cn/large/006tKfTcly1frga7b575oj30hs0dcdg9.jpg)

![](https://ws4.sinaimg.cn/large/006tKfTcly1frga7lo2ktj31kw0wu0vg.jpg)

有几个问题

- 为什么有那个框子，不知道是哪行代码印出来的。
- salmon和python与另外几个的距离不是1.0就是2.0, 巧合吗？
- 自动生成的figure不能完整显示7组的图表，需要手动调整，为什么？

---

以上，2018-05-19 07:12:35