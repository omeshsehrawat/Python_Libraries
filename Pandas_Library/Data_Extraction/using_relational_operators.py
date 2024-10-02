#Program for using realtional operators for filtering the data
#Importing pandas library
import pandas as pd

#Importing "csv" file and storing in data frame
liver = pd.read_csv("./Pandas_Library/Import_of_Data/indian_liver_patient.csv")

#Displaying columns
print("Columns in the dataset are:\n", liver.keys())

#Displaying the first 2 records where gender is male
male_data = liver[liver["Gender"]=="Male"]
print("First 2 records for male patients are:\n", male_data.head(2))

#Displaying the first 3 records where Age is greater than equal to 50
age_more50 = liver["Age"]>=50
print("First 3 records for age>=50 are:\n", liver[age_more50].head(3))

#Displaying the last 2 records where Albumin is less than or equal to 1
albumin_less1 = liver["Albumin"]<=1
print("Last 2 records having Albumin<=1 are:\n", liver[albumin_less1].tail(2))



