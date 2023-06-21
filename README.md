# Fluctuation-Dissipation-Algorithm
Introducing the Fluctuation-Dissipation algorithm! An optimization algorithm inspired from statistical physics notions such as the Boltzmann-Gibbs distribution as well as H-theorem, and more precisely Fluctution-Dissipation theorem.This project is a tribute to the genius of Ludwig Boltzmann 

## Fluctuation-Dissipation theorem
Fluctuation-Dissipation theorem (Herbert Callen and Theodore Welton, 1951) is a theorem in statistical physics that entails, in the case of systems obeying detailed balance, that thermodynamic fluctuations can predict the response quantified by impedance/admittance (abstracted notion) and vice versa. Examples include Brownian motion, Johnson noise and Kirchhoff law of Thermal Radiation. The theorem provides a connection between the microscopic behavior of a system (fluctuations) and its macroscopic response (dissipation) in equilibrium conditions.

Susceptibility is a measure of the system's sensitivity to external perturbation (how easy it is to influence or perturb the system) which entails the strength of its response to such perturbation (high susceptibility means strong response).  the relationship between susceptibility and energy dissipation arises from dissipative forces intervening the system-specific physical mechanisms (the redistribution of energy, the generation of excitations, or the relaxation of the system towards equilibrium via moderation law) associated with the system's response to external perturbations (a response is often associated with energy dissipation plus useful energy due to the 2nd law of thermodynamics entailing irreversibility of the macroscopic response as opposed to microscopic reversible fluctuations)

Examples:

### Brownian motion (Albert Einstein, 1905):
Drag forces (air/fluid resistance) dissipates kinetic energy in the form of heat which, due to thermal agitation captured by Boltzmann distribution-factor, is converted to molecular kinetic energy (which is the microscopic definition of temperature). This is well captured by Einstein relation:

![Einstein relation](Images/EinsteinRelation.png)

### Johnson-Nyquist noise (John Johnson and Harry Nyquist,1928):
In RC circuits, resistors dissipate electrical energy (decreasing electrical current) in the form of Joule-heat energy. However, the current is never exactly zero, and that’s due to the electrons mobility and agitation galvanized by the heat in the wire loop, thus giving back electrical energy (electrons movement). This is captured by the Johnson-Nyquist equation of the mean-square voltage:

![Johnson Nyquist equation](Images/JN_Equation.png)

### Thermal radiation (Gustav Kirchhoff ,1860):
Kirchhoff law says that the more light a body effectively absorbs (absorbtivity), the more light energy/thermal radiation it will emit. This is mathematically written in the form of absorptivity = emissivity:

