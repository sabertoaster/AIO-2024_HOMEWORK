import pandas as pd
import numpy as np
df = pd.read_csv('advertising.csv')
data = df.to_numpy()
print(len(df[df["Sales"] >= 20]))