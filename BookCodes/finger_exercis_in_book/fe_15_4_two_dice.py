import random, pylab
vals = []
for i in range(10000):
    num1 = random.choice(range(1, 7))
    num2 = random.choice(range(1, 7))
    vals.append(num1 + num2)
pylab.hist(vals, bins = 10)
pylab.ylabel("Number of Occurences")

for i in range(1, 7):
    l = "  "*(i-1)
    for j in range(1, 7):
        l += " " + str(i+j)
    print(l)

pylab.show()
