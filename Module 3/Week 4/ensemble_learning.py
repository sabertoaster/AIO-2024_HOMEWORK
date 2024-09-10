import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

dataset_path = './Housing.csv'
df = pd.read_csv(dataset_path)

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns.to_list()
print(categorical_cols)

# Encode categorical columns
ordinal_encoder = OrdinalEncoder()
encoded_categorical_cols = ordinal_encoder.fit_transform(
    df[categorical_cols]
)
encoded_categorical_df = pd.DataFrame(
    encoded_categorical_cols,
    columns=categorical_cols
)
numerical_df = df.drop(categorical_cols, axis=1)
encoded_df = pd.concat(
    [numerical_df, encoded_categorical_df], axis=1
)

# Normalize the dataset
normalizer = StandardScaler()
dataset_arr = normalizer.fit_transform(encoded_df)

# Split features and target
X, y = dataset_arr[:, 1:], dataset_arr[:, 0]

# Split into train and validation sets
test_size = 0.3
random_state = 1
is_shuffle = True
X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=test_size,
    random_state=random_state,
    shuffle=is_shuffle
)

# Train Random Forest model
regressor = RandomForestRegressor(
    random_state=random_state
)
regressor.fit(X_train, y_train)

# Train AdaBoost model
regressor = AdaBoostRegressor(
    random_state=random_state
)
regressor.fit(X_train, y_train)

# Train Gradient Boosting model
regressor = GradientBoostingRegressor(
    random_state=random_state
)
regressor.fit(X_train, y_train)

# Make predictions
y_pred = regressor.predict(X_val)

# Evaluate the model
mae = mean_absolute_error(y_val, y_pred)
mse = mean_squared_error(y_val, y_pred)

print('Evaluation results on validation set:')
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
