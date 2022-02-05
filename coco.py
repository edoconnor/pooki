import pandas as pd
import csv

pd.set_option('display.max_rows', 600)
pd.set_option('display.max_columns', 60)
pd.set_option('display.width', 60)

df = pd.read_csv("mega.csv") 

# df['f'] = df.groupby('strokes')['strokes'].transform('count')
# df['n'] = len(df['strokes'])

df1 = df[['player','05-30-21']]
df3 = df1.sort_values(by='05-30-21', ascending=False)

df4 = df3.head(20)

print(df4)
# df3.to_csv('coco-pooki.csv', header=None,index=False)