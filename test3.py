import kf_internal as kf_internal
import numpy as np
import pandas as pd
from numpy.random import randn
import matplotlib
import matplotlib.pyplot as plt
import book_plots as bp
import time
import filterpy


#plt.figure(figsize=(13,3))

df=pd.read_csv('2003.10.22.16.24.13-data-3x.csv')
dflist=df['-0.081'].tolist()
sample_value=200				#this is total number of sample points
zs=dflist[:sample_value-1]

def g_h_filter(data, x0, dx, g, h, dt=1.):
    x = x0
    results = []
    for z in data:
        #prediction step
        x_est = x + (dx*dt)
        dx = dx

        # update step
        residual = z - x_est
        dx = dx    + h * (residual) / dt
        x  = x_est + g * residual     
        results.append(x)  
    return np.array(results)



def predict(pos, movement):
    return (pos[0] + movement[0], pos[1] + movement[1])

def gaussian_multiply(g1, g2):
    mu1, var1 = g1
    mu2, var2 = g2
    mean = (var1*mu2 + var2*mu1) / (var1 + var2)
    variance = (var1 * var2) / (var1 + var2)
    return (mean, variance)


def update(prior, likelihood):
    posterior = gaussian_multiply(likelihood, prior)
    return posterior
t=[]
for i in range (1, sample_value) :
	t.append(i)
	i=i+1


process_var = 20
sensor_var = 2

x=(-0.15 , 100.0)
process_model =(0.,.2)



print('PREDICT\t\t\tUPDATE')
print('     x      var\t\t  z\t    x      var')
xs, predictions = [],[]
for z in zs:
	#perform Kalman filter on measurement z
	prior=predict (x, process_model)
	likelihood=(z, sensor_var)         #this is the sensor observation data mean and variance.
	x = update(prior, likelihood) 

	predictions.append(prior[0])
	xs.append(x[0])
	kf_internal.print_gh(prior, x, z)


print "Filter Value\n"
print xs
plt.plot(t,zs,'g', label='Measurements')
plt.plot(t,xs,'b', label='Filter_value')
plt.plot(t, predictions, 'r', label='predictions')
plt.legend()
plt.title('Filtering the vibrational data')
plt.show()

"""
#G-H Filter applied on the same input .

plt.figure(figsize=(13,5))
ghf=g_h_filter(data=zs, x0=-.3, dx=.4, dt=1., g=.5, h=0.01)
plt.plot(t, zs,'g', label='Measurements')
plt.plot(t,ghf,'b', label='Filtered value')
plt.legend()
plt.title('VIbrational data filter using g-h filter')
plt.show()
"""