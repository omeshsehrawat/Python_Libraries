#Using loc indexers for filtering data based on multiple condition
#Importing pandas library
import pandas as pd

#Importing "csv" file and storing in data frame
liver = pd.read_csv("./Pandas_Library/Import_of_Data/indian_liver_patient.csv")

#Retrieving one specific row by loc method
print("Display specific single record:\n", liver.loc[3])

#Retrieving range of rows by loc method
print("Displaying range of records:\n", liver.loc[1:5, ])

#Retrieving different multiple rows by loc method
print("Displaying selected rows for range of column:\n", liver.loc[[14,25,36]])

#Retrieving selected rows with range of columns between 'Total_Bilirubin' and 'Total_Protiens'
print("Displaying selected rows for range of columns:\n", liver.loc[[5,6], 'Total_Bilirubin':'Total_Protiens'])

#Retrieving rows with specific index and with specific columns
print("Displaying range of rows for specific columns:\n", liver.loc[7:9,['Age','Gender','Total_Bilirubin']])

#Using different relational operators for filtering data
#Using == condition for selected columns
print("Displaying rows for Direct_Bilirubin==2 of selected coumns:\n", liver.loc[liver['Direct_Bilirubin']==2, 'Age':'Total_Bilirubin'])

#Using < condition for selected columns
print("Displaying rows for Total_Bilirubin<0.1 of selected columns:\n", liver.loc[liver['Total_Bilirubin']<0.1, 'Gender':'Direct_Bilirubin'])

#Using > condition for selected columns
print("Displaying rows for age>80 of range of columns:\n", liver.loc[liver['Age']>80, 'Age':'Direct_Bilirubin'])

#Using > and < conditions together (using &) for selected columns
print("Displaying rows with Aspartate_Aminotransferase column between 400 and 420:\n",liver.loc[(liver['Aspartate_Aminotransferase']>400) & (liver['Aspartate_Aminotransferase']<=420), ['Total_Bilirubin', 'Alkaline_Phosphotase']])

#Functions with loc index
#Using startwith to select rows for gender starts with 'Fe', Albumin>=5
print("Using startswith function:\n", liver.loc[liver['Gender'].str.startswith("Fe") & (liver['Albumin'] >= 5)])

#Using isin to select rows with Albumin=specified values and Age>=60
print("Using isin function:\n", liver.loc[liver['Albumin'].isin([4.4,4.2,4.3]) & (liver['Age'] >= 60)])
