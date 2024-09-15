#Program to show slicing in multidimensional array
import numpy as np
mymultarray7 = np.reshape(range(100,500,20), (4,5))
print("The multidimensional array is:\n", mymultarray7[ : , : ])

#Slicing by specifying only the row indexes
print("First two rows are:\n", mymultarray7[0:2, ])
print("Third row is:\n", mymultarray7[2, ])

#Slicing by specifying both the row and column indexes
print("Elements in first and second row and column are:\n", mymultarray7[0:2, 0:2])
print("Elements in second row and second to fourth column are:\n", mymultarray7[1 , 1:4])