import pandas as pd

df = pd.read_csv(data.csv)

df.head()

df.describe()

#Let see what the max value is for everyone
df["value"].max()
