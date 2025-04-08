from data_loader import load_data
from data_cleaner import clean_data
from feature_engineer import engineer_features
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load and clean data
train_data,test_data=load_data()
train_cleaned=clean_data(train_data)
test_cleaned=clean_data(test_data)

#Engineer Features
train_fe=engineer_features(train_cleaned)
test_fe=engineer_features(test_cleaned)

#Inspect
print("Featured Training Data Info:")
print(train_fe.info())
print("\nFrist 5 rows:")
print(train_fe.head())

#save
train_fe.to_csv(os.path.join("..","data","train_fe.csv"),index=False)
test_fe.to_csv(os.path.join("..","data","test_fe.csv"),index=False)
print("Featured data saved to 'data/train_fe.csv' and 'data/test_fe.csv'")

#Visualize Family Size
sns.countplot(x="FamilySize", hue="Survived", data=train_fe)
plt.title("Survival by Family Size")
plt.savefig(os.path.join("..","plot","survival_by_familysize.png"))
plt.close()
print("Survival by family size plot saved as 'survival_by_familysize.png'")



