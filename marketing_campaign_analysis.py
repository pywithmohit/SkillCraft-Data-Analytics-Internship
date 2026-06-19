import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("marketing_campaign.csv")

# Basic Information
print(df.info())
print(df.describe())

# Missing Values
print(df.isnull().sum())

# Customer Age
df['Age'] = 2025 - df['Year_Birth']

# Income Distribution
plt.figure(figsize=(8,5))
plt.hist(df['Income'].dropna(), bins=20)
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Count")
plt.show()

# Education Analysis
df['Education'].value_counts().plot(kind='bar')
plt.title("Customers by Education")
plt.show()

# Marital Status Analysis
df['Marital_Status'].value_counts().plot(kind='bar')
plt.title("Customers by Marital Status")
plt.show()

# Total Purchases
df['Total_Purchases'] = (
    df['NumWebPurchases'] +
    df['NumCatalogPurchases'] +
    df['NumStorePurchases']
)

print(df[['Income','Total_Purchases']].corr())