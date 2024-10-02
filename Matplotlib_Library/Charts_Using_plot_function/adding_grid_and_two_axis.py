#Program for creating line chart with grids and special effects
import matplotlib.pyplot as plt

plt.plot([7,5,8,11,13,9,11],[5,7,9,12,15,16,17], color = 'g', linewidth = 5.0)

#Displaying title of the chart
plt.title('Chart with user defined color and width of line')

#Label on x-axis
plt.xlabel('X axis')

#Label on y-axis
plt.ylabel('Y axis')

#Displaying a grid
plt.grid(True)

#Displayng text on the plot area
plt.text(5, 12, 'Green Colored Line')

#Displaying the chart
plt.show()