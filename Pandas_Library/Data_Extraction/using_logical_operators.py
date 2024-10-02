#Using Logical operators for filtering data based on multiple condition
import pandas as pd
liver = pd.read_csv("./Pandas_Library/Import_of_Data/indian_liver_patient.csv")

#Creating a new subset using "and" for multiple conditions
filter1 = liver[(liver['Age']>=35) & (liver['Direct_Bilirubin']<=6)]
print("Shape of new dataset using and is:", filter1.shape)

#Applying sum and product functions on filtered data
#Determining sum of "TB" for a subset
print("Sum of TB from filtered set:", filter1["Total_Bilirubin"].sum())

#Determining product of "Direct_Bilirubin" for a subset
print("Product of DB from filtered set:", filter1["Direct_Bilirubin"].product())

#Creating a new subset using "or" operator for multiple conditions
filter2 = liver[(liver['Gender']=="Female") | (liver['Age']>=35) | (liver['Dataset']<=6)]
print("Shape of new dataset using or is:", filter2.shape)

#Appling mean and median functions on filtered data
#Determining mean of "Albumin" for a subset
print("Mean of Albumin from the filtered set:", filter2["Albumin"].mean())

#Determining median of "Total_Protiens" for subset
print("Median of Total_Protiens from the filtered set:", filter2["Total_Protiens"].median())

#Using both "and" and "or" together for multiple conditions
filter3 = liver[(liver["Dataset"]==1) & (liver.Age>=50) | (liver['Total_Protiens']>=2) | (liver.Albumin)>2]
print("Shape of new dataset using and & or is:", filter3.shape)

#Applying maximum and minimum functions on filtered data
#Determining maximum of "Alkaline_Phosphotase" for a subset
print("Maximum of Alkaline_Phosphotase from filtered set:", filter3['Alkaline_Phosphotase'].max())

#Detemining minimum of "Albumin_and_Globulin_Ratio" for a subset
print("Minimum of Albumin_and_Globulin_Ratio from the filtered set:", filter3['Albumin_and_Globulin_Ratio'].min())


