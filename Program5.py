import numpy as np 
import matplotlib.pyplot as plt 
data=np.random.binomial(10,0.5,1000) 
plt.hist(data,bins=30) 
plt.title("Binomial Distribution") 
plt.show() 