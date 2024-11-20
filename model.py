# model.py

import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def build_model(df):
    # Create a user-product matrix (ratings matrix)
    ratings_matrix = df.pivot_table(index='User Encoded', columns='Product Encoded', values='Rating')

    # Replace NaN values with 0 (implicit feedback for unrated products)
    ratings_matrix = ratings_matrix.fillna(0)

    # Train-test split (80-20)
    X_train, X_test = train_test_split(ratings_matrix, test_size=0.2, random_state=42)

    # Use Truncated SVD for dimensionality reduction and matrix factorization
    svd = TruncatedSVD(n_components=5, random_state=42)
    svd_matrix = svd.fit_transform(X_train)

    return svd, svd_matrix, X_train, X_test


def evaluate_model(svd, X_train, X_test):
    # Reconstruct the rating matrix from the SVD
    reconstructed_matrix = np.dot(svd.components_, X_train.T)

    # Evaluate on test data
    predicted_ratings = reconstructed_matrix.T
    mse = mean_squared_error(X_test, predicted_ratings)
    print(f"Mean Squared Error: {mse}")
    return mse
