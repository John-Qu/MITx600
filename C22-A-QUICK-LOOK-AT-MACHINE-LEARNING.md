# 20 A QUICK LOOK AT MACHINE LEARNING


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


