# 24 CLASSIFICATION METHODS


### 什么是classification model？

它是有监督的机器学习中最常用的办法。

A **classification model**, or **classifier分类器**, is used to label an example as belonging to one of a finite set of categories.

比如
- 垃圾邮件分类。

称为
- belonging to a class
- having a label


### 分类学习有几种类型？

单分类学习one-class learning
- 很难找到不属于这个类别的训练数据。
- 通常用于建立异常检测机制，例如在计算机网络中检测未知攻击。

二分类学习two-class learing (binary classification)
- 训练集中的样本全部来自两个类别（通常称为阳性和阴性）。
- 目标是找到一个可以区分两个类别的边界。

多分类学习multi-class learning


## 24.1 Evaluating Classifiers


### 训练一个分类器，要面对什么矛盾？

(1)既能够非常好地拟合现有数据；provide a reasonable good fit for the available data.

(2)又能够对未知数据做出好的预测。have a reasonable chance of making good predictions about as yet unseen data.


### 用训练集训练分类器，最小化训练误差training error时，要满足一定的约束条件subject to certain constraints。设计这些约束条件的目的是什么？

为了提高模型预测未知数据的准确率。to increase the probability that the model will perform reasonably well on as yet unseen data.


### 什么是混淆矩阵confusion matrices？怎么用？

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/27.d24z.001.png)

把classifier的结果统计入混淆矩阵。

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/27.d24z.002.png)


### 怎样用数据评价混淆矩阵？

|                   | Predicted Positive | Predicted Negative |
| ----------------- | :----------------: | :----------------: |
| Actually Positive | +➕ truePos        | +➖ falseNeg       |
| Actually Negative | -➕ falsePos       | -➖ trueNeg       |

- accuracy 精确度，总体预测准确的程度，即正确识别阳性和阴性的比例，(++ --)/( ++ -+ -- +-)
- sensitivity 灵敏度，阳性中，被正确识别的比例，++/(++ +-)
- specificity 专一度，计算阴性中，被正确识别的比例，--/(-- +-)
- positive predicted value 阳性预测中，正确的比例，++/(++ -+)
- negative predicted value 阴性预测中，正确的比例，--/(-- +-)

```python
# -*- coding: utf-8 -*-

def accuracy(truePos, falsePos, trueNeg, falseNeg):
    """
    精确度，计算总体预测准确的程度，即正确识别阳性和阴性的比例，(++ --)/( ++ -+ -- +-)
    :param truePos: int，真阳性++
    :param falsePos: int，假阳性-+
    :param trueNeg: int，真阴性--
    :param falseNeg: int，假阴性+-
    :return: float
    """
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator/denominator


def sensitivity(truePos, falseNeg):
    """
    灵敏度，计算阳性中，被正确识别的比例，++/(++ +-)
    :param truePos: int，真阳性++
    :param falseNeg: int，假阴性+-
    :return: float
    """
    try:
        return truePos/(truePos + falseNeg)
    except ZeroDivisionError:
        return float('nan')

def specificity(trueNeg, falsePos):
    """
    专一度，计算阴性中，被正确识别的比例，--/(-- +-)
    :param trueNeg: int，真阴性--
    :param falsePos: int，假阳性-+
    :return: float
    """
    try:
        return trueNeg/(trueNeg + falsePos)
    except ZeroDivisionError:
        return float('nan')

def posPredVal(truePos, falsePos):
    """
    阳性预测正确比例，++/(++ -+)
    :param truePos: int，真阳性++
    :param falsePos: int，假阳性-+
    :return:
    """
    try:
        return truePos/(truePos + falsePos)
    except ZeroDivisionError:
        return float('nan')

def negPredVal(trueNeg, falseNeg):
    """
    阴性预测正确比例，--/(-- +-)
    :param trueNeg: int，真阴性--
    :param falseNeg: int，假阴性+-
    :return:
    """
    try:
        return trueNeg/(trueNeg + falseNeg)
    except ZeroDivisionError:
        return float('nan')

def getStats(truePos, falsePos, trueNeg, falseNeg, toPrint = True):
    """
    计算classifiers的各种正确比例
    :param truePos: int，真阳性++
    :param falsePos: int，假阳性-+
    :param trueNeg: int，真阴性--
    :param falseNeg: int，假阴性+-
    :param toPrint: bool，是否打印结果，默认True
    :return: (accur, sens, spec, ppv, npv)
    """
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    npv = negPredVal(trueNeg, falseNeg)
    if toPrint:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Pos. Pred. Val. =', round(ppv, 3))
        print(' Neg. Pred. Val. =', round(npv, 3))
    return (accur, sens, spec, ppv, npv)
```


## 24.2 Predicting the Gender of Runners


### 波士顿马拉松，看成绩和年龄，就能大致猜出性别吗？怎么准备类和数据？

```python
# -*- coding: utf-8 -*-

from em_17_1_getBMdata import getBMData
import random
class Runner(object):
    def __init__(self, gender, age, time):
        # 把年龄和成绩组成了特征向量。
        self.featureVec = (age, time)
        # 性别是标签
        self.label = gender

    def featureDist(self, other):
        """计算特征向量的欧氏距离"""
        dist = 0.0 # 初始化，方便后面+=
        for i in range(len(self.featureVec)):
            dist += abs(self.featureVec[i] - other.featureVec[i])**2
        return dist**0.5

    def getTime(self):
        return self.featureVec[1]

    def getAge(self):
        return self.featureVec[0]

    def getLabel(self):
        return self.label

    def getFeatures(self):
        return self.featureVec

    def __str__(self):
        return str(self.getAge()) + ', ' + str(self.getTime())\
               + ', ' + self.label

def buildMarathonExamples(fileName):
    """提取数据，构建Runner对象，添加入examples列表。"""
    data = getBMData(fileName) # 这个bm_results2012.txt文件没有找到
    examples = []
    for i in range(len(data['age'])):
        a = Runner(data['gender'][i], data['age'][i],
                   data['time'][i])
        examples.append(a)
    return examples

def divide80_20(examples):
    """把实例按照80/20比例，分成训练集和测试集"""
    # 随机挑选出测试集实例对应的index。不直接挑，挑剩下的不好处理。
    sampleIndices = random.sample(range(len(examples)),
                                  len(examples)//5)
    trainingSet, testSet = [], []
    for i in range(len(examples)):
        if i in sampleIndices:
            testSet.append(examples[i])
        else:
            trainingSet.append(examples[i])
    return trainingSet, testSet
```


## 24.3 K-nearest Neighbors


### K最近邻方法的原理是什么？

在训练集中找到K个与手中对象最相似的邻居，他们大多数有什么标签，就把手中对像打上什么标签。

比如

- 公园里的鸟，查书，搜索引擎。


