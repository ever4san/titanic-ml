from data_loader import load_data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load Data
train_data, test_data = load_data()

# Inspect Data
print("First 5 rows of training data:")
print(train_data.head())
print("\nData info:")
print(train_data.info())
print("\nSummary Statistics:")
print(train_data.describe())
print("\nMissing Valuse:")
print(train_data.isnull().sum())

#  Visualize survival counts
sns.countplot(x="Survived", data=train_data)
plt.title("Survival Count")
plt.savefig("../survival_count.png")
plt.close()
print("Survival count plot saved as 'survival_count.png'")

# Daily Challenge: Survival rate and plot by gender
survival_rate = train_data["Survived"].mean() * 100
print(f"\nSurvival Rate: {survival_rate:.2f}%")
sns.countplot(x="Survived", hue="Sex", data=train_data)
plt.title("Survival by Gender")
plt.savefig("../survival_by_gender.png")
plt.close()
print("Survival by gender plot saved as 'survival_by_gender.png'")