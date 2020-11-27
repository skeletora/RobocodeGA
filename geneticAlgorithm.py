
#!/usr/bin/env python 3

import pandas as pd
import random
import numpy as np

########## VARIABLES AND CONSTANT DEFINITIONS ##########
#Valid options for movement
#   sublists: 0 - movement pattern, 1 - minimum distance, 2 - maximum distance,
#               3 - minimum rotation, 4 - maximum rotation, 5 - max movement delay,
#               6 - movement direction, 7 - movement velocity.
#NOTE: Might just want to have this a a list with labels
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

########## CLASS AND STRUCTURE DEFINITIONS ##########









########## GENETIC ALGORITHM ##########
class GA():
    """
    Attempts to optimize robot performance in Robocode.
    """

    def __init__(self, popSize = 10, initPop = None, numChildren = 2):
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

    def CreatePop(self):
        #Still needs tweaked to fix the movement direction parameter
        print("making a population")
        lenCat = len(MOVEMENT_OPTIONS) + len(BULLET_STRAT_OPTIONS) + len(TARGETING_OPTIONS)

        for i in range(self.nPop):
            self.population.iloc[i, 0] = 0
            self.population.iloc[i, lenCat] = 0

            for category in range(len(MOVEMENT_OPTIONS)):
                self.population.iloc[i, category + 1] = random.randrange(MOVEMENT_OPTIONS[category][0], MOVEMENT_OPTIONS[category][1])

            for category in range(len(BULLET_STRAT_OPTIONS)):
                self.population.iloc[i, len(MOVEMENT_OPTIONS) + category + 1] = random.randrange(MOVEMENT_OPTIONS[category][0], MOVEMENT_OPTIONS[category][1])

            for category in range(len(TARGETING_OPTIONS)):
                self.population.iloc[i, len(MOVEMENT_OPTIONS) + len(BULLET_STRAT_OPTIONS) + category + 1] = random.randrange(TARGETING_OPTIONS[category][0], TARGETING_OPTIONS[category][1])

    def FitnessFunc(self):
        print("Inside fitness function")
        #This would likely read in the file with the scores of each genetic combination.

    def SurvivorSelection(self):
        print("Inside survivor selection")

        if self.generation == 0:
            self.generation = 1
        else:
            self.population = pd.concat([self.population.iloc[:len(self.population.index) - self.numChildren], self.children],
                                        ignore_index = True)

    def ParentSelection(self):
        print("Inside parent selection function")
        #Probably just use the Stochastic Universal Sampling

    def CalcProb(self):
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
        print("Inside recombination function")

    def Mutate(self):
        print("Inside the mutate function")
