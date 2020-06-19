# Aim
#   To plot the variation of Comoving distance and angular diameter distance with redshift.
#   To reproduce this image: https://en.wikipedia.org/wiki/File:CosmoDistanceMeasures_z_to_1e4.png 

# Libraries required: 
#   Obvious: numpy, matplotlib
#   Others: 
#       cosmolopy: To calculate the angular diameter distance and comoving distance        
#       (optional) tqdm: Gives a progress bar for the For loop. Shows how much time the loop will take to complete 


import numpy as np                                                                           
import cosmolopy.distance as cd
import matplotlib.pyplot as plt
import matplotlib
from tqdm.auto import tqdm

# Angular diameter distance (Units: Mpc)

def a_distance(var):
    return cd.angular_diameter_distance(var, **cosmo)

# Comoving distance (Units: Mpc)

def c_distance(var):
    return cd.comoving_distance(var, **cosmo)


# Cosmology 
# Parameters used are taken from Planck 2013

omegam0 = 0.315
omegal = 0.685
h = 0.673
cosmo = {'omega_M_0': omegam0, 'omega_lambda_0': omegal, 'omega_k_0': 0.0, 'h': h}

# Write the data into files so that we can read them later to make the plot

f_a = open("ang_dia_dist_vs_z.txt", 'w')
f_c = open("comov_dist_vs_z.txt", 'w')

# Step size of 0.1 is chosen to get a smooth curve. 
# With step size = 1 we  get a kink near z = 1
# If you are not using tqdm, then run the For loop as - for n in z:

z = np.arange(0, 1000, 0.1)
for n in tqdm(z):
   f_a.write('{}  {}\n'.format(n, a_distance(n))) 
   f_c.write('{}  {}\n'.format(n, c_distance(n))) 
f_a.close()
f_c.close()

# Read files and make the plots

red, a_dist = np.loadtxt('ang_dia_dist_vs_z.txt', unpack = True)
red, c_dist = np.loadtxt('comov_dist_vs_z.txt', unpack = True)

fig, ax = plt.subplots()
plt.xscale('log')
plt.yscale('log')

# 0.0032637977445371 has been multiplied to convert the distance from Mpc to Gly (Giga light years)

plt.plot(red, 0.0032637977445371 * a_dist, label = 'Ang. Dia. Distance')
plt.plot(red, 0.0032637977445371 * c_dist, label = 'Comoving Distance')
plt.xlim(1E-4, 10000)
plt.ylim(0.001, 100)
plt.xticks((1E-4, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000),(1E-4, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000))
plt.yticks((0.001, 0.01, 0.1, 1, 10, 100),(0.001, 0.01, 0.1, 1, 10, 100))
plt.xlabel("Redshift (z)")
plt.ylabel("Distance in Gly")
plt.title("Comparison of distance measures")
plt.grid(True)
plt.savefig("distances_in_cosmology.pdf")
plt.legend()
plt.show()
