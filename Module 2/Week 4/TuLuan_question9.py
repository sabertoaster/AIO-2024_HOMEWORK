import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("advertising.csv")

plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, fmt=".2f", linewidth=.5)
plt.show()
