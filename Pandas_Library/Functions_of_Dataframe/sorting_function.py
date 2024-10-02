#Program for sorting in ascending, descending order on basis of "Total_Protiens"
#Importing pandas library
import pandas as pd

#Importing "csv" file and storing in data frame
liver = pd.read_csv("./Pandas_Library/Import_of_Data/indian_liver_patient.csv")

#Sorting in descending order
print("Top two records based on descending order of Total_Protiens are:\n", liver.sort_values(by='Total_Protiens', ascending = False).head(2))
print("Bottom two records based on descending order of Total_Protiens are:\n", liver.sort_values(by='Total_Protiens', ascending = False).tail(2))

#Sorting in ascending order
print("Top two records based on ascending order of Total_Protiens are:\n", liver.sort_values(by='Total_Protiens', ascending = True).head(2))
print("Bottom two records based on ascending order of Total_Protiens are:\n", liver.sort_values(by='Total_Protiens', ascending = True).tail(2))
