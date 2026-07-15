import numpy as np 
import matplotlib.pyplot as plt 
data=np.random.uniform(0,1,1000) 
plt.hist(data,bins=30) 
plt.title("Uniform Distribution") 
plt.show() 