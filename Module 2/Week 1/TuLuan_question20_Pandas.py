import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
data = df.to_numpy()
A = np.mean(df["Sales"])
df["scores"] = df[["Sales"]]
mask_0 = df["Sales"] > A
mask_1 = df["Sales"] == A
mask_2 = df["Sales"] < A
df.loc[mask_0, "scores"] = "Good"
df.loc[mask_1, "scores"] = "Average"
df.loc[mask_2, "scores"] = "Bad"
print(df.loc[7:9, "scores"])
