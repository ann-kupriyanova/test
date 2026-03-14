import pandas as pd
import random as rd
dict = {'age': [rd.randint(20, 50) for i in range(100)],
        'user_id': [rd.randint(10000, 20000) for i in range(100)]}
df = pd.DataFrame(dict)
#print(df.head(10))
print(df['age'].mean())
df_new = df.where((df['age'] >= 20) & (df['age'] <=30))
print(df_new['age'].mean())
print(df.describe())