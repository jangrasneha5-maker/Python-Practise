import pandas as pd

data = {
    'Name':['sneha','rishita','simran','umaa'],
    'Age':[23,25,22,24],
    'Salary':[50000,60000,55000,62000]
}

df = pd.DataFrame(data)
# print(df[['Name','Age']])
# print(df.iloc[1])
# print(df[df['Age']>22])
# df['Bonus']=df['Salary']*0.10
# print(df)
# Corrected line:
# df.loc[0, 'Salary'] = 52000
# print(df)