#Program to show creation of multidimensional array
import numpy as np

#Creating a two-dimensional array using array() function
mymultarray1 = np.array([[100,200,300,400],[600,700,800,900]])
print("Multidimensional array using array function is:\n", mymultarray1)

#Creating a two-dimensional array using matrix() function
mymultarray2 = np.matrix('11 22; 33 44; 55 66')
print("Multidimensional array using matrix function is:\n", mymultarray2)

#Creating a two-dimensional array using reshape() function
newarray = np.array([10,20,30,40,50,60])
mymultarray3 = np.reshape(newarray,(3,2))
print("Multidimensional array using reshape function is:\n", mymultarray3)

#Creating array using zeros() function
mymultarray4 = np.zeros((4,2))
print("Multidimensional array using zeros function is:\n", mymultarray4)

#Creating array using ones() function
mymultarray5 = np.ones((2,3))
print("Multidimensional array using ones function is:\n", mymultarray5)