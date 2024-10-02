#Program for creating series using series() function of Pandas Library
#Importing Pandas library
import pandas as pd

#Creating a list of prices
pricelist = [100, 200, 300, 400]

#Creating a series
productseries = pd.Series(pricelist, index=['Pen', 'Shirt', 'Book', 'Mouse'])

#Displaying the series
print(productseries)