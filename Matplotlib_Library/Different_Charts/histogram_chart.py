#Program to display a histogram
import matplotlib.pyplot as plt

#Creating a histogram using hist2d() function
list1 = list(range(1,10,2))
list2 = [12,15,17,19,15]
plt.hist2d(list1, list2)

#Displaying the histogram
plt.show()


