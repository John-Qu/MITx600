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