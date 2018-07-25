def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    import random
    count = 0
    for num in range(numTrials):
        num_red, num_green = 4.0, 4.0
        num_balls = num_red + num_green
        draws = 3
        flag_red = True
        for i in range(draws):
            r = random.random()
            if r <= num_red/num_balls:
                num_red -= 1
                num_balls -= 1
            else:
                flag_red = False
                break
        if flag_red:
            count += 1
    return 2*count/numTrials

print(drawing_without_replacement_sim(1000000))

