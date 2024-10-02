#Program for using functions related to general information of data
#Importing pandas library
import pandas as pd

#Importing "csv" file and storing in data frame
liver = pd.read_csv("./Pandas_Library/Import_of_Data/indian_liver_patient.csv")

#Displaying the information of the dataset using info() function
print("Information of the dataset is:\n", liver.info())

#Displaying the complete dataset using describe
print("Details of the dataset is:\n", liver.describe)

#Displaying descriptive statistical values of column using describe()
print("Description of the dataset is:\n", liver.describe())

#Use of head() function to display starting records
#Displaying first/last records from dataset - head(), tail() function
print("First five records of dataset are:\n", liver.head())

#Displaying the first two records
print("First two records of dataset are:\n", liver.head(2))

#Displaying the first three records of "Age" and "Total_Protiens"
print("First three records of Age and Total_Protiens:\n", liver[['Age','Total_Protiens']].head(3))

#Use of tail() function to display ending records
#Displaying the last three records
print("Last three records of dataset is:\n", liver.tail(3))

#Displaying the last two recores of "Age" and "Total_Bilirubin"
print("Last 2 records of age and Total_Bilirubin:\n", liver[['Age','Total_Bilirubin']].tail(2))

#Determining all the values of Direct_Bilirubin column only
print("Values for Direct_Bilirubin column are:\n", liver['Direct_Bilirubin'].values)

#Program to use different functions for specified column
#Determine number of records based on gender
print("Number of records for gender:\n", liver['Gender'].value_counts())

#Determine number of records based on gender in percentage form
print("Number of records based on gender in percentage form:\n", liver['Gender'].value_counts()/len(liver['Gender']))

#Displaying the descriptive statistics of Total_Protiens
print("Describing the details of TB column:\n", liver['Total_Protiens'].describe())

#Program for converting data frame to a list
agelist = liver['Age'].tolist()
print("The list corresponding to age is: \n", agelist)