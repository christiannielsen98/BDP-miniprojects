import pandas as pd

data = pd.read_csv('origin.txt', sep=" ", header=None)
data.columns = ['date', 'time', 'epoch', 'moteid', 'temperature', 'humidity', 'light', 'voltage']
data.dropna(inplace=True)
data.to_csv('./origin.csv', index=False)


# Take a sample from whole dataset
# 