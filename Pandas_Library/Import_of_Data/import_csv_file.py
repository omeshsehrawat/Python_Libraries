#Program to determine characteristics of an existing dataset
#Importing pandas library
import pandas as pd
'''import os
print(os.getcwd())'''

#Importing "csv" file and storing in data frame
liver = pd.read_csv("./Pandas_Library/Import_of_Data/indian_liver_patient.csv")

#Determining dimension and size of the dataset
print("Dimension of the dataset is:", liver.shape)
print("Size of the dataset is:", liver.size)

#Determining columns of the dataset
print("Columns in the dataset are:\n", liver.keys())
print("Columns in the dataset are:\n", liver.columns)