### KNN分类法有什么缺点？

如果训练集中的各种标签严重分类不均。

比如

- K个近邻中，真正与手中对象相似的，得不到大多数。


### k最近邻分类器怎么写？

```python
# -*- coding: utf-8 -*-

import pylab, random
from em_24_1_evaluating_classifiers import accuracy
from em_24_2_runner import divide80_20


def findKNearest(example, exampleSet, k):
    """
    用手中的实例，在实例集中找到k个最近邻。
    :param example: 手中有待贴标的对象实例
    :param exampleSet: 作为搜索源的实例集
    :param k: k个最近邻
    :return: k个最近邻的列表，以及相应距离的列表
    """
    kNearest, distances = [], []
    #建立一个列表，包含最初K个样本和它们的距离
    for i in range(k):
        kNearest.append(exampleSet[i])
        distances.append(example.featureDist(exampleSet[i]))
    maxDist = max(distances) #找出最大距离
    #检查其余样本，替换初始邻居
    for e in exampleSet[k:]:
        dist = example.featureDist(e)
        if dist < maxDist:
            #通过查找distances列表，找到原始maxDist的索引位置
            maxIndex = distances.index(maxDist)
            #替换掉索引位置伤的实例和相应距离
            kNearest[maxIndex] = e
            distances[maxIndex] = dist
            #重新计算出k个邻居中的最大距离，进入下一个循环
            maxDist = max(distances)
    return kNearest, distances


def KNearestClassify(training, testSet, label, k):
    """
    使用K最近邻分类器预测testSet中的每个样本是否具有给定的标签
    :param training: 训练集
    :param testSet: 测试集
    :param label: 二类学习的标签
    :param k: 选取K位邻居，过半数占优的标签胜出
    :return: 真阳性、假阳性、真阴性和假阴性的数量
    """
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for e in testSet:
        nearest, distances = findKNearest(e, training, k)
        #进行投票
        numMatch = 0
        for i in range(len(nearest)):
            if nearest[i].getLabel() == label:
                numMatch += 1
        if numMatch > k//2: #预测e具有此标签
            if e.getLabel() == label: #e真有此标签
                truePos += 1
            else: #e却没有此标签
                falsePos += 1
        else: #预测e不具有此标签
            if e.getLabel() != label: #e真没有此标签
                trueNeg += 1
            else: #e却有这个标签
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

```


### k最近邻分类算法的复杂度？

这个实现其实是一种暴力算法。

函数findKNearest的复杂度与exampleSet中的样本数量成线性关系，因为它要计算example与exampleSet中每个元素之间的特征距离。

函数KNearestClassify使用简单的多数票胜出原则来进行分类，它的复杂度是O(len(training)* len(testSet))，因为它要对函数findNearest进行总共len(testSet)次调用。
- 相当于O(n2)?


### 根据标签分布的概率算法怎么写？比k最近邻算法结果差吗？

```python
# -*- coding: utf-8 -*-

def prevalenceClassify(training, testSet, label):
    """
    把训练集中标签所占的比例（流行程度），作为给测试集对象分配标签的概率。
    :param training: 训练集
    :param testSet: 测试集
    :param label: 标签
    :return: 真阳性、假阳性、真阴性和假阴性的数量
    """
    numWithLabel = 0
    for e in training:
        if e.getLabel()== label:
            numWithLabel += 1
    probLabel = numWithLabel/len(training) #标签的概率
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for e in testSet:
        if random.random() < probLabel: #标签概率大于随机数，预测e具有标签
            if e.getLabel() == label: #e真有此标签
                truePos += 1
            else: #e却没有此标签
                falsePos += 1
        else: #预测e不具有此标签
            if e.getLabel() != label: #e真没有此标签
                trueNeg += 1
            else: #e却有这个标签
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

```

```commandline
K最近邻算法的结果：
Accuracy = 0.65
Sensitivity = 0.715
Specificity = 0.563
Pos. Pred. Val. = 0.684

根据标签流行程度概率分配的结果：
准确度=0.514 因为对训练集做了随机性的下采样，准确度低于总体的58%也正常。
灵敏度=0.593
特异度=0.41
阳性预测值=0.57
```


### 在k最近邻算法里，为什么把K设为9？

与训练集有关，实验出来的。

```python
# -*- coding: utf-8 -*-

def findK(training, minK, maxK, numFolds, label):
    """
    k最近邻法，检验什么k值足够好，取一定范围内的奇数值，分别计算numFold次的平均准确度，绘图输出
    :param training: 训练集
    :param minK: 尝试用的最小K值
    :param maxK: 尝试用的最大K值
    :param numFolds: 每个K值采样几次再取平均
    :param label: 标签
    :return: None
    """
    #在k的奇数取值范围内找出平均准确度
    accuracies = []
    for k in range(minK, maxK + 1, 2):
        score = 0.0
        for i in range(numFolds):
            #通过下采样减少计算时间
            fold = random.sample(training, min(5000, len(training)))
            examples, testSet = divide80_20(fold)
            truePos, falsePos, trueNeg, falseNeg =\
                KNearestClassify(examples, testSet, label, k)
            score += accuracy(truePos, falsePos, trueNeg, falseNeg)
        accuracies.append(score/numFolds)
    pylab.plot(range(minK, maxK + 1, 2), accuracies)
    pylab.title('Average Accuracy vs k (' + str(numFolds)\
                + ' folds)')
    pylab.xlabel('k')
    pylab.ylabel('Accuracy')

findK(training, 1, 21, 5, 'M')
```

