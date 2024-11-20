from data_preprocessing import load_data, preprocess_data
from eda import perform_eda
from model import build_model, evaluate_model
from recommendation import recommend_products


def main():
    # Load and preprocess data
    df = load_data()
    df, user_encoder, product_encoder = preprocess_data(df)

    # Perform EDA
    perform_eda(df)

    # Build and train the model
    svd, svd_matrix, X_train, X_test = build_model(df)

    # Evaluate model
    mse = evaluate_model(svd, X_train, X_test)

    # Generate recommendations for a specific user
    user_id = 1  # Example: User ID = 1
    recommended_products = recommend_products(user_id, svd, X_train, num_recommendations=5)

    # Decode the recommended products back to original Product IDs
    recommended_product_ids = product_encoder.inverse_transform(recommended_products)
    print(f"Recommended Products for User {user_id}: {recommended_product_ids}")


if __name__ == "__main__":
    main()