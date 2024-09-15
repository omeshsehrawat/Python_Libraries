#Program for using functions on numpy array
import numpy
myarray13 = numpy.array([13,24,22,13,11,28,16,24,18], int)
print("Original array is:\n", myarray13)

#Modifying an element at a specified index
myarray13[3] = 45
print("Modified array is:\n", myarray13)

#Detemine characteristics of the array
#The size returns the size of the array
print("Size of the array is:",myarray13.size)

#The dtype return the datatype of the elements of the array
print("Data type of the array is:", myarray13.dtype)

#Functions returning one single numeric output
#The mean() function returns the mean of all array elements
print("Mean of all array elements is:",numpy.mean(myarray13))

#The median() functon returns the median of all array elements.
print("Median of all array elements is:", numpy.max(myarray13))

#The min() function returns the minimum element of the array
print("Minimum element of the array is:",numpy.min(myarray13))

#The max() function returns the maximum element of the array
print("Maximum element of the array is:",numpy.max(myarray13))

#The sum() function returns the sum of all array elements
print("Minimum element of the array is:",numpy.sum(myarray13))

#The prod() function returns the product of all array elements
print("Product of all array elements is:", numpy.prod(myarray13))

#The cov() function returns the covariance of all array elements
print("Covariance of all array elements is:", numpy.cov(myarray13))

#The var() function returns the variance of all array elements
print("Variance of all array elements is:", numpy.var(myarray13))

#The std() funtion returns standard deviation of all array elements
print("Standard deviation of array elements is:", numpy.std(myarray13))

#Mathematical functions return an array output (all elements)
#The sort() function returns the elements in a sorted order
print("The sorted array is:\n", numpy.sort(myarray13))

#The power() function returns all elements raised to power of a number
print("Power raised to element (3) of array:\n", numpy.power(myarray13,3))

#The sqrt() function returns the square root of all elements
print("Square root of the array elements is:\n", numpy.sqrt(myarray13))

#The abs() function returns the suare root of all elements
print("Square root of the array elements is:\n", numpy.abs(myarray13))

#Trigonometric functions return an array output (all elements)
#The sin() function returns the sine value of all the elements
print("Sine value of the array elements is:\n",numpy.sin(myarray13))

#The cos() function returns the cosine value of all the elements
print("Cosine value of the array elements is:\n",numpy.cos(myarray13))

#The tan() functin returns the tangent value of al the elements 
print("Tangent value of the array elements is:\n", numpy.tan(myarray13))

#Logarithmic/Exponential functions return an array output
#The log() function returns log with exponential base of all elements
print("Log of all elements with \"e\" base is:\n",numpy.log(myarray13))

#The log10() function returns the log with base 10 of all elements
print("Log of all elements with base 10 is:\n", numpy.log10(myarray13))

#The exp() function returns the exponential value of all the elements
print("Exponential of the array elements is:\n", numpy.exp(myarray13))