import scipy.integrate, pylab, random


def gaussian(x, mu, sigma):
    factor1 = (1/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2


tightSD = 1
wideSD = 100
area = round(scipy.integrate.quad(gaussian, -3, 3, (0, tightSD))[0], 4)
print('Probability of being within 3',
      'of true mean of tight dist. =', area)
area = round(scipy.integrate.quad(gaussian, -3, 3, (0, wideSD))[0], 4)
print('Probability of being within 3',
      'of true mean of wide dist. =', area)


def testSamples(numTrials, sampleSize, tightSD=1, wideSD=100):
    tightMeans, wideMeans = [], []
    for t in range(numTrials):
        sampleTight, sampleWide = [], []
        for i in range(sampleSize):
            sampleTight.append(random.gauss(0, tightSD))
            sampleWide.append(random.gauss(0, wideSD))
        tightMeans.append(sum(sampleTight)/len(sampleTight))
        wideMeans.append(sum(sampleWide)/len(sampleWide))
    return tightMeans, wideMeans

sample_size = 4000
tightMeans, wideMeans = testSamples(1000, sample_size, tightSD, wideSD)
pylab.figure('Means of Samples of Size ' + str(sample_size))
pylab.plot(wideMeans, 'y*', label = (' SD = ' + str(wideSD)))
pylab.plot(tightMeans, 'bo', label = ('SD = ' + str(tightSD)))
pylab.xlabel('Sample Number')
pylab.ylabel('Sample Mean')
pylab.title('Means of Samples of Size ' + str(sample_size))
pylab.legend()

pylab.figure('Distribution of wild Sample Means')
pylab.hist(wideMeans, bins = 20, label = (' SD = ' + str(wideSD)))
pylab.title('Distribution of wild Sample Means')
pylab.xlabel('Sample Mean')
pylab.ylabel('Frequency of Occurrence')
pylab.legend()

pylab.figure('Distribution of tight Sample Means')
pylab.hist(tightMeans, bins = 20, label = (' SD = ' + str(tightSD)))
pylab.title('Distribution of tight Sample Means')
pylab.xlabel('Sample Mean')
pylab.ylabel('Frequency of Occurrence')
pylab.legend()

pylab.show()