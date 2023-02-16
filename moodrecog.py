# importing the required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('week1.csv')
sns.countplot(x='emotion', data=df)
plt.show()

