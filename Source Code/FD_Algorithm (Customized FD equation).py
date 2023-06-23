#F-D algorithm (Permutation-Boolean Discrete representation example)


import numpy as np
import matplotlib.pyplot as plt
import itertools
import functools
import random
import math
from scipy.stats import maxwell
from scipy.spatial import distance
from scipy.constants import Boltzmann

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)


## Solution representation [context-dependent]: In this example, I will go with Permutation representation: Molecule/Solution = Permutation list of integers (atoms)

## Fitness function: let's take sum fitness function as an example!
def Fitness(L):
    return np.sum(L)

### Solution representation and Fitness function are problem-dependent. I chose simple scenarios to demonstrate the functionality of the algorithm



kb = Boltzmann #Boltzmann constant


def Boltzmann_Gibbs_Distribution(T,plot):
    Boltzmann_Factor = kb*T #Boltzmann factor
    e = np.linspace(1,100,1000) #Energy states
    exp_term = np.exp(-e/Boltzmann_Factor)
    Pr = exp_term/np.sum(exp_term)
    if plot == True:
        plt.hist(Pr, 1000)
        plt.show()
    return Pr
    
    

def Maxwell_Boltzmann_Distribution(n, plot):
    mean, var, skew, kurt = maxwell.stats(moments='mvsk')
    x = np.linspace(maxwell.ppf(0.01), #list of kinetic energies/speed
                maxwell.ppf(0.99), n)
    MB = maxwell.pdf(x)
    if plot == True:
        fig, ax = plt.subplots(1, 1)
        ax.plot(x, maxwell.pdf(x),
       'r-', lw=5, alpha=0.6, label='maxwell pdf')
    return MB
    
    
def MB_Random_Generator(size):
    r = maxwell.rvs(size)
    return r
    
def Dist_Comparison(dist1, dist2): #One can use K-L divergence, J-S divergence, Variational Distance or Wasserstein distance (Earth Mover's Distance)
    return distance.jensenshannon(dist1, dist2)

def Distribution_Accumulator(v_list): #if one wants to use M-B distribution as termination criterion
    unique_values = list(set(v_list))
    occupation_probabilities = []
    for value in unique_values:
        count = v_list.count(value)
        probability = count / N
        occupation_probabilities.append(probability)

    return occupation_probabilities
    
#For the sake of simplicity, H value is taken to be equal to 1/S
def Entropy_Production(S,Q,T): #Gibbs entropy (not to be confused with conformational entropy or combinatorial entropy)
    S = S + Q/T
    return S

def H_Production(H,S,Q,T): #if one wants to use H value as termination criterion
    S = Entropy_Production(S,Q,T)
    H = 1/S
    return H
    


M = 8 #Number of atoms in a molecule
N = 50 # Number of molecules of the system
E_P_Number = 1 #External Perturbation number: number of times we perturb the system externally to steer it towards exploitation direction
Hys = False #Hysteresis effect (only make sense if E_P_Number > 1)
Th = False #Threshold effect
FC =0.5 #Fluctuation/Algorithmic Shaking coefficient (F-D equation)
VC = 0.5 #Lost-Forever Void energy coefficient (F-D Equation)
# FC = VC = 0.5 (always) is a representation of Equipartition theorem as well as Virial theorem

E_P_S = 3 #Strength of external perturbation
S_R = 2 # susceptibilty rate: measure system's intrinsic sensitivity to perturbation (high susceptibility -> strong response) [Smart-Active Systems]
CF = 0.8 # Cooling factor (closer to one in order to avoid premature convergence by making the cooling process progressive and gradual)
C = 1.5 #Exploitation cost (though not necessary, but it's essential for the algorithm correspodence)
Smax = kb*np.log(factorial(N)) #Maximum entropy 
Hmin = 1/Smax #Minimum H value
MBD = Maxwell_Boltzmann_Distribution(N,False)

# there are two ways in quantifying the response: EPS-SR threshold relationship (but you lose proportionality) or Etot = SR x EPS (this relationship assumes the linearity of the system thus the proprotionality between Etot and EPS as well as absence of hysteresis effects...etc)
Etot = E_P_S*S_R #Total energy of the system quantifying the strength of the resposne (linear response function)



def Cooling(UEC, DHEC): # This function is responsible for incrementally steering the thermodynamic system more and more towards exploitation as the timestep counts
    DHEC = CF*DHEC
    UEC = 1 - DHEC
    return UEC, DHEC
    
def Total_Energy_Distributor(UEC, DHEC): # This function acts as a total energy distributor (pre-actuator) which initially favors Joule energy over utile energy
    UE = UEC*Etot #Useful/Exploitation energy: initially zero because there is nothing to exploit initially
    DHE = DHEC*Etot #Dissipated-Heat/Exploration energy: initially maximum because all optimization algorithms start with exploration
    return UE, DHE

def Heat_Energy_Distributor(DHE): #This function is a competition between the Fluctuation-Dissipation theorem and 2nd law of thermodynamics
    FS = FC*DHE # Fluctuation-Algorithmic Shaking of solutions
    VE = VC*DHE # Lost forever energy due to the 2nd law of thermodynamics
    return FS, VE # FC = VC = 0.5 (always) is a representation of Equipartition theorem as well as Virial theorem

