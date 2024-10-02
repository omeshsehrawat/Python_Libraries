#Program for adding rows and columns to the data frame
#Importing Pandas Library
import pandas as pd

#Creating my first data frame
productdf = pd.DataFrame([[100,200,300,400],[4,2,5,6]],
                         columns=['Pen', 'Shirt', 'Book', 'Mouse'])

#Creating a new data frame
productdf2 = pd.DataFrame([[15,16,17,18],[5,6,7,8]],
                          columns=['Pen','Shirt','Book','Mouse'])
print("Second data frame is:\n", productdf2)
print("Dimension of the new data frame is:", productdf2.shape)

#Adding rows to the data frame by adding other data frame
productdf3 = productdf._append(productdf2)
print("Third data frame is:\n", productdf3)
print("Dimension of the new data frame is:", productdf3.shape)

#Adding column named "Mobile" to th data frame
productdf3["Mobile"] = [3500,3,10,15]

#Adding column named "Laptop" to the data frame
productdf3["Laptop"] = [35000,3,10,15]

#Displaying the new data frame
print("New data frame after adding two columns is:\n", productdf3)

#Display the Shape of the new data frame
print("Dimension of the new data frame is:", productdf3.shape)

#Display the size of the data frame using size
print("Size of the new data frame is:", productdf3.size)