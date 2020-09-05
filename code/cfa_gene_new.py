import math
import numpy as np
import matplotlib.pyplot as plt


def calc_value_popu(n0, kg, kc, t):
	n = n0*math.exp((kg-kc)*t)
	
	return n

Kg = 0.0216
Kc = 0.007

K_g = [0.025, 0.07, 0.5, 0.0216, 0.002, 0.0002, 2*10**(-6)]
K_c = [0.0002, 0.0002, 0.0002, 0.007, 0.007,  0.02, 0.1]

font = {'family' : 'serif',
		'weight' : 'normal',
		'size': 12}

y = 'y'
while y == 'y':
	n0 = float(input('Initial number of the population having the gene: '))
	n = n0
	m0 = 100 - n0
	m = m0

	for (kg,kc) in zip(K_g, K_c):
		dt = 0.1
		noof_generations = 100
		t = [i*dt for i in range(int(noof_generations/dt)+1)]
		
		n_vals = [n0]
		m_vals = [m0]
		for i in t[1:]:
			n = calc_value_popu(n0, kg, kc, i)
			n_vals.append(n)
			
			m = calc_value_popu(m0, Kg, Kc, i)
			m_vals.append(m)
		
		prop = []
		for i in range(len(n_vals)):
			proportion = n_vals[i]/(n_vals[i]+m_vals[i])
			prop.append(proportion)


		string = 'K_g = ' + str(kg) + ', K_c = ' + str(kc) + ', Initial start population = ' + str(int(n0))
		plt.figure()
		plt.plot(t,n_vals, linewidth = 3)
		plt.title(string, fontdict = font)
		plt.xlabel('Number of Generations', fontdict = font)
		plt.ylabel('Number of Individuals having the gene', fontdict = font)
		plt.show()

		plt.figure()
		plt.plot(t,prop, linewidth = 3)
		plt.title(string, fontdict = font)
		plt.xlabel('Number of Generations', fontdict = font)
		plt.ylabel('Proportion of Individuals having the gene', fontdict = font)
		plt.show()
	
	y = input('Continue (y/n)? ').lower()