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

