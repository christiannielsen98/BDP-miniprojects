import pandas as pd

data = pd.read_csv('raw.csv')
data["date"] = pd.DatetimeIndex(data["date"])
data.to_csv("raw2.csv", index=False)