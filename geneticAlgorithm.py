
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
MOVEMENT_OPTIONS = {"Move Pattern" : [0, 5],   "Min Dist" : [0, 100], "Max Dist"   : [0, 100],
                    "Min Rot"      : [0, 360], "Max Rot"  : [0, 360], "Move Delay" : [0, 10],
                    "Move Dir"     : [-1, 1],  "Move Vel" : [0, 8]}

#Valid options for bullet strategy
BULLET_STRAT_OPTIONS = {"Bullet Pattern" : [0, 4]}

#Valid options for targeting strategies
TARGETING_OPTIONS = {"Targeting Pattern" : [0, 3]}

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




########## FUNCTION DEFINITIONS ##########





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
        self.VALID_MUTATION = {"gaussian" : self.GaussianMutation}

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

        for i in self.population.index:
            self.population.loc[i, "Score"] = 0 # Initializes individual score to zero at start.
            self.population.loc[i, "Probability"] = 0 # Initializes individual probability to zero at start

            #Set up movement parameters
            for category in MOVEMENT_OPTIONS.keys():
                if category == "Move Dir":
                    self.population.loc[i, category] = random.choice(MOVEMENT_OPTIONS[category])
                else:
                    self.population.loc[i, category] = random.randrange(MOVEMENT_OPTIONS[category][0], MOVEMENT_OPTIONS[category][1] + 1)

            #Set up bullet strategy parameters
            for category in BULLET_STRAT_OPTIONS.keys():
                self.population.loc[i, category] = random.randrange(BULLET_STRAT_OPTIONS[category][0], BULLET_STRAT_OPTIONS[category][1] + 1)

            #Set up the targeting parameters
            for category in TARGETING_OPTIONS.keys():
                self.population.loc[i, category] = random.randrange(TARGETING_OPTIONS[category][0], TARGETING_OPTIONS[category][1] + 1)



        if DEBUG and DEBUG_MAKE_POP:
            print("FINISHED MAKING POPULATION")
            print("--------------------------------------------------")

    ########## GENETIC ALGORITHM PHASE FUNCTIONS ##########

    def FitnessFunc(self, fitMethod = None):
        if DEBUG and DEBUG_FITNESS:
            print("--------------------------------------------------")
            print("INSIDE FITNESS FUNCTION")

        if fitMethod == None:
            fitMethod = self._FirstKey(self.VALID_FITNESS)


        self.VALID_FITNESS[fitMethod]()

        if DEBUG and DEBUG_FITNESS:
            print("END OF FITNESS FUNCTION")
            print("--------------------------------------------------")

    def SurvivorSelection(self, survivorMethod = None):
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
        self.parents = self.VALID_PARENT[parentMethod](numParents = self.numParents)

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
            self.VALID_RECOMBINATION[recombMethod](parent1 = pair[0], parent2 = pair[1], childCount = childCount, weight = weight)
            childCount += 2

        self._FixGenome(self.children)

        if DEBUG and DEBUG_RECOMB:
            print("END OF RECOMBINATION")
            print("--------------------------------------------------")

    def Mutate(self, mutationMethod = None, mutationRate = 0.05, mutationVariance = 1.0):
        if DEBUG and DEBUG_MUTATE:
            print("--------------------------------------------------")
            print("INSIDE MUTATE")
            print(f"Mutation rate is: {mutationRate}")
            print(f"Mutation variation is: {mutationVariance}")

        if mutationMethod == None:
            mutationMethod = self._FirstKey(self.VALID_MUTATION)

        for child in self.children.index:
            if random.random() <= mutationRate:
                self.VALID_MUTATION[mutationMethod](individual = child, mutationVariance = mutationVariance)

        self._FixGenome(self.children)

        if DEBUG and DEBUG_MUTATE:
            print("END OF MUTATE")
            print("--------------------------------------------------")

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
    def SpliceGenomes(self, parent1, parent2, childCount, **kargs):
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
    def GaussianMutation(self, individual, mutationVariance):
        if DEBUG and DEBUG_MUTATE:
            print("--------------------------------------------------")
            print("INSIDE GAUSSIAN MUTATION")

        genomeCat = ["Move Pattern","Min Dist","Max Dist","Min Rot", "Max Rot","Move Delay",
                     "Move Dir","Move Vel", "Bullet Pattern","Targeting Pattern"]

        for category in genomeCat:
            if DEBUG and DEBUG_MUTATE:
                print(f"Before mutation of child {individual} in category {category}: {self.children.loc[individual, category]}")
            self.children.loc[individual, category] = np.random.normal(loc = self.children.loc[individual, category],
                                                                       scale = mutationVariance)
            if DEBUG and DEBUG_MUTATE:
                print(f"After mutation of child {individual} in category {category}: {self.children.loc[individual, category]}")

        if DEBUG and DEBUG_MUTATE:
            print("END OF GAUSSIAN MUTATION")
            print("--------------------------------------------------")

    ########## MISC. OTHER FUNCTIONS ##########
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

    def _Clamp(self,value, minValue, maxValue):
        if DEBUG:
            print("--------------------------------------------------")
            print("INSIDE CLAMP")
            print(f"value: {value} and [min, max]: [{minValue}, {maxValue}]")
            print("END OF CLAMP")
            print("--------------------------------------------------")
        return max(minValue, min(value, maxValue))

    def _FixGenome(self, df):
        #NOTE: STILL NEED TO ADD VALUE CLAMPING AND SET UP TO FIND VALUE RANGES
        if DEBUG:
            print("--------------------------------------------------")
            print("INSIDE FIX GENOME")

        """
        ["Score", "Move Pattern", "Min Dist","Max Dist", "Min Rot", "Max Rot", "Move Delay", "Move Dir",
         "Move Vel", "Bullet Pattern", "Targeting Pattern", "Probability"]
        """
        skipClamp = False

        for index in df.index:
            for column in df.columns:
                if DEBUG:
                    print(f"Rounding {df.loc[index, column]} at ({index}, {column})")

                if column in MOVEMENT_OPTIONS.keys():
                    valRange = MOVEMENT_OPTIONS
                elif column in BULLET_STRAT_OPTIONS.keys():
                    valRange = BULLET_STRAT_OPTIONS
                elif column in TARGETING_OPTIONS.keys():
                    valRange = TARGETING_OPTIONS
                else:
                    skipClamp = True

                if DEBUG:
                    print(f"The value of skipClamp is: {skipClamp}")
                if not skipClamp:
                    df.loc[index, column] = self._Clamp(int(round(df.loc[index, column])),(valRange[column][0]), (valRange[column][1]))
                else:
                    skipClamp = False

        if DEBUG:
            print("END OF FIX GENOME")
            print("--------------------------------------------------")

    def _FirstKey(self, dict):
        if len(list(dict.keys())) > 0:
            return list(dict.keys())[0]

        raise IndexError("dictionary has no keys")
