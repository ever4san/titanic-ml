import pandas as pd

def engineer_features(df):
	"""Add new features to the Titanic dataset"""
	df_fe=df.copy()
	df_fe['FamilySize']=df_fe['SibSp']+df_fe['Parch']+1
	df_fe['Title']= df_fe['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
	df_fe['Title']= df_fe['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
	df_fe['Title']= df_fe['Title'].replace('Mlle','Miss')
	df_fe['Title']= df_fe['Title'].replace('Ms','Miss')
	df_fe['Title']= df_fe['Title'].replace('Mme','Mrs')
	embarked_dummies= pd.get_dummies(df_fe['Embarked'], prefix='Embarked')
	df_fe= pd.concat([df_fe,embarked_dummies], axis=1)
	df_fe= df_fe.drop(columns=['Embarked'])
	return df_fe