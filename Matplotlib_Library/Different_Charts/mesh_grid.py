#Program for creating a meshgrid
import matplotlib.pyplot as plt
import numpy

#Creating large dataset
val1 = numpy.linspace(-9, 9, 600)
val2 = numpy.linspace(-5, 5, 500)

#Creating a meshgrid chart
A,B = numpy.meshgrid(val1, val2)
plt.figure(1, figsize=(10,5))
plt.subplot(131)
plt.imshow(A+B)
plt.subplot(132)
plt.imshow(A-B)
plt.subplot(133)
plt.imshow(A*B)

plt.show()