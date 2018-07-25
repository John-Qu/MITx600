嗯，术业有专攻，这才是Prof范。@庞松 你现在还是摄像？转制片了？

## Exercise 1-1
6/6 points (graded)

For the following explanations of different types of programmatic models, fill in the blank with the appropriate model the definition describes.

A ______ model is one whose behavior is entirely predictable. Every set of variable states is uniquely determined by parameters in the model and by sets of previous states of these variables. Therefore, these models perform the same way for a given set of initial conditions, and it is possible to predict precisely what will happen.

 correct  deterministic
 
A ________ model is one in which randomness is present, and variable states are not described by unique values, but rather by probability distributions. The behavior of this model cannot be entirely predicted.

 correct  stochastic
 
A _______ model does not account for the element of time. In this type of model, a simulation will give us a snapshot at a single point in time.

 correct  static
 
A _______ model does account for the element of time. This type of model often contains state variables that change over time.

 correct  dynamic
 
A _______ model does not take into account the function of time. The state variables change only at a countable number of points in time, abruptly from one state to another.

 correct  discrete
 
A ______ model does take into account the function of time, typically by modelling a function f(t) and the changes reflected over time intervals. The state variables change in an unbroken way through an infinite number of states.

 correct  continuous
 

## Exercise 1-2
3/3 points (graded)

1. If you are using differential equations to model a simulation, are you more likely to be doing a discrete or continuous model?


- Discrete
- Continuous correct

2. Let's say you run a stochastic simulation 100 times. How many times do you need to run the simulation again to get the same result?


- 1 time
- 99 times
- 100 times
- 101 times
- All of the above will give you the same result.
- None will necessarily give you the same result. correct

3. Which modelling system would be best to model a bank account?

- Discrete
- Continuous
- Either discrete or continuous would work, depending on the specifics of the model you wish to use. correct

## Exercise 4
0/3 points (graded)

1. Are the following two distributions equivalent?

import random
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 

Yes correct
No incorrect
Explanation:

The random.random() distribution is uniform, so both dist1 and dist2 are a uniform distribution over [-1.0, 1.0).

我想因为乘了2，"密度"不一样。原来没区别。

2. Are the following two distributions equivalent?

import random
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

Yes correct
No incorrect

Explanation:

The random.random() distribution is uniform, and so is the random.randrange() distribution, so both dist3 and dist4 are a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

Are the following two distributions equivalent?

import random
def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)

Yes incorrect
No correct
Explanation:

The random.random() distribution is uniform, and so is the random.randint() distribution. However unlike random.randrange(start, end), random.randint(start, end) returns a distribution that is inclusive of both the given start and end points.

Thus dist5 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], but dist6 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

You can code a simple simulation to see what a distribution looks like using dictionaries:

d1 = {}
for i in range(10000):
    x = random.randrange(10) 
    d1[x] = d1.get(x, 0) + 1
d2 = {}
for i in range(10000):
    x = int(random.random()*10)
    d2[x] = d2.get(x, 0) + 1
d3 = {}
for i in range(10000):
    x = random.randint(0, 10)
    d3[x] = d3.get(x, 0) + 1
    
Examine the values of the three dictionaries to see what sort of distribution results!

Question to ponder: Should all the values of the dictionaries be equal? That is, should d1[x] == d1[y] for all values of x and y, where x != y and both x and y are values in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]?