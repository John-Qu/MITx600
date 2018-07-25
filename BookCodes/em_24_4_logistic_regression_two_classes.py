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
model = sklearn.linear_model.LogisticRegression().fit(featureVecs, labels)

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
