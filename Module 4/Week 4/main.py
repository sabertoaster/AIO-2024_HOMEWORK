import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def load_data(file_path):
    """
    Load the sales prediction dataset
    """
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """
    Preprocess the data:
    1. One-hot encode the Influencer column
    2. Handle null values
    3. Split features and target
    """
    # One-hot encoding for Influencer column
    df = pd.get_dummies(df)
    df = df.fillna(df.mean())
    
    # Get features and target
    X = df[['TV', 'Radio', 'Social Media', 'Influencer_Macro', 
            'Influencer_Mega', 'Influencer_Micro', 'Influencer_Nano']]
    y = df[['Sales']]
    
    return X, y

def scale_features(X_train, X_test):
    """
    Scale features using StandardScaler
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled

def create_polynomial_features(X_train_scaled, X_test_scaled, degree=2):
    """
    Create polynomial features
    """
    poly_features = PolynomialFeatures(degree=degree)
    X_train_poly = poly_features.fit_transform(X_train_scaled)
    X_test_poly = poly_features.transform(X_test_scaled)
    return X_train_poly, X_test_poly

def train_and_evaluate(X_train_poly, X_test_poly, y_train, y_test):
    """
    Train the model and evaluate its performance
    """
    # Initialize and train the model
    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, y_train)
    
    # Make predictions
    predictions = poly_model.predict(X_test_poly)
    
    # Calculate R2 score
    r2 = r2_score(y_test, predictions)
    
    return poly_model, predictions, r2

def main():
    df = load_data('SalesPrediction.csv')
    
    X, y = preprocess_data(df)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=0
    )
    
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)
    
    X_train_poly, X_test_poly = create_polynomial_features(X_train_scaled, X_test_scaled)
    
    print("Training and evaluating model...")
    model, predictions, r2_score_val = train_and_evaluate(
        X_train_poly, X_test_poly, y_train, y_test
    )
    
    print(f"\nModel Performance:")
    print(f"R² Score: {r2_score_val:.4f}")

if __name__ == "__main__":
    main()