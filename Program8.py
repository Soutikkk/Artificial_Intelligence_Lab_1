import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
d=np.random.choice(['A','B','C'],500) 
pd.Series(d).value_counts().plot(kind='bar') 
plt.show() 