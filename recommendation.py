import numpy as np

def recommend_products(user_id, svd, ratings_matrix, num_recommendations=5):
    user_idx = ratings_matrix.index.get_loc(user_id)
    user_ratings = np.dot(svd.components_, ratings_matrix.iloc[user_idx, :].T)

    # Get the indices of the top products
    recommended_product_indices = np.argsort(user_ratings)[::-1][:num_recommendations]

    recommended_products = ratings_matrix.columns[recommended_product_indices]
    return recommended_products
