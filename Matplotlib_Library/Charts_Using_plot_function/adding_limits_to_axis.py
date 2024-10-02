#Program to draw dot and lines on the same chart with axes limit
import matplotlib.pyplot as plt
plt.plot([6,9,7,11,13], [8,11,13,12,15], 'ro', [6,9,7,11,13], [8,11,13,12,15], 'm')

#Adding label to the x-axis
plt.xlabel('X axis')

#Adding label to the y-axis
plt.ylabel('Y axis')

#Adding title to the chart
plt.title("Dot and Line chart together")

#Setting the limit of both the axes
plt.axis([5,15,5,17])

#Displaying the chart
plt.show()