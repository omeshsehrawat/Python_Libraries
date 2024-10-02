#Program to draw multiple quiver plots in single image
import matplotlib.pyplot as plt
import numpy as np
a = [10,20,30,40,50,60,70]
b = [60,40,80,100,120,140,50]
plt.figure(1, figsize=(15,15))

#Creating a quiver plot in first cell of image having 3 rows and 2 columns
plt.subplot(3,2,1)
plt.quiver(a, b, color='r')

#Creating a quiver plot in second cell
plt.subplot(3,2,2)
plt.quiver(b, a, color='b')

#Creating a quiver plot in third cell
plt.subplot(3,2,3)
x = 8
y = 6
M,N = np.mgrid[0:x, 0:y]
plt.quiver(M,N)

#Creating a quiver plot in fourth cell
plt.subplot(3,2,4)
plt.quiver(N,M)

#Creating a quiver plot in fifth cell
plt.subplot(3,2,5)
x = 20
y = 15
M,N = np.mgrid[10:x, 10:y]
plt.quiver(N, M)

#Creating a quiver plot in sixth cell
plt.subplot(3,2,6)
plt.quiver(N,M)
plt.suptitle('Quiver Plots')
#Displaying the image
plt.show()