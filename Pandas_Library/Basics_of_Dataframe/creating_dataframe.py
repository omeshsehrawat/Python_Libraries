#Program for creating and determining characteristics of a data frame
#Importing Pandas Library
import pandas as pd

#Creating my first data frame
productdf = pd.DataFrame([[100,200,300,400],[4,2,5,6]],
                         columns=['Pen', 'Shirt', 'Book', 'Mouse'])

#Displaying the data frame
print("Data frame of product is:\n", productdf)

#Displaying the dimensions of the data frame using shape
print("Dimension of the product data frame is:", productdf.shape)

#Displaying the size of the data frame using size
print("Size of the product data frame is:", productdf.size)

#Displaying the name of the columns using keys() function
print("Name of the columns are:\n", productdf.keys())