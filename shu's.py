import matplotlib.pyplot as plt
import numpy as np
import random
omega = 1
(delta,gamma,timestep,iterations,realizations) = (0, 0.1*omega, (1/100)*(1/omega)*(2*np.pi), 1000, 1000)

# Analytical method
excitedpopana = []
sinecoef = (3*gamma)/np.sqrt(16*omega**2-gamma**2)
frontfactor = (omega**2)/(2*(omega**2)+gamma**2)

for t in range(iterations):
    bothcoef = (np.exp(-3*gamma*t*timestep/4))
    argument = np.sqrt(omega**2 - gamma**2/16)*t*timestep
    r11ana = frontfactor*(1-bothcoef*(np.cos(argument)+sinecoef*np.sin(argument)))
    excitedpopana.append(r11ana)

# Monte Carlo Method
(a,b) = (1,0)

average = np.zeros([iterations,realizations], dtype='float')
for r in range (0,realizations):
    (a,b) = (1,0)
    for i in range (0,iterations):
        average[i][r] += np.abs(np.conj(b)*b)
        da = (1/2j)*timestep*(a*delta+b*omega)
        db = (1/2j)*timestep*(a*omega-b*delta-b*gamma*1j)
        a += da; b += db

        norm = np.conj(a)*a + np.conj(b)*b # normsquared of the updated wavefunction
        if norm <= random.random() :
            (a,b) = (1,0)
        else:
            a /= np.sqrt(norm); b /= np.sqrt(norm)

excitedpopmc = np.zeros(iterations)
excitedpopmcstd = np.zeros(iterations)
for x in range (0,iterations):
    excitedpopmc[x] = np.mean(average[x])
    excitedpopmcstd[x] = np.std(average[x])

mcres = (np.array(excitedpopmc) - np.array(excitedpopana))/excitedpopmcstd #residual
mcres = np.delete(mcres,range(0,50)) #take away first 50 items


#plotting
fig, ax = plt.subplots(2, 1, figsize = [16,9], gridspec_kw={'height_ratios': [3, 1]}, sharex = True)
plt.subplots_adjust(hspace=0)

ax[0].plot(range(iterations),excitedpopana, label = 'Analytic',color = 'green')
#ax[0].plot(range(iterations),excitedpoprk4, label = 'RK4',color = 'red')
ax[0].plot(range(iterations),excitedpopmc,label = 'Monte Carlo',color = 'blue')
ax[0].legend()
#ax[0].xlabel("Time (1/100 of Rabi Period)")
#ax[0].ylabel("Excited State Population Ratio")

#ax[1].plot(range(iterations),rk4res, label = 'RK4', color = 'red')
ax[1].plot(range(50,iterations),mcres, label = 'Monte Carlo', color = 'blue')
ax[1].legend()
