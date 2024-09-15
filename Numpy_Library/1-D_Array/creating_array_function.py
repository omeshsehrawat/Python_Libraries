#Program for creating arrays using different functions
import numpy

#creating an integer array usinbg arange() function
myarray7 = numpy.arange(14)
print("The array of integers using arange() function is:\n", myarray7)

#creating a float array using arange() function
myarray8 = numpy.arange(14, 19, dtype = numpy.float16)
print("The array of decimal numbers using arange() function is:\n", myarray8)

#creating an integer array using linspace() for equal spacing
myarray9 = numpy.linspace(12, 24, 5)
print("The array of integers using linspace() function is:\n", myarray9)

#creating float array using linspace() for equal spacing
myarray10 = numpy.linspace(1., 4., 5)
print("The array of decimal numbers using linspace() function is:\n", myarray10)

#creating arrayusing zeros() function
myarray11 = numpy.zeros((4))
print("An array using zeros:\n", myarray11)

#creating array using ones() function
myarray12 = numpy.ones((5))
print("An array using ones:\n", myarray12)