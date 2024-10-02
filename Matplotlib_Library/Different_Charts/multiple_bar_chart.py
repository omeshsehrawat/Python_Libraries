#Program for drawing multiple bar charts on one image
import matplotlib.pyplot as plt
ecommerce = ['Myntra', 'Snapdeal', 'Alibaba', 'Amazon', 'Flipkart']
Q1_Profit = [35,45,100,70,40]
Q2_Profit = [38,40,105,65,45]
Q3_Profit = [30,42,120,72,50]
Q4_Profit = [25,34,115,60,48]

#Creating different bar charts on one image using subplot() function
plt.figure(1, figsize=(10, 10))

#Creating bar chart in first cell of figure having 2 rows, 3 columns
plt.subplot(221)
plt.bar(ecommerce, Q1_Profit)
plt.title("Quarter1 Profit")

#Creating a bar chart in second cell
plt.subplot(2,2,2)
plt.bar(ecommerce, Q2_Profit)
plt.title('Quarter2 Profit')

#Creating a bar chrat in third cell
plt.subplot(223)
plt.bar(ecommerce, Q3_Profit)
plt.title('Quarter3 Profit')

#Creating a bar chart in fourth cell
plt.subplot(2,2,4)
plt.bar(ecommerce, Q4_Profit)
plt.title('Quarter4 Profit')

#Adding a Main title for the figure
plt.suptitle('Profit on Quarter Basis')

#Displaying the chart
plt.show()