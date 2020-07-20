# importing the  necessary libraries
import pandas as pd
import numpy as np
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

# loading the dataset
ds = pd.read_csv('gapminder-FiveYearData.csv')

# converting the dataset to dataframe
df1 = DataFrame(ds)

# pivoting table to requested format
df2 = df1.pivot_table('lifeExp', 'year', 'continent', aggfunc='mean', margins=True, margins_name='Total')
print(df2)

# ploting the heatmap using seaborn
sns.heatmap(df2, annot=True)
plt.title('HeatMap')
plt.savefig('Heatmap.png')

# visualizing the image
plt.show()











