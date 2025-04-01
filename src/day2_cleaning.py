#src/day2_cleaning.py
from data_loader import load_data
from data_cleaner import clean_data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

#Load data
train_data, test_data=load_data()

#Clean data
train_cleaned=clean_data(train_data)
test_cleaned=clean_data(test_data)

#Print Cleaned Data
print("Cleaned Training Data Info:")
print(train_cleaned.info())

print("\nMissing Values After Cleaning:")
print(train_cleaned.isnull().sum())

#Save Cleaned data to CSV

train_cleaned.to_csv(os.path.join("..","data","train_cleaned.csv"), index=False)
test_cleaned.to_csv(os.path.join("..","data","test_cleaned.csv"), index=False)
print("Cleaned data saved to 'data/train_cleaned.csv' and 'data/test_cleaned.csv'")

#Visualize cleaned Age Distribution
sns.histplot(train_cleaned['Age'],bins=20)
plt.title("Age Distribution After Cleaning")
plt.savefig(os.path.join("..","age_distribution.png"))
plt.close()
print("Age distribution plot saved as 'age_distribution.png'")
