import pylab
vals = []
for i in range(10):
    vals.append(3**i)
pylab.plot(vals,'ko', label = 'Actual points')
xVals = pylab.arange(10)
fit = pylab.polyfit(xVals, vals, 5)
yVals = pylab.polyval(fit, xVals)
pylab.plot(yVals, 'bx', label = 'Predicted points',
           markeredgewidth = 2, markersize = 15)
pylab.title('Fitting y = 3**x')
pylab.legend(loc = 'upper left')

print('Model predicts that 3**20 is roughly',
      # pylab.polyval(fit, [3**20])[0])
    pylab.polyval(fit, 3**20))
print('Actual value of 3**20 is', 3**20)

xVals, yVals = [], []
for i in range(10):
    xVals.append(i)
    yVals.append(3**i)
pylab.figure()
pylab.plot(xVals, yVals, 'k')
pylab.semilogy()

pylab.show()
