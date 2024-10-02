#Program to use all the data processing techniques in one dataset
import pandas as pd
loandata = pd.read_csv("./Pandas_Library/Missing_Values/Loan_Prediction.csv")

#Displaying the dimension of the original dataset
print("Dimension of the dataset is:", loandata.shape)

#Information related to number of missing observations for each column
print("Number of missing values in column:\n", loandata.isnull().sum())

