import numpy as np 
import matplotlib.pyplot as plt 
data=np.random.exponential(2,1000) 
plt.hist(data,bins=30) 
plt.title("Exponential Distribution") 
plt.show() 