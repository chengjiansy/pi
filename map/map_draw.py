import numpy as np
import pylab as pl
data = np.loadtxt('map_training.txt')
for i in range(len(data)):
    pl.plot(data[i,3], data[i,2], 'ro')
    pl.text(data[i,3], data[i,2],data[i,5])
    
pl.xlabel('x')
pl.ylabel('y')
pl.xlim(0.0, 10.)
print data
pl.show()
