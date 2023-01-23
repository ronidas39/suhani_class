import pandas as pd
df=pd.read_csv("input.csv")
df1=df[["name","email"]]
df1.to_csv("subset.csv",index=False)
