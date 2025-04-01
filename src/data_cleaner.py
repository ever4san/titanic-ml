import pandas as pd

def clean_data(df):
	##Clean the Titanic Datasets
	# Copy to avoid modifying the original
	
	df_cleaned= df.copy()
	
	#Drop irrelevent columns
	df_cleaned=df_cleaned.drop(columns=['Cabin','Ticket','PassengerId'])
	
	#Fill Missing Age with mean
	df_cleaned['Age'] = df_cleaned['Age'].fillna(df_cleaned['Age'].mean())
	
	#Fill missing Embarked with mode
	df_cleaned['Embarked'] = df_cleaned['Embarked'].fillna(df_cleaned['Embarked'].mode()[0])
	
	#Encode Sex (male=0, female=1)
	df_cleaned['Sex'] = df_cleaned['Sex'].replace({'male': 0, 'female': 1}).infer_objects(copy=False)
	
	return df_cleaned
	
	