import pandas as pd

df = pd.read_csv(data.csv)

df.head()

df.describe()

#Let see what the min value is for everyone
df["value"].min()
