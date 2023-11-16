# Quantum_Computing
Here is the illustration for the code:
Main.py: It contains the main function and it is the function to run:

One_complete_evolution: for a single particle do 1 evolution within a timestep.

One_particle: for a single particle do 1 complete trajectory in the total time.

Task, parallel: for the multiprocessing. I expect it will take ages to compute so I introduce this method, but I found your way are clear and effective lol. You may ignore this part because these are only for accelerating the speed of calculation.

Unpack, plot_flag: for plotting graphs.


functions.py: It contains the used functions that helps make it clear:
density_matrix: for OBE but not used yet
 
evolution: function to calculate the wavefunction at the next time step
 
comparison: function to make comparison between random number and the norm
 
inner: function to calculate the inner product
 
daga: function to calculate the daga operator.
 (some unstated functions are useless and will be deleted.)

 
parameters.py: It contains some of the unchanged parameters that used.

try run it on the jupyter notebook on university server
