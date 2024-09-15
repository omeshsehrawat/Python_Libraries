#Program for using basic mathematical operators on multidimensional array
import numpy as np

mymultarray9 = np.array([[10,20,30,40],[50,60,70,80]])
mymultarray10 = np.array([[11,22,33,44,55,66,77,88]])
mymultarray10 = np.reshape(mymultarray10,(2,4))

#Mathematical operations between multidimensional array
print("Addition of 2-D arrays:\n", mymultarray9 + mymultarray10)
print("Subtraction of 2-D arrays:\n", mymultarray9 - mymultarray10)
print("Multiplication of 2-D arrays:\n", mymultarray9 * mymultarray10)
print("Division of 2-D arrays:\n", mymultarray9 / mymultarray10)
print("Modulus of 2-D arrays:\n", mymultarray9 % mymultarray10)
print("Integer division of 2-D arrays:\n", mymultarray9 // mymultarray10)

#Matrix Multiplication
mymultarray11 = np.matrix('10 12; 14 10; 12 10; 14 20')
print("Matrix Multiplication:\n", mymultarray10 * mymultarray11)