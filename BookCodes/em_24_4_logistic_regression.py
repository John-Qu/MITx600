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