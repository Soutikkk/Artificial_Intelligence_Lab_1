import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Age': np.random.randint(18, 60, 20),
    'Score': np.random.normal(70, 10, 20)
})

df.plot(x='Age', y='Score', kind='scatter')

plt.title("Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.show()