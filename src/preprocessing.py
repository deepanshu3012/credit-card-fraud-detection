import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Preprocessing function
def preprocess(df):
    # Handle missing values (optional)
    df.fillna(df.median(), inplace=True)  # For numerical columns
    for col in df.select_dtypes(include=['object']).columns:  # For categorical columns
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Initialize LabelEncoder for encoding categorical columns
    label_encoder = LabelEncoder()
    # Encode 'merchant' and 'city' columns
    df['merchant'] = label_encoder.fit_transform(df['merchant'])
    df['city'] = label_encoder.fit_transform(df['city'])

    # Encode other object columns (if any)
    for col in df.select_dtypes(include=['object']).columns:
        if col not in ['merchant', 'city']:  # Skip already encoded columns
            df[col] = label_encoder.fit_transform(df[col])

    # Separate features and target
    X = df.drop(columns=['is_fraud'])  # Assuming 'is_fraud' is the target column
    y = df['is_fraud']
    
    return X, y