def Shaking_Distributor(FS): # This function is crucial for optimization, responsible for applying Equipartition theorem as to ensure maximum coverage and exploration
    PS = 0.8*FS/N #Individual shaking of each molecule/solution (random seed) [methylating FS-UE conversion instead]
    return PS # All molecuels receive the same amount of shaking per iteration (Equipartition theorem, Virial theorem)

def FD_EE_Feedback_Loop(FS): #Feedback loop between exploration and exploitation via a given FD equation (Dissipation -> Fluctuation [exploration] -> Useful energy [exploitation]
        UE = UE + 0.2*FS
        return UE

def Collision(P1,P2): # Fitness evaluation: This function is based on Molecular Chaos hypothesis breaking via Mutual Information (Cooperation)
    F = Fitness(P1)*Fitness(P2) #Coupled Mutual information
    return F #Out of N particles/molecules, there are N(N-1)/2 total collisions overall (+ N with the wall but that is irrelevant)

def Fluctuation_Dissipation(UEC,DHEC): # This function is a one-for-all that broadly covers all steps of Fluctuation-Dissipation algorithm
    UEC, DHEC = Cooling(UEC, DHEC)
    UE, DHE = Total_Energy_Distributor(UEC, DHEC)
    FS = Heat_Energy_Distributor(DHE)[0]
    PS = Shaking_Distributor(FS)
    IUE = FD_EE_Feedback_Loop(FS)
    UE = UE + IUE
    return UE, PS


# Virial theorem and Equipartition theorem operate on the level of Hyperparameters only, especially on the level of DHE = FS + VE (0.5 coefficients) and PS = FS/N
# F-D equation (DHE-FS equation + FS-UE equation): I used a coefficient-driven equation (phenomenological) instead of physical laws (Einstein relation, Johnson-Nyquist equation, Stefan-Boltzmann law, Planck's law  or Kirchhoff's law of Thermal Radiation, Boltzmann-Gibbs distribution)

F = [] #Fitness list
LM = [] #Loschmidt memory (Aspiration Criteria)

def Solution_Extraction(BSL):
    BFL = []
    for k in range(len(LM)):
        BFL.append(Fitness(BSL[k]))
    MBF = np.max(BFL)
    BI = BFL.index(MBF)
    Best_Sol = LM[BI]
    return Best_Sol

Max_Iter = 20 
t = 0 
S = 0 
UEC = 0 
DHEC = 1
## Optimization Algorithm structure:
UE = UEC*Etot
DHE = DHEC*Etot
FS = FC*DHE
PS = FS/N
T = FS/kb #Temperature
#Initialization: Initialize the population or solution space.
B_M = [] #Base molecule
for j in range(M):
    B_M.append(int(random.uniform(1,10))) #9 types of atoms (permutation representation) or 2 types of atoms (boolean representation: 0 and 1)
G = []
for k in range(N):
    Shuffled_B_M = B_M.copy()
    np.random.shuffle(Shuffled_B_M)
    G.append(Shuffled_B_M)



while t < Max_Iter and Etot > 0 and S < Smax:
    #Evaluation: Evaluate each candidate solution using an objective function.
    for j in range(len(G)):
        F.append(Fitness(G[j]))
    #Selection: Select the most promising solutions based on fitness values (Exploitation)
    #Exp_Th = random.uniform(1,Etot) #Exploitation threshold (Exploitation is a one-off operation, at least when chosing one best solution)
    #if UE > Exp_Th: 
        #LM = G[F.index(np.max(F))]
    
    # Or one can deploy UE continuously (more relevant to our algo): 
    while UE > 0: # This step is similar to Elitism in Genetic algorithms (except it's intergenerational comparison be)
        Best_Index = F.index(np.max(F))
        LM.append(G[Best_Index]) #Intergenerational comparison as to maximize chances of finding the best solution 
        F.pop(Best_Index)
        UE = UE - C
    #Variation: Shake molecules/solutions through Boltzmannian operators (Exploration)
    for j in range(len(G)):
        sn = int(PS)#int(PS) = amount of shuffled atoms (shaking) of a molecule (Thanks to Equipartition theorem, all molecules have the same PS)
        while sn > 0:
            p = 0
            G[j][p] = int(random.uniform(1,10))
            sn = sn - 1 
            p = p + 1 #the shaking is sequential and not random. But it doesn't matter since sum fitness is commutative
    FS = Heat_Energy_Distributor(DHE)[0]        
    VE = Heat_Energy_Distributor(DHE)[1]
    Q = Total_Energy_Distributor(UEC, DHEC)[1]
    UE, PS = Fluctuation_Dissipation(UEC, DHEC)
    T = FS/kb
    S = Entropy_Production(S,Q,T)
    Etot = Etot - VE
    t = t + 1
#Solution Extraction: Extract the final optimized or near-optimal solution.

Sol = Solution_Extraction(LM) #Using Loschmidt memory in aspiration criterion as to avoid having current costful solution (violating molecular chaos hypothesis)
FFT = Fitness(Sol)

print(Sol)
print(FFT)
