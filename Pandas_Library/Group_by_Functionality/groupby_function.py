#Using groupby() to group records on basis of categorical variable
#Importing pandas library
import pandas as pd

#Importing "csv" file and storing in data frame
liver = pd.read_csv("./Pandas_Library/Import_of_Data/indian_liver_patient.csv")
print(liver.keys())
#Count the number of records on the basis of Gender.
print("Number of records based on different gender are:\n", liver['Gender'].groupby(liver['Gender']).count())

#Grouping on basis of "Gender" and using sum() function for "Total_Bilirubin"
print("Grouping of observations on basis of Gender and calculating sum of Total_Bilirubin:\n", 
      liver['Total_Bilirubin'].groupby([liver['Gender']]).sum())

#Grouping on basis of "Dataset" and using min() function for "Direct_Bilirubin".
print("Grouping on basis of Dataset and calculting minimum of Direct_Bilirubin:\n", liver["Direct_Bilirubin"].groupby([liver['Dataset']]).min())

#Grouping on basis of "Dataset" and using max() function for "Albumin"
print("Grouping on basis of Dataset and calculating maximum of Albumin:\n", liver['Albumin'].groupby([liver['Dataset']]).max())

#Grouping on basis of "Dataset" and using mean() function for "Total_Protiens" 
print("Grouping on basis of Dataset and calculating mean of Total_Protiens:\n", liver['Total_Protiens'].groupby([liver['Dataset']]).mean())

#Grouping on basis of "Dataset", using median() function for "Albumin_and_Globulin_Ratio"
print("Grouping on basis of Dataset and calculating median of Albumin_and_Globulin_Ration:\n", 
      liver['Albumin_and_Globulin_Ratio'].groupby([liver['Dataset']]).median())