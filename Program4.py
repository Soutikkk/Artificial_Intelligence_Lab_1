import numpy as np 
import matplotlib.pyplot as plt 
data=np.random.randint(1,101,500) 
plt.hist(data,bins=30) 
plt.title("Random Integers") 
plt.show()