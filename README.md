# Fluctuation-Dissipation-Algorithm
Introducing the Fluctuation-Dissipation algorithm! An optimization algorithm inspired from statistical physics notions such as the Boltzmann-Gibbs distribution as well as H-theorem, and more precisely Fluctution-Dissipation theorem.This project is a tribute to the genius of Ludwig Boltzmann 

# Fluctuation-Dissipation theorem
Fluctuation-Dissipation theorem (Herbert Callen and Theodore Welton, 1951) is a theorem in statistical physics that entails, in the case of systems obeying detailed balance, that thermodynamic fluctuations can predict the response quantified by impedance/admittance (abstracted notion) and vice versa. Examples include Brownian motion, Johnson noise and Kirchhoff law of Thermal Radiation. The theorem provides a connection between the microscopic behavior of a system (fluctuations) and its macroscopic response (dissipation) in equilibrium conditions.

Susceptibility is a measure of the system's sensitivity to external perturbation (how easy it is to influence or perturb the system) which entails the strength of its response to such perturbation (high susceptibility means strong response).  the relationship between susceptibility and energy dissipation arises from dissipative forces intervening the system-specific physical mechanisms (the redistribution of energy, the generation of excitations, or the relaxation of the system towards equilibrium via moderation law) associated with the system's response to external perturbations (a response is often associated with energy dissipation plus useful energy due to the 2nd law of thermodynamics entailing irreversibility of the macroscopic response as opposed to microscopic reversible fluctuations)

Examples:

Brownian motion (Albert Einstein, 1905): drag forces (air/fluid resistance) dissipates kinetic energy in the form of heat which, due to thermal agitation captured by Boltzmann distribution-factor, is converted to molecular kinetic energy (which is the microscopic definition of temperature). This is well captured by Einstein-Smoluchowski relation D = nuKT.

Johnson-Nyquist noise (John Johnson and Harry Nyquist,1928): in RC circuits, resistors dissipate electrical energy (decreasing electrical current) in the form of Joule-heat energy. However, the current is never exactly zero, and that’s due to the electrons mobility and agitation galvanized by the heat in the wire loop, thus giving back electrical energy (electrons movement). This is captured by the Johnson-Nyquist equation of the mean-square voltage  <V**2> = 4RkT<v>

Thermal radiation(Gustav Kirchhoff ,1860): Kirchhoff law says that the more light a body effectively absorbs (absorbtivity), the more light energy/thermal radiation it will emit

# Systems theory formulation (General formulation):

Systems theoretic formulation of Fluctuation-Dissipation theorem is an input-output formulation of the mechanisms underlying the phenomenon. In fact, one could reformulate most, if not all, of physical laws and theories via systems theory (and specifically, control theory and cybernetics). In the case of F-D theorem, it could be translated into the relationship between the power spectrum S, capture the thermal fluctuations of an observable x(t) around its mean value x(0), and susceptibility (linear response function) X(T) capturing the response function of the dynamical system to an external time-dependent field perturbation f(t). More specifically, the perturbation is on the level of the Hamiltonian of the dynamical system: H(x) = H0(x) - f(t)x. Given that the observable average value is defined as :

![AverageObservable](Images/Avg.png)

Thus, the F-D theorem could be states as: 

![FD equation](Images/PowerSpectrum_Response.png)

Where Sx is the power spectrum representing the fluctuations of x(t): 

![Power Spectrum](Images/PowerSpectrum.png)

f(t) is the oscillatory field perturbing the Hamiltonian:

![Perturbation Field](Images/ExternalPerturbation.png)



