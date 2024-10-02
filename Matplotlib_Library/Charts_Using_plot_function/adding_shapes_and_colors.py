#Program to display multiple lines with different shapes and colors
import matplotlib.pyplot as plt

#Creating four lists
a = list(range(1,11))
b = list(range(5,55,5))
c = list(range(10,110,10))
d = list(range(20,210,20))
print("First list:", a)
print("Second list:", b)
print("Third list:", c)
print("Fourth list:", d)

#Creating a chart with different colors and effects for different data
plt.plot(a, a, 'g^', a, b, 'bs', a, c, 'r--', a, d, 'mo')

#Set limits of x-axis
plt.xlim(0, 11)

#Set limits of y-axis
plt.ylim(0, 220)

plt.xlabel('X axis')
plt.title('Multiple lines with different shapes and colors')

#Displaying grid in chart
plt.grid(True, color='k')

#Displaying the chart
plt.show()