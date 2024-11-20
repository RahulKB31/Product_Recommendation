# eda.py

import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    # Basic Summary
    print("Data Info:\n", df.info())
    print("\nData Description:\n", df.describe())

    # Visualizations
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Product Category', data=df)
    plt.title('Product Category Distribution')
    plt.show()

    plt.figure(figsize=(10, 6))
    df['Purchase Date'].value_counts().plot(kind='bar')
    plt.title('Purchase Frequency Over Time')
    plt.show()