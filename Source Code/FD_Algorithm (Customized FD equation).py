#F-D algorithm (Permutation-Boolean Discrete representation example)


import numpy as np
import matplotlib.pyplot as plt
import itertools
import functools
import random
import math



## F-D System:
# Linear (no chaos, no complexity, no threshold effects, no hysteresis effects, no multipicities of outputs given one input, no response absence...etc)
# Static: the system functionality is constant
# Continuous or Discrete -> Fitness function and Solution representation
# Deterministic: it has a deterministic functioning that is not stochastic (zero shannon entropy)
# Explicit: All input parameters are known and thus not implicit


## Hyperparameters (Metafunctionality/Meta-Model): Hyperparameters don't change, they are fixed apriori
M = 8 #Number of atoms in a molecule
N = 50 # Number of molecules of the system
E_P_Number = 1 #External Perturbation number: number of times we perturb the system externally to steer it towards exploitation direction
Hys = False #Hysteresis effect (only make sense if E_P_Number > 1)
Th = False #Threshold effect
FC =0.5 #Fluctuation/Algorithmic Shaking coefficient (F-D equation)
VC = 0.5 #Lost-Forever Void energy coefficient (F-D Equation)
# FC = VC = 0.5 (always) is a representation of Equipartition theorem as well as Virial theorem

E_P_S = 3 #Strength of external perturbation
S_R = 2 # susceptibilty rate: measure system's sensitivity to perturbation (high susceptibility -> strong response) [Smart-Active Systems]
CF = 0.8 # Cooling factor (closer to one in order to avoid premature convergence by making the cooling process progressive and gradual)
C = 1.5 #Exploitation cost (though not necessary, but it's essential for the algorithm correspodence)

# there are two ways in quantifying the response: EPS-SR threshold relationship (but you lose proportionality) or Etot = SR x EPS (this relationship assumes the linearity of the system thus the proprotionality between Etot and EPS as well as absence of hysteresis effects...etc)
Etot = E_P_S*S_R #Total energy of the system quantifying the strength of the resposne (linear response function)

### Parameters (functionality/model): Parameters change as the algoritm goes
## Parameters Terminology:
# UE = Useful/Utility Energy (Exploitation energy) eg; Electrical energy, Light energy, Kinetic energy, Mechanical Energy...etc (Actuator)
# DHE = Dissipated Heat Energy due to Joule effect (Exploration energy)
# UEC = Useful energy coefficient which measures the percentage of total energy (response strength of the system) that is utile
# DHEC = Dissipated Heat energy coefficient (Total Dissipative forces)  which measures the percentage of total energy that is dissipated due to Joule effect
# FS = global/emergent Fluctuation level via Algorithmic Shaking of molecules (solutions)
# VE = Void Energy that is lost forever due to the 2nd law of thermodynamics (not necessary for the functioning of the algorithm as it acts as a validity test with actual physical theories)
# PS = molecular fluctuation that each molecule receives equally (Equipartition theorem, Virial theorem)


def Cooling(UEC, DHEC):
    DHEC = CF*DHEC
    UEC = 1 - DHEC
    return UEC, DHEC
    
def Total_Energy_Distributor(UEC, DHEC):
    UE = UEC*Etot #Useful/Exploitation energy: initially zero because there is nothing to exploit initially
    DHE = DHEC*Etot #Dissipated-Heat/Exploration energy: initially maximum because all optimization algorithms start with exploration
    return UE, DHE

def Heat_Energy_Distributor(DHE): #This function is a competition between the Fluctuation-Dissipation theorem and 2nd law of thermodynamics
    FS = FC*DHE # Fluctuation-Algorithmic Shaking of solutions
    VE = VC*DHE # Lost forever energy due to the 2nd law of thermodynamics
    return FS # FC = VC = 0.5 (always) is a representation of Equipartition theorem as well as Virial theorem

