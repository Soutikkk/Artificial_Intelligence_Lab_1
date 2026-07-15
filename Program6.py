import numpy as np 
import matplotlib.pyplot as plt 
data=np.random.poisson(5,1000) 
plt.hist(data,bins=30) 
plt.title("Poisson Distribution") 
plt.show() 