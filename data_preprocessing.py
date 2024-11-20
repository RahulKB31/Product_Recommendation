import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_data():
    # Sample data
    data = {
        'User ID': [1, 2, 1, 3, 2, 4, 5, 3, 4, 5],
        'Product ID': [101, 101, 102, 103, 104, 102, 103, 104, 105, 106],
        'Product Category': ['A', 'A', 'B', 'C', 'B', 'B', 'C', 'C', 'A', 'A'],
        'Purchase Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'Rating': [5, 4, 4, 3, 5, 4, 3, 2, 4, 5]
    }
    df = pd.DataFrame(data)
    return df


def preprocess_data(df):
    # Encoding User ID and Product ID
    user_encoder = LabelEncoder()
    product_encoder = LabelEncoder()

    df['User Encoded'] = user_encoder.fit_transform(df['User ID'])
    df['Product Encoded'] = product_encoder.fit_transform(df['Product ID'])

    return df, user_encoder, product_encoder
