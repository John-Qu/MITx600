# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab
import numpy
''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        p = random.random()
        if p <= self.getClearProb():
            return True
        else:
            return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        r = random.random()
        if r <= self.getMaxBirthProb()*(1-popDensity):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException




class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop


    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses[:]


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        temp_viruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                temp_viruses.append(virus)
        self.viruses = temp_viruses
        popDensity = float(len(temp_viruses)/self.getMaxPop())
        for virus in temp_viruses[:]:
            try:
                temp_viruses.append(virus.reproduce(popDensity))
            except NoChildException:
                continue
        self.viruses = temp_viruses
        return self.getTotalPop()





#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    mean_viruses = numpy.array([0]*300)
    viruses = []
    for j in range(numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    for i in range(numTrials):
        patient = Patient(viruses[:], maxPop)
        # print(patient.getTotalPop())
        total_viruses = []
        for k in range(300):
            total_viruses.append(patient.update())
        mean_viruses += numpy.array(total_viruses)
    mean_viruses = mean_viruses / numTrials
    # print(mean_viruses)
    pylab.figure()
    pylab.plot(range(300), list(mean_viruses), label="SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc="best")
    pylab.show()


def test_simulationWithoutDrug():
    random.seed(0)
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    numTrials = 50

    simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)


# test_simulationWithoutDrug()

# simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
# simulationWithoutDrug(100, 200, 0.2, 0.8, 1)
# Test: simulationWithoutDrug(1, 90, 0.8, 0.1, 1)

#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances.get(drug, False)

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        flag = True
        for drug in activeDrugs:
            flag = flag and self.isResistantTo(drug)
        if flag:
            r = random.random()
            if r <= self.maxBirthProb*(1-popDensity):
                new_resistances = {}
                for drug in self.resistances.keys():
                    rr = random.random()
                    if rr <= self.mutProb:
                        new_resistances[drug] = not self.resistances[drug]
                    else:
                        new_resistances[drug] = self.resistances[drug]
                return ResistantVirus(self.maxBirthProb, self.clearProb, new_resistances, self.mutProb)
            else:
                raise NoChildException
        else:
            raise NoChildException


# def test_ResistanceVirus():
#     virus = ResistantVirus(1.0, 0.0, {}, 0.0)
#     virus = ResistantVirus(0.0, 0.0, {}, 0.0)
#     virus = ResistantVirus(1.0, 1.0, {}, 0.0)
#     virus = ResistantVirus(0.0, 1.0, {}, 0.0)
#     virus = ResistantVirus(0.0, 1.0, {"drug1":True, "drug2":False}, 0.0)
#     # Running
#     virus.reproduce(0, [])
#     # to make sure that resistances are not changed.
#     virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":True}, 0.0)
#     child = virus.reproduce(0, ["drug2"])
#     child = virus.reproduce(0, ["drug1"])
#
#     virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
#     # Reproducing 10 times by calling virus.reproduce(0, [])
#     # Checking the resistances of the children to each of the 6 prescriptions.
#     # Since mutProb = 0.5 and the parent virus was resistant to all 6 drugs, we expect each child to be resistant to, on average, half of the six drugs.
#     # Test completed.
#     virus = ResistantVirus(1.0, 0.0, {"drug2": True}, 1.0)
#     # Making 100 successive generations and testing their resistance to drug2
#     virus = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
#     # Making 100 successive generations and testing their resistance to drug1.
#     virus = ResistantVirus(0.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
#     child = virus.reproduce(0, ["drug2"])
#     child = virus.reproduce(0, ["drug1"])


# test_ResistanceVirus()


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.drugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs[:]

# 它只处理drugResist中的药物，并不管virus是否有抗药性，与PS3的测试之意不符。
    # def getResistPop(self, drugResist):
    #     """
    #     Get the population of virus particles resistant to the drugs listed in
    #     drugResist.
    #
    #     drugResist: Which drug resistances to include in the population (a list
    #     of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])
    #
    #     returns: The population of viruses (an integer) with resistances to all
    #     drugs in the drugResist list.
    #     """
    #     count = 0
    #     for virus in self.viruses:
    #         flag = True
    #         for drug in drugResist:
    #             flag = flag and virus.isResistantTo(drug)
    #         if flag:
    #             count += 1
    #     return count
    #
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        count = 0
        for virus in self.viruses:
            flag = True
            for drug in drugResist:
                flag = flag and virus.isResistantTo(drug)
            for drug in virus.resistances.keys():
                flag = flag and virus.resistances[drug]
            if flag:
                count += 1
        return count


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        temp_viruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                temp_viruses.append(virus)
        self.viruses = temp_viruses
        popDensity = float(len(temp_viruses)/self.getMaxPop())
        for virus in temp_viruses[:]:
            try:
                temp_viruses.append(virus.reproduce(popDensity, self.drugs))
            except NoChildException:
                continue
        self.viruses = temp_viruses
        return self.getTotalPop()


# def test_TreatedPatient():
#     # Test: TreatedPatient 1
#     # Create a TreatedPatient with virus that is never cleared and always reproduces.
#     # Output:
#     virus = ResistantVirus(1.0, 0.0, {}, 0.0)
#     patient = TreatedPatient([virus], 100)
#     # Updating patient for 100 time steps
#     # Test completed.
#
#     # Test: TreatedPatient 2
#     # Create a TreatedPatient with virus that is always cleared and always reproduces.
#     # Output:
#     virus = ResistantVirus(1.0, 1.0, {}, 0.0)
#     patient = TreatedPatient([virus], 100)
#     # Updating patient for 100 time steps Test completed.
#
#     # Test: TreatedPatient 3
#     # Test for adding duplicate prescriptions in TreatedPatient
#     # Output:
#     # Test completed.
#
#     # Test: TreatedPatient 4
#     # Test addPrescription and getPrescription in TreatedPatient.
#     # Output:
#     patient = TreatedPatient([], 100)
#
#     # Output:
#     virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
#     virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
#     virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
#     # patient.getResistPop(['drug1']): 2
#     # patient.getResistPop(['drug2']): 2
#     # patient.getResistPop(['drug1', 'drug2']): 1
#     # patient.getResistPop(['drug3']): 0
#     # patient.getResistPop(['drug1', 'drug3']): 0
#     # patient.getResistPop(['drug1', 'drug2', 'drug3']): 0
#     # # Test completed.
#     # Test: TreatedPatient 6
#     # Test
#     # for virus populations in TreatedPatient.
#
#     # Output:
#     virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
#     virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
#     patient = TreatedPatient([virus1, virus2], 1000000)
#     patient.addPrescription("drug1")

#
# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    mean_total_viruses = numpy.array([0]*300)
    mean_resist_viruses = numpy.array([0]*300)
    viruses = []
    for j in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    for i in range(numTrials):
        patient = TreatedPatient(viruses[:], maxPop)
        total_viruses = []
        resist_viruses = []
        for k in range(150):
            total_viruses.append(patient.update())
            resist_viruses.append(patient.getResistPop(patient.getPrescriptions()))
        patient.addPrescription("guttagonol")
        for k in range(150):
            total_viruses.append(patient.update())
            resist_viruses.append(patient.getResistPop(patient.getPrescriptions()))
        mean_total_viruses += numpy.array(total_viruses)
        mean_resist_viruses += numpy.array(resist_viruses)
    mean_total_viruses = mean_total_viruses / numTrials
    mean_resist_viruses = mean_resist_viruses / numTrials
    pylab.figure()
    pylab.plot(range(300), list(mean_total_viruses), label="TotalVirus")
    pylab.plot(range(300), list(mean_resist_viruses), label="ResistanceVirus")
    pylab.title("ResistanceVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc="best")
    pylab.show()

# numViruses = 100
# maxPop = 1000
# maxBirthProb = 0.1
# clearProb = 0.05
# resistances = {"guttagonol": True}
# mutProb = 0.005
# numTrials = 100
# simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials)

random.seed(0)
simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
