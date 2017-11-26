import matplotlib.pyplot as plt
import numpy as np 
print "numpy test"
x = np.arange(-3,3.5,0.5)
y = [e **2 for e in x]
z = [e *2 for e in x]
fit = plt.figure(1)
ax = fit.add_subplot(211)
line1 = ax.plot(x,y,'ro-')
ax = fit.add_subplot(212)
line2 = ax.plot(x,z,"g-")
plt.show()
