#Program for deleting rows and columns from the data frame
#Importing Pandas Library
import pandas as pd

#Creating my first data frame
productdf = pd.DataFrame([[100,200,300,400],[4,2,5,6]],
                         columns=['Pen', 'Shirt', 'Book', 'Mouse'])

#Creating a new data frame
productdf2 = pd.DataFrame([[15,16,17,18],[5,6,7,8]],
                          columns=['Pen','Shirt','Book','Mouse'])

#Adding rows to the data frame by adding other data frame
productdf3 = productdf._append(productdf2)

#Adding column named "Mobile" to th data frame
productdf3["Mobile"] = [3500,3,10,15]

#Adding column named "Laptop" to the data frame
productdf3["Laptop"] = [35000,3,10,15]

#Deleting multiple columns from the data frame using drop() function
productdf3 = productdf3.drop(columns = ["Pen", "Book"])
print("Column deleted data frame:", productdf3)
print("Dimension after deleting two columns is:", productdf3.shape)

#Deleting row from the data frame
productdf3 = productdf3.drop(index=[0])
print("Dimension after deleting row at index 0 is:", productdf3.shape)
print("The modified data frame is:\n", productdf3)
print("Size of modified data frame is:", productdf3.size)

#Creating a new data frame
productdf4 = pd.DataFrame([[100,200,300,400,3500,3500],[4,2,5,6,3,3],[15,16,17,18,10,10],[5,6,7,8,15,15]],
                         columns=['Pen', 'Shirt', 'Book', 'Mouse',"Mobile","Laptop"])
print("New Dataframe without using append function:\n", productdf4)
productdf4 = productdf4.drop(columns = ["Pen", "Book"])
productdf4 = productdf4.drop(index=[0])
print("Modified Dataframe (formed without append function):\n",productdf4)