#Program for creating a pie chart
import matplotlib.pyplot as plt
list1 = [10,30,40,30,60,70,80,100,70,40]

#Creating and displaying a pie chart
plt.pie(list1, labels=list1)
plt.show()