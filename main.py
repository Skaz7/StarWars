import pandas as pd

df = pd.read_csv('Star Wars.csv')
print(df.head(5))

print(df.columns)

for i in df.columns:
    if 'Unnamed' in i:
        print(i)