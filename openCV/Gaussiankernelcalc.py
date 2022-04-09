#2d gaussian like array
import numpy as np

x,y=np.meshgrid(np.linspace(-1,1,5),np.linspace(-1,1,5))

d=np.sqrt(x**2 + y**2)
s,mu=1.0,0.0
g=np.exp(-((d-mu)**2/2*s**2))
print(g)