import pandas as pd
loandata = pd.read_csv("./Pandas_Library/Missing_Values/Loan_Prediction.csv")

#Determining total loan amount from the data
print("Sum of loan amount before missing data imputation:", loandata['LoanAmount'].sum())
print("Number of missing values:", loandata['LoanAmount'].isnull().sum())

#Replacing missing values of continuous variable "LoanAmount" with 0.
loan1 = loandata.copy()
loan1.fillna({'LoanAmount':0}, inplace=True)
print("Sum of loan amount after replacing missing values with 0:", loan1['LoanAmount'].sum())
print("Number of missing values:", loan1['LoanAmount'].isnull().sum())

#Replacing missing values of continuous variable "LoanAmount" with median
loan2 = loandata.copy()
loan2.fillna({'LoanAmount':loan2['LoanAmount'].median()}, inplace=True)
print("Sum of loan amount after replacing missing values with median:", loan2['LoanAmount'].sum())
print("Number of missing values:", loan2['LoanAmount'].isnull().sum())

#Replacing missing values of continuous variable "LoanAmount" with mean
loan3 = loandata.copy()
loan3.fillna({'LoanAmount':loan3['LoanAmount'].mean()}, inplace=True)
print("Sum of loan amount after replacing missing values with mean:", loan3['LoanAmount'].sum())
print("Number of missing values:", loan3['LoanAmount'].isnull().sum())

#Replacing the categorical variable "Gender" with mode of Gender
loan4 = loandata.copy()
loan4.fillna({'Gender':loan4['Gender'].mode().iloc[0]}, inplace=True)
print("Missing values in Gender:", loan4['Gender'].isnull().sum())

#Replacing the categorical variable "Marrid" with "Yes"
loan4.fillna({'Married':'Yes'}, inplace=True)
print("Missing values in Married:", loan4['Married'].isnull().sum())


