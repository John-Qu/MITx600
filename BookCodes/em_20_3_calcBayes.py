import random
def calcBayes(priorA, probBifA, probB):
    """priorA：A独立于B时的初始概率估计值
       probBifA：A为真时，B的概率估计值
       probB：B的概率估计值
       返回priorA*probBifA/probB"""
    return priorA*probBifA/probB

# priorA = 1/3
priorA = 0.9
prob6ifA = 1/5
prob6 = (1/5 + 1/6 + 1/7)/3

# postA = calcBayes(priorA, prob6ifA, prob6)
# print('Probability of type A =', round(postA, 4))
# postA = calcBayes(postA, prob6ifA, prob6)
# print('Probability of type A =', round(postA, 4))

# postA = calcBayes(priorA, 1 - prob6ifA, 1 - prob6)
# print('Probability of type A =', round(postA, 4))
# postA = calcBayes(postA, 1 - prob6ifA, 1 - prob6)
# print('Probability of type A =', round(postA, 4))

numRolls = 200
postA = priorA
for i in range(numRolls+1):
    if i%(numRolls//10) == 0:
       print('After', i, 'rolls. Probability of type A =',
             round(postA, 4))
    isSix = random.random() <= 1/7 #because die of type C
    if isSix:
        postA = calcBayes(postA, prob6ifA, prob6)
    else:
        postA = calcBayes(postA, 1 - prob6ifA, 1 - prob6)