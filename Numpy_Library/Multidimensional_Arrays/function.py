#Program for functions on multidimensional array
import numpy as np
mymultarray8 = np.array([[10,60,40],[40,50,30],[50,60,40],[40,50,20]])

#Displaying the matrix
print("Transposed matrix is:\n", mymultarray8)

#The transpose() function returns the transpose of a matrix
print("Transposed matrix is:\n", mymultarray8.transpose())

#The ndim determines dimension of the array
print("Dimension of the array is:", mymultarray8.ndim)

#The shpae determines shape of the array
print("Shape of the array is:", mymultarray8.shape)

#The flatten() flattens matrix and convert into one-dimensional
print("Flattened matrix is:\n", mymultarray8.flatten())

#The sort() function with axis=1(default)sorts the matrix on row basis
print("Sorted matrix on row basis (default):\n", np.sort(mymultarray8))

#The sort() function with axis=0 sorts the matrix on column basis
print("Sorted matrix on row basis (default):\n", np.sort(mymultarray8, axis=0))

#The diagonal() function helps to determine the diagonal elements
print("Diagonal elements are:\n", np.diagonal(mymultarray8))