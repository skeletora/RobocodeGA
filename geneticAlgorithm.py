
#!/usr/bin/env python 3

import pandas as pd
import random
import numpy as np

########## VARIABLES AND CONSTANT DEFINITIONS ##########


##### AI BEHAVIOR VARIABLES AND PARAMETERS #####
#Valid options for movement
#   sublists: 0 - movement pattern, 1 - minimum distance, 2 - maximum distance,
#               3 - minimum rotation, 4 - maximum rotation, 5 - max movement delay,
#               6 - movement direction, 7 - movement velocity.
'''
MOVEMENT_OPTIONS = {"pattern"   : [0, 5], "minDist"   : [0, 100], "maxDist"   : [0, 100],
                    "minRot"    : [0, 360], "maxRot"    : [0, 360], "moveDelay" : [0, 10],
                    "moveDir"   : [-1, 1], "moveVel"   : [0, 8]}
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

    def __init__(self, popSize = 10, initPop = None, numParents = 5, numChildren = 2):
        if DEBUG and DEBUG_INIT:
            print("--------------------------------------------------")
            print("STARTING INITIALIZATION")
            print("Creating population with the following parameters:")
            print(f"Population size: {popSize}")
            print(f"Initial population: {initPop}")
            print(f"Number of parents per generation: {numParents}")
            print(f"Number of children per generation: {numChildren}")

        ##### GENETIC ALGORITHM VALID METHODS DEFINITION #####
        self.VALID_FITNESS = {}
        self.VALID_SURVIVOR = {"genitor" : self.Genitor}
        self.VALID_PARENT = {"stochastic" : self.StochasticUnivSampling}
        self.VALID_PROBABILITY = {"score" : self.ScoreBasedProbability}
        self.VALID_RECOMBINATION = {"splice" : self.SpliceGenomes, "weighted average" : self.SimpleArithmRecomb}
        self.VALID_MUTATION = {}

        ##### CLASS VARIABLES #####
        self.generation = 0
        self.nPop = popSize
        self.numParents = numParents
        self.numChildren = numChildren
        self.parents = [] #Will eventually be a list of indexes.
        self.children = self._CreateDataframe(numChildren)

        #initPop is the name of a comma separated variable (csv) file if defined.
        if initPop == None:
            self.population = self._CreateDataframe(popSize)
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

        for i in range(self.nPop):
            self.population.loc[i, "Score"] = 0 # Initializes individual score to zero at start.
            self.population.loc[i, "Probability"] = 0 # Initializes individual probability to zero at start

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
            print("--------------------------------------------------")
            print("INSIDE FITNESS FUNCTION")
        #This would likely read in the file with the scores of each genetic combination.

        if DEBUG and DEBUG_FITNESS:
            print("END OF FITNESS FUNCTION")
            print("--------------------------------------------------")

    def SurvivorSelection(self, survivorMethod = None):
        #NOTE: Will want to modify how survivors are chosen to carry over.  Right now, just bottom of the
        #       dataframe is getting cut off each generation.
        if DEBUG and DEBUG_SURVIVOR:
            print("--------------------------------------------------")
            print("INSIDE SURVIVOR SELECTION")

        if self.generation == 0:
            self.generation = 1
        else:
            if survivorMethod == None:
                survivorMethod = self._FirstKey(self.VALID_SURVIVOR)
            self.VALID_SURVIVOR[survivorMethod]()

        if DEBUG and DEBUG_SURVIVOR:
            print("END OF SURVIVOR SELECTION")
            print("--------------------------------------------------")

    def ParentSelection(self, probMethod = None, parentMethod = None):
        if DEBUG and DEBUG_PARENT:
            print("--------------------------------------------------")
            print("INSIDE PARENT SELECTION")

        if probMethod == None:
            probMethod = self._FirstKey(self.VALID_PROBABILITY)
        if parentMethod == None:
            parentMethod = self._FirstKey(self.VALID_PARENT)

        self.CalcProb(probMethod)
        #self.parents = self.StochasticUnivSampling(5)
        self.parents = self.VALID_PARENT[parentMethod](self.numParents)

        if DEBUG and DEBUG_PARENT:
            print("END OF PARENT SELECTION")
            print("--------------------------------------------------")

    def CalcProb(self, probMethod):
        if DEBUG and DEBUG_PROB:
            print("--------------------------------------------------")
            print("INSIDE CALCPROB")

        self.VALID_PROBABILITY[probMethod]()

        if DEBUG and DEBUG_PROB:
            print("END OF CALCPROB")
            print("--------------------------------------------------")

    def Recombination(self, recombMethod = None, weight = 0.5):
        #NOTE: NEED TO ADD A VALIDATOR TO THE CHILD GENOMES
        if DEBUG and DEBUG_RECOMB:
            print("--------------------------------------------------")
            print("INSIDE RECOMBINATION")

        pairs = []

        #Generate a number of random pairs of parents equal to the number of desired children / 2 rounded up
        for i in range(int(np.ceil(self.numChildren / 2))):
            pairs.append(random.sample(self.parents, 2))

        if recombMethod == None:
            recombMethod = self._FirstKey(self.VALID_RECOMBINATION)

        childCount = 0

        for pair in pairs:
            if DEBUG and DEBUG_RECOMB:
                print(f"Pair: {pair}")
                print(f"childCount: {childCount}")
            self.VALID_RECOMBINATION[recombMethod](pair[0], pair[1], childCount, weight)
            childCount += 2

        if DEBUG and DEBUG_RECOMB:
            print("END OF RECOMBINATION")
            print("--------------------------------------------------")

    def Mutate(self):
        if DEBUG and DEBUG_MUTATE:
            print("Inside the mutate function")

    ########## SUBFUNCTIONS FOR EACH PHASE ##########
    ##### FITNESS SUBFUNCTIONS #####

    ##### SURVIVOR SELECTION SUBFUNCTIONS #####
    def Genitor(self):
        #NOTE: NEED TO CHECK THAT THE SORT IS GOING IN THE CORRECT ORDER (I.E. HIGHEST SCORE IN #1 POSITION)
        if DEBUG and DEBUG_SURVIVOR:
            print("--------------------------------------------------")
            print("INSIDE GENITOR")

        self.population = self.population.sort_values(by = ["Score"], ascending = False)
        self.population = pd.concat([self.population.iloc[:len(self.population.index) - self.numChildren], self.children],
                                    ignore_index = True)

        if DEBUG and DEBUG_SURVIVOR:
            print("END OF GENITOR")
            print("--------------------------------------------------")

    ##### PARENT SELECTION SUBFUNCTIONS #####
    def StochasticUnivSampling(self, numParents):
        """
        Selects parents from population using a Stochastic Universal Sampling algorithm.

        Parameters
        ----------
        numParents : int
            The number of individuals to add to the parent pool.
        """
        if DEBUG and DEBUG_PARENT:
            print("--------------------------------------------------")
            print("INSIDE STOCHASTIC UNIVERSAL SAMPLING")
            print(f"Selecting {numParents} Parents")

        cmlProb = self.population["Probability"].cumsum().tolist()
        parents = []

        currMember = i = 0
        r = random.uniform(0, 1 / numParents)

        if DEBUG and DEBUG_PARENT:
            print(f"Cumulative probability is: {cmlProb}")
            print(f"r is: {r}")

        while currMember < numParents:
            while r <= cmlProb[i] and currMember < numParents:
                parents.append(i)
                r += 1 / numParents
                if DEBUG and DEBUG_PARENT: print(f"r is: {r}")
                currMember += 1

            i += 1

        if DEBUG and DEBUG_PARENT:
            print(f"The parents are:\n{parents}")
            print("END OF STOCHASTIC UNIVERSAL SAMPLING")
            print("--------------------------------------------------")

        return parents

    ##### ASSIGNING PROBABILITY SUBFUNCTIONS #####
    def ScoreBasedProbability(self):
        if DEBUG and DEBUG_PROB:
            print("--------------------------------------------------")
            print("INSIDE SCORE BASED PROBABILITY")

        cmltFitness = self.population["Score"].sum()

        if cmltFitness == 0:
            for row in self.population.index:
                self.population.loc[row, "Probability"] = 1 / len(self.population.index)
        else:
            for row in self.population.index:
                self.population.loc[row, "Probability"] = self.population.loc[row, "Score"] / cmltFitness

        if DEBUG and DEBUG_PROB:
            print("END OF SCORE BASED PROBABILITY")
            print("--------------------------------------------------")

    ##### RECOMBINATION SUBFUNCTIONS #####
    def SpliceGenomes(self, parent1, parent2, childCount, *args):
        if DEBUG and DEBUG_RECOMB:
            print("--------------------------------------------------")
            print("INSIDE SPLICE GENOME")
            print(f"Parent 1 is: {parent1}")
            print(f"Parent 2 is: {parent2}")

        genomeCat = ["Move Pattern","Min Dist","Max Dist","Min Rot", "Max Rot","Move Delay",
                     "Move Dir","Move Vel", "Bullet Pattern","Targeting Pattern"]

        par1 = self.population.loc[parent1, genomeCat].tolist()
        par2 = self.population.loc[parent2, genomeCat].tolist()

        k = int(random.choice(range(len(genomeCat))))

        child1 = par1[0:k] + par2[k:]
        child2 = par2[0:k] + par1[k:]

        i = 0
        for key in genomeCat:
            self.children.loc[childCount, key] = child1[i]
            if childCount + 1 < self.numChildren:
                self.children.loc[childCount + 1, key] = child2[i]
            i = i + 1
        self.children.loc[childCount, ["Score", "Probability"]] = 0
        if childCount + 1 < self.numChildren:
            self.children.loc[childCount + 1, ["Score", "Probability"]] = 0

        if DEBUG and DEBUG_RECOMB:
            print(f"Par1 is: {par1}")
            print(f"Par2 is: {par2}")
            print(f"k is: {k}")
            print(f"child1 is: {child1}")
            print(f"child2 is: {child2}")
            print("END OF SPLICE GENOME")
            print("--------------------------------------------------")

    def SimpleArithmRecomb(self, parent1, parent2, childCount, weight):
        if DEBUG and DEBUG_RECOMB:
            print("--------------------------------------------------")
            print("INSIDE SIMPLE ARITHMETIC RECOMBINATION")
            print(f"Parent 1 is: {parent1}")
            print(f"Parent 2 is: {parent2}")
            print(f"Weight is: {weight}")


        genomeCat = ["Move Pattern","Min Dist","Max Dist","Min Rot", "Max Rot","Move Delay",
                     "Move Dir","Move Vel", "Bullet Pattern","Targeting Pattern"]

        par1 = self.population.loc[parent1, genomeCat].tolist()
        par2 = self.population.loc[parent2, genomeCat].tolist()

        k = int(random.choice(range(len(genomeCat))))

        child1 = par1[0:k]
        child1 = child1 + np.add(np.multiply(par1[k:], 1 - weight), np.multiply(par2[k:], weight)).tolist()
        child2 = par2[0:k]
        child2 = child2 + np.add(np.multiply(par2[k:], 1 - weight), np.multiply(par1[k:], weight)).tolist()

        i = 0
        for key in genomeCat:
            self.children.loc[childCount, key] = child1[i]
            if childCount + 1 < self.numChildren:
                self.children.loc[childCount + 1, key] = child2[i]
            i = i + 1
        self.children.loc[childCount, ["Score", "Probability"]] = 0
        if childCount + 1 < self.numChildren:
            self.children.loc[childCount + 1, ["Score", "Probability"]] = 0

        if DEBUG and DEBUG_RECOMB:
            print(f"Par1 is: {par1}")
            print(f"Par2 is: {par2}")
            print(f"k is: {k}")
            print(f"child1 is: {child1}")
            print(f"child2 is: {child2}")
            print("END OF SIMPLE ARITHMETIC RECOMBINATION")
            print("--------------------------------------------------")

    ##### MUTATION SUBFUNCTIONS #####

    ########## MISC. OTHER FUNCTIONS ##########
    def ValidateGenome(self):
        if DEBUG:
            print("--------------------------------------------------")
            print("INSIDE VALIDATE GENOME")

    def PrintPopStatus(self):
        print(f"Current Generation: {self.generation}")
        print(self.population)

    def _CreateDataframe(self, indexSize):
        dataframe = pd.DataFrame(columns = ["Score", "Move Pattern",
                                                  "Min Dist","Max Dist",
                                                  "Min Rot", "Max Rot",
                                                  "Move Delay", "Move Dir",
                                                  "Move Vel", "Bullet Pattern",
                                                  "Targeting Pattern", "Probability"],
                                 index = [i for i in range(indexSize)])
        return dataframe

    def _FirstKey(self, dict):
        if len(list(dict.keys())) > 0:
            return list(dict.keys())[0]

        raise IndexError("dictionary has no keys")
