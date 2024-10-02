#Program to use mathematical and statistical functions as filtered data
#Importing pandas library
import pandas as pd

#Importing "csv" file and storing in data frame
liver = pd.read_csv("./Pandas_Library/Import_of_Data/indian_liver_patient.csv")

#Determining median of 'Age' column using median() function
print("Median of age is:", liver['Age'].median())

#Determining mean of 'Age' column using mean() function
print("Mean of age is:", liver['Age'].mean())

#Determining max of 'Age' column using max() function
print("Max of age is:", liver['Age'].max())

#Determining min of 'Age' column using min() function
print("Min of age is:", liver['Age'].min())

#Determining sum of 'Age' column using sum() function
print("Sum of age is:", liver['Age'].sum())

#Determining Product of 'Age' column using product() function
print("Product of age is:", liver['Age'].product())

#Determining 3 smallest values of 'Age' using nsmallest() function
print("Three smallest values of Age:\n", liver['Age'].nsmallest().head(3))

#Determining 4 largest values of 'Age' using nlargest() function
print("Four largest values of Age:\n", liver['Age'].nlargest().head(4))

