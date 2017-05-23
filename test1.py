import numpy as np
from numpy.random import randn
import kf_internal as kf_internal
import matplotlib
import matplotlib.pyplot as plt
import book_plots as bp
import time





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


#normal kf mode update and predict step
np.random.seed(13)

process_var = 1. # variance in the dog's movement
sensor_var = 2. # variance in the sensor

x = (-0.01,2.)  # dog's position, N(0, 20**2)
velocity = 1
dt = 1. # time step in seconds
process_model = (velocity*dt, process_var) 

zs=[]             #create a list of measurements

xs, predictions = [],[]


for z in zs:
	#perform Kalman filter on measurement z
	prior=predict (x, process_model)
	likelihood=(z, sensor_var)         # #this is the sensor observation data mean and variance.
	x = update(prior, likelihood) 

	predictions.append(prior[0])
    xs.append(x[0])
    kf_internal.print_gh(prior, x, z)

print('final estimate:        {:10.3f}'.format(x[0]))
print('actual final position: {:10.3f}'.format(dog.x))





"""
xs = range(500)
ys = randn(500)*1 + 10.
plt.plot(xs, ys)
plt.show()
print('Mean of readings is {:.3f}'.format(np.mean(ys)))
"""
