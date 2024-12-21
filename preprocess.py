import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def load_data(filepath):
    """Load the dataset."""
    return pd.read_csv(filepath)

def preprocess_data(df, numerical_features, categorical_features):
    """Preprocess the data by scaling and encoding."""
    # Handle missing values
    df.fillna(method='ffill', inplace=True)
    
    # Scale numerical features
    scaler = StandardScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    
    # Encode categorical features
    encoder = OneHotEncoder(sparse=False)
    encoded = encoder.fit_transform(df[categorical_features])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out())
    
    # Combine data
    return pd.concat([df.drop(columns=categorical_features), encoded_df], axis=1)