![](http://www.ituring.com.cn/figures/2017/PythonIntroduction/27.d24z.006.png)

- 从图中可以看出，对于5折交叉验证，获得最高准确度的k值是17。
- 当然，k>21时，完全有可能得到更高的准确度。
- 但k达到9时，准确度就在一个相当狭窄的区间内波动，所以我们选择9作为k的值。


## 24.4 Regression-based Classifiers


### 马拉松成绩、年龄和性别，三个变量，谁做自变量？

方法一：

用年龄做自变量，成绩做因变量，性别做区别，可以得到男和女两个线性回归模型。

测试集中的实例，年龄作为自变量分别带入两个模型，得到两个成绩，哪个更接近真实成绩，就打上哪个性别标签。

问题：

为什么这么不直接？不能用年龄和成绩做自变量，性别做因变量吗？性别值更靠近哪一个，就算哪个性别。

方法二：

使用polyfit将一个年龄和完成时间的函数映射成一个实数。

问题：

如果预测出某个跑步者在男性和女性之间，我们应该如何解释呢？

或许我们可以将Y轴解释为跑步者是男性的概率。这样也不是很好，因为对模型应用polyval函数时，甚至不能保证返回值肯定在0和1之间。


### logistic regression为什么叫这个名字？

之所以称作logistic回归是因为，解决这种最优化问题时，目标函数是基于比值比（odds ratio）的对数的。这种函数称为logit(分对数)函数，它的反函数称为logistic（对数的）函数。

![](https://ws4.sinaimg.cn/large/006tNc79gy1frmgy30jsaj31kw0whdq1.jpg)
![](https://ws3.sinaimg.cn/large/006tNc79gy1frmgxz8pytj31kw0eaad3.jpg)
![](https://ws3.sinaimg.cn/large/006tNc79gy1frmgxw64a5j31kw0gfafx.jpg)
![](https://ws2.sinaimg.cn/large/006tNc79gy1frmgxtq58dj31kw0chgp3.jpg)
![](https://ws1.sinaimg.cn/large/006tNc79gy1frmgxrs90qj31kw0f9gph.jpg)
![](https://ws4.sinaimg.cn/large/006tNc79gy1frmgxp856rj31kw07rmzo.jpg)


参考：

https://en.wikipedia.org/wiki/Logistic_regression

http://www.stat.cmu.edu/~cshalizi/uADA/12/lectures/ch12.pdf


### logistic regression明确设计用来做什么？它怎么写的？

预测一个事件的概率。to predict the probability of an event.

module `sklearn.linear_model.logistic.py`中有

```python
# -*- coding: utf-8 -*-

class LogisticRegression(BaseEstimator, LinearClassifierMixin,
                         _LearntSelectorMixin, SparseCoefMixin):
    """Logistic Regression (aka logit, MaxEnt) classifier.

    In the multiclass case, the training algorithm uses the one-vs-rest (OvR)
    scheme if the 'multi_class' option is set to 'ovr', and uses the cross-
    entropy loss if the 'multi_class' option is set to 'multinomial'.
    (Currently the 'multinomial' option is supported only by the 'lbfgs',
    'sag' and 'newton-cg' solvers.)

    This class implements regularized logistic regression using the
    'liblinear' library, 'newton-cg', 'sag' and 'lbfgs' solvers. It can handle
    both dense and sparse input. Use C-ordered arrays or CSR matrices
    containing 64-bit floats for optimal performance; any other input format
    will be converted (and copied).

    The 'newton-cg', 'sag', and 'lbfgs' solvers support only L2 regularization
    with primal formulation. The 'liblinear' solver supports both L1 and L2
    regularization, with a dual formulation only for the L2 penalty.

    Read more in the :ref:`User Guide <logistic_regression>`.

    Parameters
    ----------
    penalty : str, 'l1' or 'l2', default: 'l2'
        Used to specify the norm used in the penalization. The 'newton-cg',
        'sag' and 'lbfgs' solvers support only l2 penalties.

    dual : bool, default: False
        Dual or primal formulation. Dual formulation is only implemented for
        l2 penalty with liblinear solver. Prefer dual=False when
        n_samples > n_features.

    C : float, default: 1.0
        Inverse of regularization strength; must be a positive float.
        Like in support vector machines, smaller values specify stronger
        regularization.

    fit_intercept : bool, default: True
        Specifies if a constant (a.k.a. bias or intercept) should be
        added to the decision function.

    intercept_scaling : float, default 1.
        Useful only when the solver 'liblinear' is used
        and self.fit_intercept is set to True. In this case, x becomes
        [x, self.intercept_scaling],
        i.e. a "synthetic" feature with constant value equal to
        intercept_scaling is appended to the instance vector.
        The intercept becomes ``intercept_scaling * synthetic_feature_weight``.

        Note! the synthetic feature weight is subject to l1/l2 regularization
        as all other features.
        To lessen the effect of regularization on synthetic feature weight
        (and therefore on the intercept) intercept_scaling has to be increased.

    class_weight : dict or 'balanced', default: None
        Weights associated with classes in the form ``{class_label: weight}``.
        If not given, all classes are supposed to have weight one.

        The "balanced" mode uses the values of y to automatically adjust
        weights inversely proportional to class frequencies in the input data
        as ``n_samples / (n_classes * np.bincount(y))``.

        Note that these weights will be multiplied with sample_weight (passed
        through the fit method) if sample_weight is specified.

        .. versionadded:: 0.17
           *class_weight='balanced'* instead of deprecated
           *class_weight='auto'*.

    max_iter : int, default: 100
        Useful only for the newton-cg, sag and lbfgs solvers.
        Maximum number of iterations taken for the solvers to converge.

    random_state : int seed, RandomState instance, default: None
        The seed of the pseudo random number generator to use when
        shuffling the data. Used only in solvers 'sag' and 'liblinear'.

    solver : {'newton-cg', 'lbfgs', 'liblinear', 'sag'}, default: 'liblinear'
        Algorithm to use in the optimization problem.

        - For small datasets, 'liblinear' is a good choice, whereas 'sag' is
            faster for large ones.
        - For multiclass problems, only 'newton-cg', 'sag' and 'lbfgs' handle
            multinomial loss; 'liblinear' is limited to one-versus-rest
            schemes.
        - 'newton-cg', 'lbfgs' and 'sag' only handle L2 penalty.

        Note that 'sag' fast convergence is only guaranteed on features with
        approximately the same scale. You can preprocess the data with a
        scaler from sklearn.preprocessing.

        .. versionadded:: 0.17
           Stochastic Average Gradient descent solver.

    tol : float, default: 1e-4
        Tolerance for stopping criteria.

    multi_class : str, {'ovr', 'multinomial'}, default: 'ovr'
        Multiclass option can be either 'ovr' or 'multinomial'. If the option
        chosen is 'ovr', then a binary problem is fit for each label. Else
        the loss minimised is the multinomial loss fit across
        the entire probability distribution. Works only for the 'newton-cg',
        'sag' and 'lbfgs' solver.

        .. versionadded:: 0.18
           Stochastic Average Gradient descent solver for 'multinomial' case.

    verbose : int, default: 0
        For the liblinear and lbfgs solvers set verbose to any positive
        number for verbosity.

    warm_start : bool, default: False
        When set to True, reuse the solution of the previous call to fit as
        initialization, otherwise, just erase the previous solution.
        Useless for liblinear solver.

        .. versionadded:: 0.17
           *warm_start* to support *lbfgs*, *newton-cg*, *sag* solvers.

    n_jobs : int, default: 1
        Number of CPU cores used during the cross-validation loop. If given
        a value of -1, all cores are used.

    Attributes
    ----------
    coef_ : array, shape (n_classes, n_features)
        Coefficient of the features in the decision function.

    intercept_ : array, shape (n_classes,)
        Intercept (a.k.a. bias) added to the decision function.
        If `fit_intercept` is set to False, the intercept is set to zero.

    n_iter_ : array, shape (n_classes,) or (1, )
        Actual number of iterations for all classes. If binary or multinomial,
        it returns only 1 element. For liblinear solver, only the maximum
        number of iteration across all classes is given.

    See also
    --------
    SGDClassifier : incrementally trained logistic regression (when given
        the parameter ``loss="log"``).
    sklearn.svm.LinearSVC : learns SVM models using the same algorithm.

    Notes
    -----
    The underlying C implementation uses a random number generator to
    select features when fitting the model. It is thus not uncommon,
    to have slightly different results for the same input data. If
    that happens, try with a smaller tol parameter.

    Predict output may not match that of standalone liblinear in certain
    cases. See :ref:`differences from liblinear <liblinear_differences>`
    in the narrative documentation.

    References
    ----------

    LIBLINEAR -- A Library for Large Linear Classification
        http://www.csie.ntu.edu.tw/~cjlin/liblinear/

    SAG -- Mark Schmidt, Nicolas Le Roux, and Francis Bach
        Minimizing Finite Sums with the Stochastic Average Gradient
        https://hal.inria.fr/hal-00860051/document

    Hsiang-Fu Yu, Fang-Lan Huang, Chih-Jen Lin (2011). Dual coordinate descent
        methods for logistic regression and maximum entropy models.
        Machine Learning 85(1-2):41-75.
        http://www.csie.ntu.edu.tw/~cjlin/papers/maxent_dual.pdf
    """

    def __init__(self, penalty='l2', dual=False, tol=1e-4, C=1.0,
                 fit_intercept=True, intercept_scaling=1, class_weight=None,
                 random_state=None, solver='liblinear', max_iter=100,
                 multi_class='ovr', verbose=0, warm_start=False, n_jobs=1):

        self.penalty = penalty
        self.dual = dual
        self.tol = tol
        self.C = C
        self.fit_intercept = fit_intercept
        self.intercept_scaling = intercept_scaling
        self.class_weight = class_weight
        self.random_state = random_state
        self.solver = solver
        self.max_iter = max_iter
        self.multi_class = multi_class
        self.verbose = verbose
        self.warm_start = warm_start
        self.n_jobs = n_jobs

     def fit(self, X, y, sample_weight=None):
        """Fit the model according to the given training data.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape (n_samples, n_features)
            Training vector, where n_samples is the number of samples and
            n_features is the number of features.

        y : array-like, shape (n_samples,)
            Target vector relative to X.

        sample_weight : array-like, shape (n_samples,) optional
            Array of weights that are assigned to individual samples.
            If not provided, then each sample is given unit weight.

            .. versionadded:: 0.17
               *sample_weight* support to LogisticRegression.

        Returns
        -------
        self : object
            Returns self.
        """
        if not isinstance(self.C, numbers.Number) or self.C < 0:
            raise ValueError("Penalty term must be positive; got (C=%r)"
                             % self.C)
        if not isinstance(self.max_iter, numbers.Number) or self.max_iter < 0:
            raise ValueError("Maximum number of iteration must be positive;"
                             " got (max_iter=%r)" % self.max_iter)
        if not isinstance(self.tol, numbers.Number) or self.tol < 0:
            raise ValueError("Tolerance for stopping criteria must be "
                             "positive; got (tol=%r)" % self.tol)

        X, y = check_X_y(X, y, accept_sparse='csr', dtype=np.float64,
                         order="C")
        check_classification_targets(y)
        self.classes_ = np.unique(y)
        n_samples, n_features = X.shape

        _check_solver_option(self.solver, self.multi_class, self.penalty,
                             self.dual)

        if self.solver == 'liblinear':
            self.coef_, self.intercept_, n_iter_ = _fit_liblinear(
                X, y, self.C, self.fit_intercept, self.intercept_scaling,
                self.class_weight, self.penalty, self.dual, self.verbose,
                self.max_iter, self.tol, self.random_state,
                sample_weight=sample_weight)
            self.n_iter_ = np.array([n_iter_])
            return self

        if self.solver == 'sag':
            max_squared_sum = row_norms(X, squared=True).max()
        else:
            max_squared_sum = None

        n_classes = len(self.classes_)
        classes_ = self.classes_
        if n_classes < 2:
            raise ValueError("This solver needs samples of at least 2 classes"
                             " in the data, but the data contains only one"
                             " class: %r" % classes_[0])

        if len(self.classes_) == 2:
            n_classes = 1
            classes_ = classes_[1:]

        if self.warm_start:
            warm_start_coef = getattr(self, 'coef_', None)
        else:
            warm_start_coef = None
        if warm_start_coef is not None and self.fit_intercept:
            warm_start_coef = np.append(warm_start_coef,
                                        self.intercept_[:, np.newaxis],
                                        axis=1)

        self.coef_ = list()
        self.intercept_ = np.zeros(n_classes)

        # Hack so that we iterate only once for the multinomial case.
        if self.multi_class == 'multinomial':
            classes_ = [None]
            warm_start_coef = [warm_start_coef]

        if warm_start_coef is None:
            warm_start_coef = [None] * n_classes

        path_func = delayed(logistic_regression_path)

        # The SAG solver releases the GIL so it's more efficient to use
        # threads for this solver.
        backend = 'threading' if self.solver == 'sag' else 'multiprocessing'
        fold_coefs_ = Parallel(n_jobs=self.n_jobs, verbose=self.verbose,
                               backend=backend)(
            path_func(X, y, pos_class=class_, Cs=[self.C],
                      fit_intercept=self.fit_intercept, tol=self.tol,
                      verbose=self.verbose, solver=self.solver, copy=False,
                      multi_class=self.multi_class, max_iter=self.max_iter,
                      class_weight=self.class_weight, check_input=False,
                      random_state=self.random_state, coef=warm_start_coef_,
                      max_squared_sum=max_squared_sum,
                      sample_weight=sample_weight)
            for (class_, warm_start_coef_) in zip(classes_, warm_start_coef))

        fold_coefs_, _, n_iter_ = zip(*fold_coefs_)
        self.n_iter_ = np.asarray(n_iter_, dtype=np.int32)[:, 0]

        if self.multi_class == 'multinomial':
            self.coef_ = fold_coefs_[0][0]
        else:
            self.coef_ = np.asarray(fold_coefs_)
            self.coef_ = self.coef_.reshape(n_classes, n_features +
                                            int(self.fit_intercept))

        if self.fit_intercept:
            self.intercept_ = self.coef_[:, -1]
            self.coef_ = self.coef_[:, :-1]

        return self

    def predict_proba(self, X):
        """Probability estimates.

        The returned estimates for all classes are ordered by the
        label of classes.

        For a multi_class problem, if multi_class is set to be "multinomial"
        the softmax function is used to find the predicted probability of
        each class.
        Else use a one-vs-rest approach, i.e calculate the probability
        of each class assuming it to be positive using the logistic function.
        and normalize these values across all the classes.

        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]

        Returns
        -------
        T : array-like, shape = [n_samples, n_classes]
            Returns the probability of the sample for each class in the model,
            where classes are ordered as they are in ``self.classes_``.
        """
        if not hasattr(self, "coef_"):
            raise NotFittedError("Call fit before prediction")
        calculate_ovr = self.coef_.shape[0] == 1 or self.multi_class == "ovr"
        if calculate_ovr:
            return super(LogisticRegression, self)._predict_proba_lr(X)
        else:
            return softmax(self.decision_function(X), copy=False)

    def predict_log_proba(self, X):
        """Log of probability estimates.

        The returned estimates for all classes are ordered by the
        label of classes.

        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]

        Returns
        -------
        T : array-like, shape = [n_samples, n_classes]
            Returns the log-probability of the sample for each class in the
            model, where classes are ordered as they are in ``self.classes_``.
        """
        return np.log(self.predict_proba(X))

```


### 怎么理解和怎么用好logistic regression?

结合例子，理解LogisticRegression类，以及关键函数fit和predict_proba的输入输出。

```python
# -*- coding: utf-8 -*-
import sklearn.linear_model, random

# 构建数据
# 特征向量有三个值，第一第二个值符合高斯分布，ABCD四个标签对应的平均值不同，第三个是随机数，ABCD不做区分。
# 注意将特征向量和标签同步添加，在两个列表中顺序对应。
featureVecs, labels = [], []
for i in range(25000): #每次迭代创建4个样本，总计10000个样本。
    featureVecs.append([random.gauss(0, 0.5), random.gauss(0, 0.5),
                        random.random()])
    labels.append('A')
    featureVecs.append([random.gauss(0, 0.5), random.gauss(2, 0.),
                        random.random()])
    labels.append('B')
    featureVecs.append([random.gauss(2, 0.5), random.gauss(0, 0.5),
                        random.random()])
    labels.append('C')
    featureVecs.append([random.gauss(2, 0.5), random.gauss(2, 0.5),
                        random.random()])
    labels.append('D')
# fit接受两个等长序列作为参数，前者是特征向量，后者是每个特征向量对应的标签。
# 通过fit函数的返回值，创建一个LogisticRegression类对象，名叫model。
model = sklearn.linear_model.LogisticRegression().fit(featureVecs,
                                                     labels)

# classes_属性就是fit函数输入的labels的种类。
print('model.classes_ =', model.classes_) #直接访问了model的属性。
# 输出：model.classes_ = ['A' 'B' 'C' 'D']
# ---
# coef_是列表的列表，如果不是二分类，它的长度等于标签(classes_)的数量，元素是特征向量的每个分量对相应的class的影响因子。
print('model.coef =', model.coef_)
# 输出：
# model.coef = [[-4.64341152 -4.41153112  0.01183737]
#  [-5.17871915  5.87236929  0.01170626]
#  [ 4.00021738 -4.01591384  0.01597446]
#  [ 4.26874022  5.27542104 -0.11529597]]
for i in range(len(model.coef_)):
    print('For label', model.classes_[i],
          'feature weights =', model.coef_[i])
# 输出：
# For label A feature weights = [-4.68704666 -4.43291562 -0.10498865]
# For label B feature weights = [-5.15305285  5.81255566 -0.07642778]
# For label C feature weights = [ 4.00713522 -3.97348906  0.08631709]
# For label D feature weights = [ 4.34910126  5.37669745 -0.15221423]
# ---
# predict_proba接受特征向量的列表作为参数，返回每个特征向量对应各个标签的概率向量的列表。
# 虽然只有一个特征向量，也要写成列表的列表，输出也要打上[0]，表示列表的第一个结果。
print('[0, 0] probs =', model.predict_proba([[0, 0, 1]])[0])
print('[0, 2] probs =', model.predict_proba([[0, 2, 2]])[0])
print('[2, 0] probs =', model.predict_proba([[2, 0, 3]])[0])
print('[2, 2] probs =', model.predict_proba([[2, 2, 4]])[0])
# 输出样子
# [0, 0] probs = [  9.90415957e-01   4.33298057e-04   9.15043442e-03   3.10454282e-07]
# [0, 2] probs = [  7.25438263e-03   9.80483517e-01   3.54250873e-06   1.22585582e-02]
# [2, 0] probs = [  4.02966065e-03   1.26476971e-08   9.94576901e-01   1.39342538e-03]
# [2, 2] probs = [  5.03697707e-07   1.28278546e-03   1.25916937e-02   9.86125017e-01]
```


### 二分类logistic regression样本例子？

```python
# -*- coding: utf-8 -*-

import sklearn.linear_model, random

# 构建数据
# 特征向量有两个值，符合高斯分布，AD两个标签对应的平均值不同。
# 注意将特征向量和标签同步添加，在两个列表中顺序对应。
featureVecs, labels = [], []
for i in range(20000):
    featureVecs.append([random.gauss(0, 0.5), random.gauss(0, 0.5)])
    labels.append('A')
    featureVecs.append([random.gauss(2, 0.5), random.gauss(2, 0.5)])
    labels.append('D')
model = sklearn.linear_model.LogisticRegression().fit(featureVecs,

# coef_是列表的列表，如果是二分类，它的长度等于1，而不是2，元素是classes中str较大的标签对应的特征向量的影响因子。
print('model.coef =', model.coef_)
print("model.labels =", model.classes_)
# 输出：
# model.coef = [[ 5.78618898  5.94267192]]
# model.labels = ['A' 'D']
print('[0, 0] probs =', model.predict_proba([[0, 0]])[0])
print('[0, 2] probs =', model.predict_proba([[0, 2]])[0])
print('[2, 0] probs =', model.predict_proba([[2, 0]])[0])
print('[2, 2] probs =', model.predict_proba([[2, 2]])[0])
# 输出：
# [0, 0] probs = [  9.99991305e-01   8.69471048e-06]
# [0, 2] probs = [ 0.44212141  0.55787859]
# [2, 0] probs = [ 0.52009144  0.47990856]
# [2, 2] probs = [  7.46755999e-06   9.99992532e-01]
```


### 什么是ROC curve-reciever operating characteristic curve和AUROC-area under ROC？

tradeoff between false positive and false negatives.

tradeoff between sensitivity and specificity. 

plot the true positive rate (sensitivity) against the false positive rate (1 - specificity) for multiple decision thresholds.

对于线性回归模型，知道改变决策阈值所带来的影响非常容易。因此，人们通常使用受试者工作特征曲线8，或称ROC曲线，来形象地表示灵敏度和特异度之间的折衷关系。这种曲线可以绘制出多个决策阈值的真阳性率（灵敏度）和假阳性率（1 - 特异度）之间的关系。

AUROC比较的是多个ROC曲线的性能，即模型的判别能力discrimination of the model。

> 对于一个随机选择的阳性样本，一个好的模型将其标注为阳性的概率应该高于将一个随机选择的阴性样本标注为阳性的概率。

This area is equal to the probability that 
the model will asign a higher probability of 
being positive 
to a randomly chosen positive example than 
to a randomly chosen negative example. 

![](https://ws1.sinaimg.cn/large/006tNc79gy1frmlm98uunj30rs0l5jui.jpg)

logistic regression模型选取阈值p = 0.578，得到

```commandline
准确度=0.659
灵敏度=0.714
特异度=0.586
阳性预测值=0.695
```

与KNN算法相同了。
- 但是这个p值是怎么从ROC曲线中找到的？
- 虚线是随便蒙模型的ROC曲线，它的AUROC就是0.5。


## 24.5 Surviving the Titanic


### 泰坦尼克号的基本信息？

April 15, 1912, the RMS Titanic hit an iceberg and sank in the North Atlantic. 

Of roughly 1300 passengers on board, 832 perished in the disaster.

Whether or not individual passengers survived had an element of randomness, but was far from completely random.


### 怎么读取和构建乘客数据结构？

源文件开头10行：

```txt
1,29.0,F,1,Allen, Miss. Elisabeth Walton
1,0.92,M,1,Allison, Master. Hudson Trevor
1,2.0,F,0,Allison, Miss. Helen Loraine
1,30.0,M,0,Allison, Mr. Hudson Joshua Creighton
1,25.0,F,0,Allison, Mrs. Hudson J C (Bessie Waldo Daniels)
1,48.0,M,1,Anderson, Mr. Harry
1,63.0,F,1,Andrews, Miss. Kornelia Theodosia
1,39.0,M,0,Andrews, Mr. Thomas Jr
1,53.0,F,1,Appleton, Mrs. Edward Dale (Charlotte Lamson)
1,71.0,M,0,Artagaveytia, Mr. Ramon
```
Passenger类，读文件为字典，字典构建实例列表。
```python
# -*- coding: utf-8 -*-

class Passenger(object):
    featureNames = ('C1', 'C2', 'C3', 'age', 'male gender')
#    def __init__(self, pClass, age, gender, survived, name):
#        self.name = name
#        self.featureVec = [0, 0, 0, age, gender]
#        self.featureVec[pClass - 1] = 1
#        #self.featureVec[0] = 0 #Ugly hack
#        self.label = survived
#        self.cabinClass = pClass
#     featureNames = ('C2', 'C3', 'age', 'male gender')
    def __init__(self, pClass, age, gender, survived, name):
        self.name = name
        self.featureVec = [0, 0, 0, age, gender]
        self.featureVec[pClass - 1] = 1
        # 两位二进制本可以表达四个数字
        # if pClass == 2:
        #     self.featureVec = [1, 0, age, gender]
        # elif pClass == 3:
        #     self.featureVec = [0, 1, age, gender]
        # else:
        #     self.featureVec = [0, 0, age, gender] # 这就是一等舱，但是不能计算权重。
        self.label = survived
        self.cabinClass = pClass
    def distance(self, other):
        return minkowskiDist(self.featureVec, other.featureVec, 2)
    def getClass(self):
        return self.cabinClass
    def getAge(self):
        return self.featureVec[3]
    def getGender(self):
        return self.featureVec[4]
    def getName(self):
        return self.name
    def getFeatures(self):
        return self.featureVec[:]
    def getLabel(self):
        return self.label
        
def getTitanicData(fname):
    data = {}
    data['class'], data['survived'], data['age'] = [], [], []
    data['gender'], data['name'] = [], []
    f = open(fname)
    line = f.readline()
    while line != '':
        split = line.split(',')
        data['class'].append(int(split[0]))
        data['age'].append(float(split[1]))
        if split[2] == 'M':
            data['gender'].append(1)
        else:
            data['gender'].append(0)
        if split[3] == '1':
            data['survived'].append('Survived')
        else:
            data['survived'].append('Died')
        data['name'].append(split[4:])
        line = f.readline()
    return data
    
    
def buildTitanicExamples(fileName):
    data = getTitanicData(fileName)
    examples = []
    for i in range(len(data['class'])):
        p = Passenger(data['class'][i], data['age'][i],
                      data['gender'][i], data['survived'][i],
                      data['name'][i])
        examples.append(p)
    print('Finished processing', len(examples), 'passengers\n')    
    return examples
    
```


### 如何评价二分类预测？用哪几个统计量？代码怎么组织？

二分类预测的结果与真实标签相乘，得到混淆矩阵。

用五个统计量描述：
- 准确度——真阳性和真阴性在所有对象中的比例 accuracy
- 敏感度——真阳性在所有阳性中的比例 sensitivity
- 专一度——真阴性在所有阴性中的比例 specificity
- 阳性预测值——真阳性在阳性预测中的比例 positive predicted value
- 阴性预测值——真阴性在阴性预测中的比例 negative predicted value

代码如下：
```python
# -*- coding: utf-8 -*-

def accuracy(truePos, falsePos, trueNeg, falseNeg):
    numerator = truePos + trueNeg
    denominator = truePos + trueNeg + falsePos + falseNeg
    return numerator/denominator

def sensitivity(truePos, falseNeg):
    try:
        return truePos/(truePos + falseNeg)
    except ZeroDivisionError:
        return float('nan')
    
def specificity(trueNeg, falsePos):
    try:
        return trueNeg/(trueNeg + falsePos)
    except ZeroDivisionError:
        return float('nan')
    
def posPredVal(truePos, falsePos):
    try:
        return truePos/(truePos + falsePos)
    except ZeroDivisionError:
        return float('nan')
    
def negPredVal(trueNeg, falseNeg):
    try:
        return trueNeg/(trueNeg + falseNeg)
    except ZeroDivisionError:
        return float('nan')
       
def getStats(truePos, falsePos, trueNeg, falseNeg, toPrint = True):
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    if toPrint:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Pos. Pred. Val. =', round(ppv, 3))
    return (accur, sens, spec, ppv)
```


### 只有1046个样本，用80/20划分训练集和测试集，如何克服偏颇？

多做几次随机划分，求平均值，给95%置信区间，以此数据表明这种方法的有效性。

```python
# -*- coding: utf-8 -*-

def split80_20(examples):
    """
    把实例集用80/20的比例划分为训练集和测试集。
    :param examples: 实例集
    :return: 训练集，测试集
    """
    # 选的是index
    sampleIndices = random.sample(range(len(examples)),
                                  len(examples)//5)
    trainingSet, testSet = [], []
    for i in range(len(examples)):
        # 用index列表做区分
        if i in sampleIndices:
            testSet.append(examples[i])
        else:
            trainingSet.append(examples[i])
    return trainingSet, testSet
    
def randomSplits(examples, method, numSplits, toPrint = True):
    """
    将实例集随机划分多次，运算某种模型得到混淆矩阵的四个值，用各次实验的平均值求四个统计量，可选是否打印，输出混淆矩阵的四个平均值。
    :param examples: 实例集
    :param method: 函数，给他训练集和测试集，给出某种预测的四个统计量
    :param numSplits: 划分多少次，即实验多少次
    :param toPrint: 是否打印统计量
    :return: 真阳性，假阳性，真阴性，假阴性的平均值
    """
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    random.seed(0)
    for t in range(numSplits):
        trainingSet, testSet = split80_20(examples)
        results = method(trainingSet, testSet)
        truePos += results[0]
        falsePos += results[1]
        trueNeg += results[2]
        falseNeg += results[3]
    getStats(truePos/numSplits, falsePos/numSplits,
             trueNeg/numSplits, falseNeg/numSplits, toPrint)
    return truePos/numSplits, falsePos/numSplits,\
             trueNeg/numSplits, falseNeg/numSplits
```


### 怎样把求解模型和应用模型结合起来？

写一个用训练集求解模型的函数，再写一个把模型应用于测试集的函数，用一个函数将二者连接起来，在泰坦尼克名单上多次划分多次运行，求得平均值结果。

```python
# -*- coding: utf-8 -*-

import sklearn
from sklearn.linear_model import LogisticRegression
from em_15_3_flip import stdDev

def buildModel(examples, toPrint = True):
    featureVecs, labels = [],[]
    for e in examples:
        featureVecs.append(e.getFeatures())
        labels.append(e.getLabel())
    model = LogisticRegression().fit(featureVecs, labels)
    if toPrint:
        print('model.classes_ =', model.classes_)
        for i in range(len(model.coef_)):
            print('For label', model.classes_[1])
            for j in range(len(model.coef_[0])):
                print('   ', Passenger.featureNames[j], '=',
                      model.coef_[0][j])
    return model

def applyModel(model, testSet, label, prob = 0.5):
    """
    将logistic regression模型应用于测试集，将对应于第二个标签的概率于阈值比较作为预测依据，输出混淆矩阵的四个值。
    :param model: 用logistic regression和训练集生成的模型
    :param testSet: 测试集
    :param label: prob对应的第二个标签。
    :param prob: 判断阈值，概率大于它，就预测该实例有第二个标签
    :return: 混淆矩阵的四个值
    """
    testFeatureVecs = [e.getFeatures() for e in testSet]
    probs = model.predict_proba(testFeatureVecs)
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for i in range(len(probs)):
        # probs是列表的列表，内层列表长度为2，因为只有Died和Survived两个标签。
        if probs[i][1] > prob:
            if testSet[i].getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else:
            if testSet[i].getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

def lr(trainingData, testData, prob = 0.5):
    """
    调用各函数，用训练集计算logistic regression模型、用测试集运行模型，得到混淆矩阵四值列表。
    :param trainingData: 训练集
    :param testData: 测试集
    :param prob: 对测试集应用模型时，判断是否打标的概率阈值。
    :return: 混淆矩阵四个值组成的元组
    """
    model = buildModel(trainingData, False)
    results = applyModel(model, testData, 'Survived', prob)
    return results
    
```


### 泰坦尼克号幸存者预测模型，如何看各种数据？

写一个testModel函数，构造模型、计算数据，给参数选择是否打印某项相关信息。

如果打印的信息比较复杂，可以单提出来成为一个函数。

```python
# -*- coding: utf-8 -*-
def testModels(examples, numTrials, printStats, printWeights):
    """
    多次运行实例集，测试模型统计性能，可打印特征向量影响权重。
    :param examples: 实例集
    :param numTrials: 实验次数
    :param printStats: 是否打印准确度等统计数据
    :param printWeights: 是否打印特征向量对生还的影响权重
    :return: None
    """
    stats, weights = [], [[], [], [], [], []]
    for i in range(numTrials):
        training, testSet = split80_20(examples)
        xVals, yVals = [], []
        for e in training:
            xVals.append(e.getFeatures())
            yVals.append(e.getLabel())
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        model = sklearn.linear_model.LogisticRegression().fit(xVals,
                                                              yVals)
        for i in range(len(Passenger.featureNames)):
            weights[i].append(model.coef_[0][i])
        truePos, falsePos, trueNeg, falseNeg =\
                         applyModel(model, testSet, 'Survived', prob = 0.44)
        auroc = buildROC(training, testSet, "auroc", False)[0]
        tmp = getStats(truePos, falsePos, trueNeg, falseNeg, False)
        stats.append(tmp + (auroc,))
    print('Averages for', numTrials, 'trials') #下面两个项目至少打印一项，所以这句放在二者外面。
    if printWeights:
        for feature in range(len(weights)):
            featureMean = sum(weights[feature])/numTrials
            featureStd = stdDev(weights[feature])
            print(' Mean weight of', Passenger.featureNames[feature],
              '=', str(round(featureMean, 3)) + ',',
              '95% confidence interval =', round(1.96*featureStd, 3))
    if printStats:
        summarizeStats(stats)


def summarizeStats(stats):
    """
    优化格式，用置信区间的形式，打印多次实验的统计信息。
    :param stats: 元组的列表，多次实验得到的准确度、灵敏度、特异度、阳性预测值和AUROC"
    :return: None
    """
    #定义带置信区间的打印格式
    def printStat(X, name):
        mean = round(sum(X)/len(X), 3)
        std = stdDev(X)
        print(' Mean', name, '=', str(mean) + ',',
               '95% confidence interval =', round(1.96*std, 3))
    #把数据区分出来，分别放入列表中
    accs, sens, specs, ppvs, aurocs = [], [], [], [], []
    for stat in stats:
        accs.append(stat[0])
        sens.append(stat[1])
        specs.append(stat[2])
        ppvs.append(stat[3])
        aurocs.append(stat[4])
    #打印输出
    printStat(accs, 'accuracy')
    printStat(sens, 'sensitivity')
    printStat(specs, 'specificity')
    printStat(ppvs, 'pos. pred. val.')
    printStat(aurocs, 'AUROC')
```

### 泰坦尼克号幸存者预测模型，100次平均性能如何？

```python
# -*- coding: utf-8 -*-

#Look at mean statisics
testModels(examples, 100, True, False)

```

```commandline
Averages for 100 trials
 Mean accuracy = 0.776, 95% confidence interval = 0.05
 Mean sensitivity = 0.736, 95% confidence interval = 0.098
 Mean specificity = 0.805, 95% confidence interval = 0.066
 Mean pos. pred. val. = 0.724, 95% confidence interval = 0.088
 Mean AUROC = 0.839, 95% confidence interval = 0.051
```

比都猜"遇难"要好一点。


### 泰坦尼克号幸存者预测模型，参与预测的几个指标，对生还的影响权重如何？

```python
# -*- coding: utf-8 -*-
#Look at weights
testModels(examples, 100, False, True)
```

```commandline
Averages for 100 trials
 Mean weight of C1 = 1.649, 95% confidence interval = 0.153
 Mean weight of C2 = 0.448, 95% confidence interval = 0.094
 Mean weight of C3 = -0.498, 95% confidence interval = 0.11
 Mean weight of age = -0.031, 95% confidence interval = 0.006
 Mean weight of male gender = -2.368, 95% confidence interval = 0.145
```

一等舱生机大，二等舱有正作用，三等仓有副作用，越年轻越好，男性严重不如女性生机大。


### 泰坦尼克号幸存者预测模型，改变评价概率阈值，几个统计指标如何消长？

```python
# -*- coding: utf-8 -*-

#Look at changing prob
random.seed(0)
trainingSet, testSet = split80_20(examples)
model = buildModel(trainingSet, False)
print('Try p = 0.1')
truePos, falsePos, trueNeg, falseNeg =\
                  applyModel(model, testSet, 'Survived', 0.1)
getStats(truePos, falsePos, trueNeg, falseNeg)
print('Try p = 0.3')
truePos, falsePos, trueNeg, falseNeg = \
    applyModel(model, testSet, 'Survived', 0.3)
getStats(truePos, falsePos, trueNeg, falseNeg)
print('Try p = 0.6')
truePos, falsePos, trueNeg, falseNeg = \
    applyModel(model, testSet, 'Survived', 0.6)
getStats(truePos, falsePos, trueNeg, falseNeg)
print('Try p = 0.9')
truePos, falsePos, trueNeg, falseNeg =\
                  applyModel(model, testSet, 'Survived', 0.9)
getStats(truePos, falsePos, trueNeg, falseNeg)

```

```commandline
Try p = 0.1
 Accuracy = 0.493
 Sensitivity = 0.976
 Specificity = 0.161
 Pos. Pred. Val. = 0.444
Try p = 0.3
 Accuracy = 0.751
 Sensitivity = 0.859
 Specificity = 0.677
 Pos. Pred. Val. = 0.646
Try p = 0.6
 Accuracy = 0.813
 Sensitivity = 0.694
 Specificity = 0.895
 Pos. Pred. Val. = 0.819
Try p = 0.9
 Accuracy = 0.656
 Sensitivity = 0.176
 Specificity = 0.984
 Pos. Pred. Val. = 0.882
```

p不是越大或越小越好，也不是大于0.5就判定是它。看ROC图，调整p阈值，在真阳性和假阳性之间权衡。


### 泰坦尼克号幸存者预测模型，改变评价概率阈值，看ROC图？

```python
# -*- coding: utf-8 -*-

#Look at ROC
random.seed(0)
trainingSet, testSet = split80_20(examples)
sensi_p_pairs = buildROC(trainingSet, testSet, "auroc", plot = True)[1]
```

![](https://ws3.sinaimg.cn/large/006tNc79ly1frnvxtnwr3j30bj08zt92.jpg)

看起来，sensitivity超过0.83就比较平了，再通过提高p值来提高敏感度，会带来严重的假阳性，所以，在sensi和p阈值组成的队列里，找到相应的p，约为0.44.

```python
# -*- coding: utf-8 -*-

#Take a better probability threshold
print(sensi_p_pairs)
print('Try p = 0.44')
truePos, falsePos, trueNeg, falseNeg =\
                  applyModel(model, testSet, 'Survived', 0.44)
getStats(truePos, falsePos, trueNeg, falseNeg)
```

```commandline
0.8941176470588236: 0.22000000000000006, 
0.8823529411764706: 0.25000000000000006, 
0.8705882352941177: 0.2900000000000001, 
0.8588235294117647: 0.36000000000000015, 
0.8470588235294118: 0.4200000000000002, 
0.8352941176470589: 0.4400000000000002, 
0.8117647058823529: 0.49000000000000027, 
0.8: 0.5100000000000002, 
0.788235294117647: 0.5200000000000002, 
0.7647058823529411: 0.5300000000000002, 
0.7529411764705882: 0.5500000000000003,
```

```commandline
Try p = 0.44
 Accuracy = 0.809
 Sensitivity = 0.835
 Specificity = 0.79
 Pos. Pred. Val. = 0.732
```

注意了！

数据量太小，如果不对随机采样分组做random.seed(0)的归零处理，ROC每次都不一样，变化很大。所以几个统计量变化也很大。我这样选p，基于一次的ROC，很不靠谱。


### 泰坦尼克号幸存者预测模型，因为样本小，随机分组ROC变化大，有没有办法克服？

用多次分组多次实验的平均值画ROC。

```python
# -*- coding: utf-8 -*-

def mean_ROC(examples, num_trials, title, plot = True):
    xVals, yVals = [], []
    p = 0.0
    sensi_p_pairs = {}
    while p <= 1.0:
        stats = testModels(examples, num_trials, False, False, p)
        accs, sens, specs, ppvs, aurocs = [], [], [], [], []
        for stat in stats:
            accs.append(stat[0])
            sens.append(stat[1])
            specs.append(stat[2])
            ppvs.append(stat[3])
            aurocs.append(stat[4])
        mean_spec = sum(specs)/len(specs)
        xVals.append(1.0 - mean_spec)
        mean_sensi = sum(sens)/len(sens)
        yVals.append(mean_sensi)
        sensi_p_pairs[mean_sensi] = p
        p += 0.05
    auroc = sklearn.metrics.auc(xVals, yVals, True)
    if plot:
        pylab.plot(xVals, yVals)
        pylab.plot([0,1], [0,1])
        title = 'Averages for ' + str(num_trials) + 'trials ' + title + '\nAUROC = ' + str(round(auroc,3))
        pylab.title(title)
        pylab.xlabel('1 - specificity')
        pylab.ylabel('Sensitivity')
    return sensi_p_pairs
   
   
#Look at the mean ROC
mean_ROC(examples, 20, "auroc", plot = True)
```

平滑很多了
![](https://ws3.sinaimg.cn/large/006tNc79ly1frnvwdy42vj30ms0hojso.jpg)

---
以上，2018-05-25 16:57:16. 书本完结。