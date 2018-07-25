import random, pylab
vals = []
for i in range(10000):
    num1 = random.choice(range(0, 101))
    num2 = random.choice(range(0, 101))
    vals.append(num1 + num2)
pylab.hist(vals, bins = 10)
pylab.ylabel("Number of Occurences")
pylab.show()