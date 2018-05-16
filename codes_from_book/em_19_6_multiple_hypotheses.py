import random, scipy
from scipy import stats # 不加这一句，python3报scipy没有stats属性。
numHyps = 20
sampleSize = 200 #这里的值越大，越容易保证有一次5%即1/20的机会推翻原假设。
population = [] #注意，只有一个总体
for i in range(5000): #Create large population
    population.append(random.gauss(0, 1))
sample1s, sample2s = [], []
for i in range(numHyps): #Generate many pairs of small samples
    sample1s.append(random.sample(population, sampleSize))
    sample2s.append(random.sample(population, sampleSize))
#Check pairs for statistically significant difference
numSig = 0
for i in range(numHyps):
    if scipy.stats.ttest_ind(sample1s[i], sample2s[i])[1] < 0.05:
        numSig += 1
print('Number of statistically significant (p < 0.05) results =',
       numSig)