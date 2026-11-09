import pandas as pd

# lst=[1,2,3,4,5,6]
# print(lst)

# Series = pd.Series(lst)
# print(Series)
# print(type(Series))


# DATAFRAME

# df=pd.DataFrame()
# print(df)

# lst=[1,2,3,4,5,6]
# df=pd.DataFrame(lst)
# print(df)

# lst=[1,2,3,4,5],[5,6,7,8,9]
# df=pd.DataFrame(lst)
# print(df)


b={'rollno.':pd.Series([1,2,3,4,5]),
   'maths':pd.Series([34,56,42,34,12]),
   'physics':pd.Series([45,22,45,46,45])}
df=pd.DataFrame(b)
print(df)
print(df.head())#first 5 print krega lekin agar bracket mei kuch lkhoge toh voh print hoga
print(df.tail())#last 5 print krega lekin agar bracket mei kuch lkhoge toh voh print hoga
print(df.info())# gives basic idea of data
print(df.describe())# saara numeric dat btayega like count mean and everything



