#Program to draw a scatter plot
import matplotlib.pyplot as plt
ecommerce = ['Myntra', 'Snapdeal', 'Alibaba', 'Amazon', 'Flipkart']
Q1_Profit = [35,45,100,70,40]
Q2_Profit = [38,40,105,65,45]
Q3_Profit = [30,42,120,72,50]
Q4_Profit = [25,34,115,60,48]

#Creating a scatter plot
plt.scatter(ecommerce, Q1_Profit, color='green')
plt.scatter(ecommerce, Q2_Profit, color='blue')
plt.scatter(ecommerce, Q3_Profit, color='pink')
plt.scatter(ecommerce, Q4_Profit, color='red')

#Adding title to the chart and labels to the axis
plt.xlabel('Organization Name')
plt.ylabel('Profit')
plt.title('Scatter Plot')

#Displaying a scatter plot
plt.show()

