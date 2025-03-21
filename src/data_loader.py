import pandas as pd
import os

def load_data():
	base_path=os.path.join(os.path.dirname(__file__),"..","data")
	print(base_path)
	train_data=pd.read_csv(os.path.join(base_path,"train.csv"))
	test_data=pd.read_csv(os.path.join(base_path,"test.csv"))
	return train_data, test_data

