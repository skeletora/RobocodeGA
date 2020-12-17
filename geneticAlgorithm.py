
#!/usr/bin/env python 3

import pandas as pd
import random
import numpy as np

########## VARIABLES AND CONSTANT DEFINITIONS ##########
#Valid options for movement
#   sublists: 0 - movement pattern, 1 - minimum distance, 2 - maximum distance,
#               3 - minimum rotation, 4 - maximum rotation, 5 - max movement delay,
#               6 - movement direction, 7 - movement velocity.
#NOTE: Might just want to have this as a list with labels
'''
MOVEMENT_OPTIONS = {"pattern"   : [0, 5],
                    "minDist"   : [0, 100],
                    "maxDist"   : [0, 100],
                    "minRot"    : [0, 360],
                    "maxRot"    : [0, 360],
                    "moveDelay" : [0, 10],
                    "moveDir"   : [-1, 1],
                    "moveVel"   : [0, 8]}
'''
MOVEMENT_OPTIONS = [[0, 5], [0, 100], [0, 100], [0, 360], [0, 360],
                    [0, 10], [-1, 1], [0, 8]]

#Valid options for bullet strategy
'''BULLET_STRAT_OPTIONS = {"pattern" : [0, 4]}'''
BULLET_STRAT_OPTIONS = [[0, 4]]

#Valid options for targeting strategies
'''TARGETING_OPTIONS = {"pattern" : [0, 3]}'''
TARGETING_OPTIONS = [[0, 3]]

##### DEBUG VARIABLES AND PARAMETERS #####
DEBUG = True
DEBUG_INIT = True
DEBUG_MAKE_POP = True
DEBUG_FITNESS = True
DEBUG_SURVIVOR = True
DEBUG_PARENT = True
DEBUG_PROB = True
DEBUG_RECOMB = True
DEBUG_MUTATE = True

########## CLASS AND STRUCTURE DEFINITIONS ##########









########## GENETIC ALGORITHM ##########
class GA():
    """
    Attempts to optimize robot performance in Robocode.
    """

    def __init__(self, popSize = 10, initPop = None, numChildren = 2):
        if DEBUG and DEBUG_INIT:
            print("--------------------------------------------------")
            print("STARTING INITIALIZATION")
            print("Creating population with the following parameters:")
            print(f"Population size: {popSize}")
            print(f"Initial population: {initPop}")
            print(f"Number of children per generation: {numChildren}")

        self.generation = 0
        self.nPop = popSize
        self.numChildren = numChildren

        #initPop is the name of a comma separated variable (csv) file if defined.
        if initPop == None:
            self.population = pd.DataFrame(columns = ["Score", "Move Pattern",
                                                      "Min Dist","Max Dist",
                                                      "Min Rot", "Max Rot",
                                                      "Move Delay", "Move Dir",
                                                      "Move Vel", "Bullet Pattern",
                                                      "Targeting Pattern"],
                                            index = [i for i in range(popSize)])
            self.CreatePop()
        else:
            #Converts the csv file into a pandas dataframe.
            self.population = pd.read_csv(initPop)

        if DEBUG and DEBUG_INIT:
            print("FINISHED INITIALIZATION")
            print("--------------------------------------------------")

    def CreatePop(self):
        #Still needs tweaked to fix the movement direction parameter
        #Also still needs adjusted to have accurate values (i.e. float vs. integer)
        if DEBUG and DEBUG_MAKE_POP:
            print("--------------------------------------------------")
            print("CREATING A POPULATION")

        lenCat = len(MOVEMENT_OPTIONS) + len(BULLET_STRAT_OPTIONS) + len(TARGETING_OPTIONS)

        for i in range(self.nPop):
            self.population.iloc[i, 0] = 0
            self.population.iloc[i, lenCat] = 0

            #Set up movement parameters
            for category in range(len(MOVEMENT_OPTIONS)):
                self.population.iloc[i, category + 1] = random.randrange(MOVEMENT_OPTIONS[category][0], MOVEMENT_OPTIONS[category][1])

            #Set up bullet strategy parameters
            for category in range(len(BULLET_STRAT_OPTIONS)):
                self.population.iloc[i, len(MOVEMENT_OPTIONS) + category + 1] = random.randrange(MOVEMENT_OPTIONS[category][0], MOVEMENT_OPTIONS[category][1])

            #Set up the targeting parameters
            for category in range(len(TARGETING_OPTIONS)):
                self.population.iloc[i, len(MOVEMENT_OPTIONS) + len(BULLET_STRAT_OPTIONS) + category + 1] = random.randrange(TARGETING_OPTIONS[category][0], TARGETING_OPTIONS[category][1])

        if DEBUG and DEBUG_MAKE_POP:
            print("FINISHED MAKING POPULATION")
            print("--------------------------------------------------")

    ########## GENETIC ALGORITHM FUNCTIONS ##########

    def FitnessFunc(self):
        if DEBUG and DEBUG_FITNESS:
            print("Inside fitness function")
        #This would likely read in the file with the scores of each genetic combination.

    def SurvivorSelection(self):
        if DEBUG and DEBUG_SURVIVOR:
            print("Inside survivor selection")

        if self.generation == 0:
            self.generation = 1
        else:
            self.population = pd.concat([self.population.iloc[:len(self.population.index) - self.numChildren], self.children],
                                        ignore_index = True)

    def ParentSelection(self):
        if DEBUG and DEBUG_PARENT:
            print("Inside parent selection function")
        #Probably just use the Stochastic Universal Sampling

    def CalcProb(self):
        if DEBUG and DEBUG_PROB:
            print("Calculating probability")
        cmltFitness = self.population["Score"].sum()

        for row in self.population.index:
            self.population.iloc[row, len(self.population.index) - 1] = self.population.iloc[row, 0] / cmltFitness

    def StochasticUnivSampling(self, numParents):
        """
        Selects parents from population using a Stochastic Universal Sampling algorithm.

        Parameters
        ----------
        numParents : int
            The number of individuals to add to the parent pool.
        """
        """
        cmlProb = self.population["probability"].cumsum().tolist()
        parents = []

        #print(cmlProb)

        currMember = i = 0
        r = random.uniform(0, 1 / numParents)

        #print(f"r is: {r}")

        while currMember < numParents:
            while r <= cmlProb[i] and currMember < numParents:
                parents.append(i)
                r += 1 / numParents
                #print(f"r is: {r}")
                currMember += 1

            i += 1

        #print(f"The parents are:\n{parents}")
        """
        return parents

    def Recombination(self):
        if DEBUG and DEBUG_RECOMB:
            print("Inside recombination function")

    def Mutate(self):
        if DEBUG and DEBUG_MUTATE:
            print("Inside the mutate function")

    ########## MISC. OTHER FUNCTIONS ##########
    def PrintPop(self):
        print(self.population)
