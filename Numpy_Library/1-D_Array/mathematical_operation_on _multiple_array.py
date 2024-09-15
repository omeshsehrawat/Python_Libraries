#Program to use mathematical operators on multiple arrays
import numpy as np

#Creating three integer arrays
myarray15 = np.array([11,22,33], int)
myarray16 = np.array([40,50,60], int)
myarray17 = np.array([7,8,9], int)

#Performing addition and subtraction on all elements of an array
myarray18 = myarray17 + myarray16 - myarray15
print("Addition and Subtraction on multiple arrays:\n", myarray18)

#Performing multiplication and division on all elements of an array
myarray19 = (myarray15*myarray16)/myarray17
print("Multiplication and division on multiple arrays:\n", myarray19)

#Using modulus operator (%) on all elements of the array
myarray20 = myarray16 % myarray17
print("Using modulus operator on two arrays:\n", myarray20)

#Using integer division (//) on all elements of the array
myarray21 = myarray16 // myarray17
print("Using integer division on two arrays:\n", myarray21)