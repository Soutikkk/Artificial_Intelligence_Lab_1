import pandas as pd 
import numpy as np 
df=pd.DataFrame({ 
'Age':np.random.randint(18,60,100), 
'Score':np.random.normal(70,10,100)}) 
print(df.head()) 
print(df.describe())