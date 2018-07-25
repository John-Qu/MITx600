Exercise 2
1/2 points (graded)
If you wanted to run a simulation that estimates the value of  in a way similar to the Pi estimation shown in lecture, what geometric shape would you throw needles at?


A square, with a smaller square drawn inside it. The smaller square is formed by connecting the larger square's midpoints. incorrect

没法检验箭头是否落在内部正方形里。

A cube with a sphere inscribed inside it.
A flat line ranging from 1 to root 2 and with a subsection that spans from 0 to 1. correct
What introduced the error for Archimedes' method of calculating Pi?


Incorrect conceptual model. correct
Calculation error.
Not enough samples. correct
Explanation:

For Q1, we can approximate using the following code:

def throwNeedles(numNeedles):
    success = 0
    for n in range(numNeedles):
        x = random.random()
        if (1+x)**2 < 2.0:
            success += 1
    sqrt2 = 1+(float(success)/numNeedles)
    return sqrt2                  
                
If the needles fall in the section from 1 to 2 then the ratio of the square of the successful random throws in the unit section between 1 and 2 to the total number of throws will approximate the decimal fraction of root 2. Since we started the lower bound at 1, we have to add 1 to the fraction to get the actual approximation of root 2.
For Q2, Archimedes' method of calculating was not a simulation but a calculation from using polygons. The error came from the fact that Archimedes used polygon approximations instead of circles.
