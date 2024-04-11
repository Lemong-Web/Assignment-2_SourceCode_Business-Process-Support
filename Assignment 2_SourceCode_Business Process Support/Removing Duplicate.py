import pandas as pd

df = pd.read_csv('ABC_Manufacturing.csv')

df.dropna(inplace = True)

print(df.to_string())





