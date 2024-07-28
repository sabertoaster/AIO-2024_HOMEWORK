import pandas as pd

data = pd.read_csv("advertising.csv")

def correlation(x, y):
    return x.corr(y)

features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")
