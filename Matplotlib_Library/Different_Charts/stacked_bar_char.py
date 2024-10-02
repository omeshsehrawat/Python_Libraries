#Program to create a stacked bar chart
import matplotlib.pyplot as plt
plt.figure(1, figsize=(10,5))
countries = ['A', 'B', 'C', 'D', 'E']
Population_1930 = [10,20,24,30,20]
Population_1940 = [12,27,30,42,26]
Population_1950 = [15,35,34,50,33]
Population_1960 = [27,43,43,57,38]
Population_1970 = [35,45,46,62,40]
Population_1980 = [38,49,55,65,45]
Population_1990 = [42,52,60,72,50]
Population_2000 = [48,54,65,75,58]
Population_2010 = [53,58,70,77,63]

#Creating a stacked bar chart
plt.bar(countries, Population_2010, color='green')
plt.bar(countries, Population_2000, color='red')
plt.bar(countries, Population_1990, color='yellow')
plt.bar(countries, Population_1980, color='blue')
plt.bar(countries, Population_1970, color='brown')
plt.bar(countries, Population_1960, color='orange')
plt.bar(countries, Population_1950, color='purple')
plt.bar(countries, Population_1940, color='magenta')
plt.bar(countries, Population_1930, color='pink')

#Adding labels and title to the chart
plt.xlabel('Countries')
plt.ylabel('popultion in different years')
plt.title('Stacked Bar Chart')

#Displaying a bar chart 
plt.show()