#Program for creating a chart considering gglot from style
import matplotlib.pyplot as plt
import matplotlib.style
matplotlib.style.use('ggplot')

#Creating a line chart with gglot
plt.plot([16,12,11,10,12,8,4,17,9,11,15,14,13])
plt.ylabel('Random Numbers')

#Displaying a chart
plt.show()
