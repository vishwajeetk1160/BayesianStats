
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
xi=z
xi[0], Pi[0]=-0.15, 4.

xp[],Pp[]=filterpy.kalman.predict(xi[],Pi[])    #have doubt in f variable

print "predicted", xp, "vairance", Pp


xp,Pp=filterpy.kalman.predict(xp,Pp)