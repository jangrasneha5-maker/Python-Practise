
import pandas as pd
import numpy as np

df = pd.DataFrame({'Emp': ['A', 'B', 'C'], 'Salary': [5000, np.nan, 7000]})

# 1. Check for nulls
print(df.isnull().sum())

# 2. Fill with mean
mean_sal = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean_sal)