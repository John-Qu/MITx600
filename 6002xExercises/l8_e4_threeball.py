def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    if numTrials == 0:
        return float("nan")
    import random
    count = 0
    for i in range(numTrials):
        x = random.random()
        if x < 2/5:
            x = random.random()
            if x < 1/4:
                count += 1
    return float(count/numTrials)

print(noReplacementSimulation(1000000))



