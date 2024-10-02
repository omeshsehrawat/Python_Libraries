#Program to create a contour plot
import matplotlib.pyplot as plt
import numpy as np

#Creating large datasets
val1 = np.linspace(-9, 9, 600)
val2 = np.linspace(-5, 5, 500)

#Creating a meshgrid chart
A,B = np.meshgrid(val1, val2)
plt.figure(1, figsize=(15, 10))
plt.subplot(2, 4, 1)
plt.contour(A, B, A+B, alpha=.75, cmap='jet')
plt.subplot(2,4,2)
plt.contour(A, B, A+B, alpha=.75, cmap='jet')
plt.subplot(2,4,3)
plt.contour(A, B, A*B, alpha=.75, cmap='jet')
plt.subplot(2,4,4)
plt.contourf(A, B, A*B, alpha=.75, cmap='jet')
plt.subplot(2,4,5)
plt.contour(A, B, A-B, alpha=.75, cmap='jet')
plt.subplot(2,4,6)
plt.contourf(A, B, A-B, alpha=.75, cmap='jet')
plt.subplot(2,4,7)
plt.contour(A, B, B-A, alpha=.75, cmap='jet')
plt.subplot(2,4,8)

#Displaying the contour plot
plt.suptitle('Contour Plot')
plt.show()


