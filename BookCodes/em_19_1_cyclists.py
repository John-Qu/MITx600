import pylab, random, scipy
from scipy import stats


treatmentDist = (119.5, 5.0)
controlDist = (120, 4.0)
sampleSize = 100
treatmentTimes, controlTimes = [], []
for s in range(sampleSize):
    treatmentTimes.append(random.gauss(treatmentDist[0],
                                       treatmentDist[1]))
    controlTimes.append(random.gauss(controlDist[0],
                                     controlDist[1]))


controlMean = sum(controlTimes)/len(controlTimes)
treatmentMean = sum(treatmentTimes)/len(treatmentTimes)
print('Treatment mean - control mean =',
      treatmentMean - controlMean, 'minutes')
twoSampleTest = stats.ttest_ind(treatmentTimes, controlTimes,
                                equal_var = False)
print('The t-statistic from two-sample test is', twoSampleTest[0])
print('The p-value from two-sample test is', twoSampleTest[1])


tStat = twoSampleTest[0] #t-statistic for PED-X example
tDist = []
numBins = 1000
for i in range(10000000):
  tDist.append(scipy.random.standard_t(198))


pylab.figure('Test of PED-X')
pylab.plot(range(sampleSize), treatmentTimes, 'bo', label = "Treatment group, mean = " + str(round(treatmentMean, 2)))
pylab.plot(range(sampleSize), controlTimes, 'r^', label = "Treatment group, mean = " + str(round(controlMean, 2)))
pylab.title('Test of PED-X')
pylab.xlabel('Cyclists')
pylab.ylabel('Finishing Time (miniutes)')
pylab.legend(loc = "upper right")


pylab.figure('T-distribution with 198 Degrees of Freedom')
pylab.hist(tDist, bins = numBins,
           weights = pylab.array(len(tDist)*[1.0])/len(tDist))
pylab.axvline(tStat, color = 'w')
pylab.axvline(-tStat, color = 'w')
pylab.title('T-distribution with 198 Degrees of Freedom')
pylab.xlabel('T-statistic')
pylab.ylabel('Probability')

pylab.show()
