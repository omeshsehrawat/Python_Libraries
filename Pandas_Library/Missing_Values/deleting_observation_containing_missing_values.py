import pandas as pd
loandata = pd.read_csv("./Pandas_Library/Missing_Values/Loan_Prediction.csv")

#creating a copy of the data frame
newloandata = loandata.copy()

#Removing the complete observations containing missing values
newloandata.dropna(inplace=True)

#Displaying the dimension after removing missing observations
print("Dimension after removing observations:", newloandata.shape)



