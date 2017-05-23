#Here i am applying filterpy library. (custom dataset(vibration data, bearing IMS))


import numpy as np
import pandas as pd
import filterpy
from filterpy.kalman import KalmanFilter
import matplotlib 
import matplotlib.pyplot as plt
sample_value=20

df=pd.read_csv('2003.10.22.16.24.13-data-3x.csv')
dflist=df['-0.081'].tolist()
z=dflist[:sample_value]

kf=KalmanFilter(dim_x=1 , dim_z=1)
xi, Pi=-0.10 ,  20.
i=0
count=0
x_predicted, P_predicted=[],[]
x_updated, P_updated=[],[]
while count<sample_value :
	xp,Pp=filterpy.kalman.predict(xi,Pi,F=1, Q=100., u=0, B=0, alpha=1.0)     #have doubt in f variable
	xu,Pu=filterpy.kalman.update(xp,Pp,z[i],R=85)
	x_predicted.append(xp)
	P_predicted.append(Pp)
	x_updated.append(xu)
	P_updated.append(Pu)
	i=i+1
	xp=xu
	print xp
	Pp=Pu
	print Pp
	count=count+1

#we will now plot the predicted value and then the updated value along with the obseravational data
t=[]
for j in range (1, sample_value+1) :
	t.append(j)
	j=j+1


plt.figure(figsize=(13,3))
plt.plot(t,z,'g', label='Measurements')
plt.plot(t,x_updated,'b', label='Filter_value')
plt.plot(t, x_predicted, 'r', label='predictions')
plt.legend()
plt.title('Filtering the vibrational data')
plt.show()
















"""
	xminus, Pminus = kf.predict(x=-0.1, P=1., u=1. , Q=.5 )
	print "Predicted State",xminus
	print "predicted Variance",Pminus
	x,P= kf.update(x=xminus, P=Pminus, z=measure1, R=.2)
	print "Updated State", x
	print "Updated vairance",P

while 1:
	xminus,Pminus=kf.predict (x=)

"""
"""f= KalmanFilter(dim_x=1, dim_z=1)
f.x=np.array([-0.15])
"""


























