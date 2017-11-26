import numpy as np 
from numpy import *
import matplotlib.pyplot as plt 
data_set = [[-0.017,14.053],[-1.39,4.66]]
data_mat = mat(data_set).T
print data_mat[0]
plt.scatter(data_mat[0].tolist(),data_mat[1].tolist(),c = "r",marker = 'o')
X = np.linspace(-2,2,100)
Y = 2.8 * X + 9
plt.plot(X,Y)
plt.show()