#Progrm to create array from numpy library
import numpy

#creating an array of integers
myarray1 = numpy.array([11,22,33,44,55,66], int)
print("The array of integers is:\n", myarray1)

#creating an aaray of characters
myarray2 = numpy.array(['a','b','c','d','e','f'])
print("The array of characters is:\n", myarray2)

#creating an array of strings
myarray3 = numpy.array(['JAVA', 'PYTHON', 'C++', 'C'], dtype=str)
print("The array of strings is:\n", myarray3)

#creating an float array
myarray4 = numpy.array([6.3,24.5,16.7,28.9,85.8], float)
print("The array of decimal numbers is:\n", myarray4)

#using view() function to create a new array from an existing array
myarray5 = myarray3.view()
print("Using view function to create a new array:\n", myarray5)

#using copy() function to create a new array from an existing array
myarray6 = myarray4.copy()
print("Using copy function to create a new array:\n", myarray6)