#Using iloc indexers for filtering data based on multiple condition
#Importing pandas library
import pandas as pd

#Importing "csv" file and storing in data frame
liver = pd.read_csv("./Pandas_Library/Import_of_Data/indian_liver_patient.csv")

#Displaying single column in single row
print("Third Column of sixth record:", liver.iloc[5,2])

#Displaying all the columns of specific row
print("Sixth Record:\n", liver.iloc[5])

#Displaying multiple specified columns and rows
print("Selected row and selected column:\n", liver.iloc[[5,9],[1,4]])

#Displaying specific column of range of rows.
print("Range of records for sixth column:\n", liver.iloc[7:9, [5]])

#Displaying specific column of range of rows and range of column
print("Range of records for sixth column:\n", liver.iloc[7:9, 5:8])