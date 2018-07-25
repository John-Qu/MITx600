import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
# CURRENTRABBITPOP = 50
# CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    for i in range(CURRENTRABBITPOP):
        r = random.random()
        if r <= 1 - (CURRENTRABBITPOP/MAXRABBITPOP):
            CURRENTRABBITPOP += 1

def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    for i in range(CURRENTFOXPOP):
        r = random.random()
        if r <= CURRENTRABBITPOP/MAXRABBITPOP and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            rr = random.random()
            if rr <= 1/3:
                CURRENTFOXPOP += 1
        else:
            rrr = random.random()
            if rrr <= 9/10 and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1

            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations, fox_populations = [], []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return rabbit_populations, fox_populations


numSteps = 200
rabbitPopulationOverTime, foxPopulationOverTime = runSimulation(numSteps)

pylab.figure("Number of Rabbits and Foxes")
pylab.plot(range(numSteps), rabbitPopulationOverTime, label="Rabbits")
pylab.plot(range(numSteps), foxPopulationOverTime, label="Foxes")
pylab.title("Number of Rabbits and Foxes")
pylab.legend(loc="best")
pylab.xlabel("Time Steps")
pylab.ylabel("Numbers")

rabit_coeff = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
pylab.plot(pylab.polyval(rabit_coeff, range(len(rabbitPopulationOverTime))))
fox_coeff = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)
pylab.plot(pylab.polyval(fox_coeff, range(len(foxPopulationOverTime))))

pylab.show()