def Shaking_Distributor(FS):
    PS = FS/N #Individual shaking of each molecule/solution (random seed) [methylating FS-UE conversion instead]
    return PS # All molecuels receive the same amount of shaking per iteration (Equipartition theorem, Virial theorem)

def Fluctuation_Dissipation(UEC,DHEC):
    UEC, DHEC = Cooling(UEC, DHEC)
    UE, DHE = Total_Energy_Distributor(UEC, DHEC)
    FS = Heat_Energy_Distributor(DHE)
    PS = Shaking_Distributor(FS)
    return UE, PS

# Virial theorem and Equipartition theorem operate on the level of Hyperparameters only, especially on the level of DHE = FS + VE (0.5 coefficients) and PS = FS/N
# F-D equation (DHE-FS equation + FS-UE equation): I used a coefficient-driven equation (phenomenological) instead of physical laws (Einstein relation, Johnson-Nyquist equation, Stefan-Boltzmann law, Planck's law  or Kirchhoff's law of Thermal Radiation, Boltzmann-Gibbs distribution)


## Solution representation [context-dependent]: In this example, I will go with Permutation representation: Molecule/Solution = Permutation list of integers (atoms)

## Fitness function: let's take sum fitness function as an example!
def Fitness(L):
    return np.sum(L)

### Solution representation and Fitness function are problem-dependent. I chose simple scenarios to demonstrate the functionality of the algorithm

def Solution_Extraction(BSL):
    BFL = []
    for k in range(len(MS)):
        BFL.append(Fitness(BSL[k]))
    MBF = np.max(BFL)
    BI = BFL.index(MBF)
    Best_Sol = MS[BI]
    return Best_Sol

Max_Iter = 20 
t = 0 
UEC = 0 
DHEC = 1
## Optimization Algorithm structure:
UE = UEC*Etot
DHE = DHEC*Etot
FS = FC*DHE
PS = FS/N
#Initialization: Initialize the population or solution space.
B_M = [] #Base molecule
for j in range(M):
    B_M.append(int(random.uniform(1,10))) #9 types of atoms (permutation representation) or 2 types of atoms (boolean representation: 0 and 1)
G = []
for k in range(N):
    Shuffled_B_M = B_M.copy()
    np.random.shuffle(Shuffled_B_M)
    G.append(Shuffled_B_M)
F = [] #Fitness list
MS = [] #Selected Molecules

while t < Max_Iter:
    #Evaluation: Evaluate each candidate solution using an objective function.
    for j in range(len(G)):
        F.append(Fitness(G[j]))
    #Selection: Select the most promising solutions based on fitness values (Exploitation)
    #Exp_Th = random.uniform(1,Etot) #Exploitation threshold (Exploitation is a one-off operation, at least when chosing one best solution)
    #if UE > Exp_Th: 
        #MS = G[F.index(np.max(F))]
    
    # Or one can deploy UE continuously (more relevant to our algo): 
    while UE > 0:
        Best_Index = F.index(np.max(F))
        MS.append(G[Best_Index]) #Intergenerational comparison as to maximize chances of finding the best solution 
        F.pop(Best_Index)
        UE = UE - C
    #Variation: Generate new offspring solutions through Boltzmannian operators (Exploration)
    for j in range(len(G)):
        sn = int(PS)#int(PS) = amount of shuffled atoms (shaking) of a molecule (Thanks to Equipartition theorem, all molecules have the same PS)
        while sn > 0:
            p = 0
            G[j][p] = int(random.uniform(1,10))
            sn = sn - 1 
            p = p + 1 #the shaking is sequential and not random. But it doesn't matter since sum fitness is commutative
    UE, PS = Fluctuation_Dissipation(UEC, DHEC)
    t = t + 1
#Solution Extraction: Extract the final optimized or near-optimal solution.

Sol = Solution_Extraction(MS)
FFT = Fitness(Sol)

print(Sol)
print(FFT)