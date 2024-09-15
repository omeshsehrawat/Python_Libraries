#Program to show indexing in multidimensional arrays
import numpy as np
mymultarray6 = np.reshape(range(100,400,50), (3,2))
print("The array is:\n", mymultarray6)

#Performing indexing
print("Element of first row and column is:", mymultarray6[0][1])
print("Element of first row and column is:", mymultarray6[1][0])
print("Element of first row and column is:", mymultarray6[1][1])
print("Element of first row and column is:", mymultarray6[2][0])
print("Element of first row and column is:", mymultarray6[2][1])