![Kirchhoff's law](Images/Kirchhoff_Law.png)

## Systems theory formulation (General formulation):

Systems theoretic formulation of Fluctuation-Dissipation theorem is an input-output formulation of the mechanisms underlying the phenomenon. In fact, one could reformulate most, if not all, of physical laws and theories via systems theory (and specifically, control theory and cybernetics). In the case of F-D theorem, it could be translated into the relationship between the power spectrum S, capture the thermal fluctuations of an observable x(t) around its mean value x(0), and susceptibility (linear response function) X(T) capturing the response function of the dynamical system to an external time-dependent field perturbation f(t). More specifically, the perturbation is on the level of the Hamiltonian of the dynamical system: H(x) = H0(x) - f(t)x. Given that the observable average value is defined as :

![AverageObservable](Images/Avg.png)

Thus, the F-D theorem could be states as: 

![FD equation](Images/PowerSpectrum_Response.png)

Where Sx is the power spectrum representing the fluctuations of x(t): 

![Power Spectrum](Images/PowerSpectrum.png)

f(t) is the oscillatory field perturbing the Hamiltonian:

![Perturbation Field](Images/ExternalPerturbation.png)

## Microscopic Reversibility

Microscopic time-reversibility is a fundamental principle in physics and chemistry. It states that the microscopic dynamics of particles are time-reversible because the microscopic equations of motion are symmetric with respect to inversion in time (T-symmetry) entailing microscopic information conversation [Noether’s theorem]. There are 3 macroscopic consequences of the microscopic reversibility property: Principle of Detailed Balance,  Wegscheider's conditions for the generalized mass action law and Onsager Reciprocal relations


### Principle of Detailed Balance:
1- The principle of detailed balance (L. Boltzmann, 1872): Statistical description of macroscopic/mesoscopic systems/processes as statistical ensembles (probability distributions over microstates) of elementary processes (collisions, reactions…etc) where, given thermodynamic equilibrium, every elementary process is equilibrated with its own reverse process with the same average rate of taking place. The principle of detailed balance was used in Boltzmann equation as to prove H-theorem concerning the Entropy Production (Principle of detailed balance is a sufficient but not necessary condition for entropy increase). That said, microscopic reversibility was used by L. Boltzmann to prove, as strange as that sounds, macroscopic irreversibility. The principle of detailed balance was also used by James Clerk Maxwell in his gas kinetics works as well as Albert Einstein (1916) in his works on Photoelectric effect and quantum theory of emission-absorption of light.

### Wegscheider's conditions for the generalized mass action law
2- Wegscheider's conditions for the generalized mass action law (Wegscheider, 1901): Wegscheider's conditions for the generalized mass action law establish the criteria necessary for its applicability in chemical kinetics. These conditions emphasize the concept of microscopic reversibility, which states that the forward and reverse reactions occur at the same rate on a molecular level. To satisfy Wegscheider's conditions, the reaction must be in chemical equilibrium, take place in a uniform system, involve elementary steps, have the slowest step determine the rate, and reach local equilibrium at each step. Additionally, it should not involve significant side reactions. By meeting these requirements, the generalized mass action law accurately describes how the rate of a reaction relates to the concentrations of the species involved, with a foundational reliance on the reversibility of microscopic processes


### Onsager Reciprocal relation
3- Onsager Reciprocal relation (L. Onsager, 1931): The Onsager reciprocal relations are mathematical relationships that describe the symmetry of transport phenomena in equilibrium systems. They state that the transport coefficients, which relate fluxes of different quantities to their corresponding driving forces, have a reciprocal relationship. These relations ensure that the transport processes follow specific symmetries and are applicable in various fields such as physics, chemistry, and engineering. By understanding these relations, we can predict and analyze transport properties in complex systems.

## How can this be exploited algorithmically? 
Algorithmic Correspondence Rule of Thumb: Specificity = Don’t restrict development to analogies and metaphors only. Instead, integrate actual functionalities and mechanisms (control flow of the code) from nature on top of mere analogies and metaphors.
### Population algorithms steps:

1. Self-adaptation: Different particles randomly exploring optimal solutions in the search space (Exploration = 1)
2. Cooperation: Information exchange between particles in order to steer the collective ensemble towards more search regions where optimal solutions might exist but it is a good practice that a subset of the collective ensemble continue on random search (1/2 Exploration-1/2 Exploitation)
3. Competition: Selection, filtration and survival based on comparison between each particle’s fitness function (Exploitation = 1)

### Algorithm components:
1. Depth: the cost of the current (best) solution → tabu tenure, memory structure and aspiration criteria
2. Mobility: the ability to rapidly move to different areas of the search space (whilst keeping the cost low);
3. Coverage: how systematically the search covers the search space, the maximum distance between any unexplored assignment and all visited assignments.

### Exploration-Exploitation paradigm:

Exploitation [exploiting the current knowledge/solutions] = Energy Dissipation (Joule-heat energy [drag, resistor, absorption]) (Macroscopic-Mesoscopic = Irreversible) = Replacement and Selection

Exploration [exploring the search space]= Thermodynamic fluctuation-driven Shaking (kinetic energy via Brownian motion, electrical energy via Johnson Noise, light energy via Thermal Radiation[Kirchhoff's law of TR]) (Microscopic = Reversible) = Delaying replacement

### Optimization Algorithm control flow (Flowchart):
1. External Perturbation of the system
2. Susceptibility tuning [handling of system-specific physical mechanisms]
3. Dissipative forces tuning [2nd law of thermodynamics]
4. System response function (useful energy + dissipated heat energy)
5. Etot = UE + DHE [Etot distribution tuning]
6. UE is used for exploitation (competition step) while DHE is fed back into the system microscopic particles (positive feedback loop due to Fluctuation-Dissipation theorem and Microscopic reversibility)
7. Fluctuation of particles used for exploration (self-adaptation step) of further solutions
8. Finding other near-optimal solutions if possible
9. particles fluctuation acting as a pseudo-perturbation (weaker actually) via information exchange/communication protocol (collaboration step)
10. Steering the macroscopic system towards favorable solutions found by particles fluctuations
11. DHE conversion to UE (positive feedback loop due to Fluctuation-Dissipation theorem and Microscopic reversibility)
12. Repeat until Etot tapers off to zero (preferably with unbalancing Etot distribution towards UE more than DHE as the algorithm goes)

### Algorithm Hyperparameter tuning (Algorithm meta-functionality/model-parameters):
1. M = 8 #Number of atoms in a molecule
2. N = 50 # Number of molecules of the system
3. E_P_Number = 1 #External Perturbation number: number of times we perturb the system externally to steer it towards exploitation direction
4. Hys = False #Hysteresis effect (only make sense if E_P_Number > 1)
5. Th = False #Threshold effect
6. FC =0.5 #Fluctuation/Algorithmic Shaking coefficient (F-D equation)
7. VC = 0.5 #Lost-Forever Void energy coefficient (F-D Equation)
#### FC = VC = 0.5 (always) is a representation of Equipartition theorem as well as Virial theorem
8. E_P_S = 3 #Strength of external perturbation
9. S_R = 2 # susceptibilty rate: measure system's sensitivity to perturbation (high susceptibility -> strong response) [Smart-Active Systems]
10. CF = 0.8 # Cooling factor (closer to one in order to avoid premature convergence by making the cooling process progressive and gradual)
11. C = 1.5 #Exploitation cost (though not necessary, but it's essential for the algorithm correspodence)

#### there are two ways in quantifying the response: EPS-SR threshold relationship (but you lose proportionality) or Etot = SR x EPS (this relationship assumes the linearity of the system thus the proprotionality between Etot and EPS as well as absence of hysteresis effects...etc)
10. Etot = E_P_S*S_R #Total energy of the system quantifying the strength of the resposne (linear response function)



### Algorithm Parameter tuning (Algorithm functionality/model-parameters):
1. UE = Useful/Utility Energy (Exploitation energy) eg; Electrical energy, Light energy, Kinetic energy, Mechanical Energy...etc (Actuator)
2. DHE = Dissipated Heat Energy due to Joule effect (Exploration energy)
3. UEC = Useful energy coefficient which measures the percentage of total energy (response strength of the system) that is utile
4. DHEC = Dissipated Heat energy coefficient (Total Dissipative forces)  which measures the percentage of total energy that is dissipated due to Joule effect
5. FS = global/emergent Fluctuation level via Algorithmic Shaking of molecules (solutions)
6. VE = Void Energy that is lost forever due to the 2nd law of thermodynamics (not necessary for the functioning of the algorithm as it acts as a validity test with actual physical theories)
7. PS = molecular fluctuation that each molecule receives equally (Equipartition theorem, Virial theorem)

### F-D equation: capturing the conversion mechanism between DHE, Algorithmic Shaking and UE = DHE-AS equation + AS-UE energy:

1. Einstein-Smoluchowski relation
2. Johnson-Nyquist equation
3. Stefan-Boltzmann law
4. Wien’s approximation law
5. Planck’s law
6. Kirchhoff’s law
7. Boltzmann-Gibbs distribution
8. Customized equation (phenomenological via coefficients)

### Implementation mode of Etot:
1. UE = Exploitation, DHE = Exploration (via F-D): In this case, the external perturbation is purported to exploit the solutions found so far, this is captured in the useful/utility energy whilst the rest of energy is ‘'wasted’' in the form of dissipated Joule-heat energy which, according to F-D theorem, is partially (due to 2nd law of thermodynamics/entropy production) or fully (customized scenario) converted back to: [1st scenario] useful energy while the rest is converted to reverse process in the form of fluctuations via algorithmic shaking (random shuffling). [2nd scenario]: fluctuations via algorithmic shaking (random shuffling) while the rest is converted into void energy that is irreversibly lost forever (2nd law). [3rd scenario]: useful energy while the rest is converted into void energy that is irreversibly lost forever (2nd law)
2. UE = ‘'wasted’'void energy in the sense of the optimization algorithm, DHE = Exploitation: less realistic scenario but this is more compatible with the positive feedback loop system in the sense that dissipation heat energy is resulting from exploiting solutions (acting as dissipative forces themselves), and this DHE is partially or fully converted into fluctuations via algorithmic shaking while the rest is lost in void, particles fluctuate and explore other solutions, and in the process, they get to dissipate energy which is going to be harnessed in exploitation thus the following cycle: DHE [exploitation]→ fluctuations [exploration] → DHE → fluctuations…etc with void being optional.

### Fluctuation-Dissipation theorem as a feedback loop between Exploration and Exploitation: 


