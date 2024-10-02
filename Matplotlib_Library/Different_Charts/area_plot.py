#Program to create an area plot
import matplotlib.pyplot as plt
month_sales = [1,2,3,4,5,6,7,8,9,10,11,12]
Electronics = [8,11,9,8,10,9,10,11,12,9,10,11]
Clothing = [8,7,8,6,8,7,5,8,5,7,8,6]
Food = [5,6,2,4,6,5,2,4,2,3,4,5]
Books = [3,4,5,3,3,6,6,2,6,5,3,4]

plt.plot([], [], color='pink', label='Books', linewidth=5)
plt.plot([], [], color='blue', label='Food', linewidth=5)
plt.plot([], [], color='red', label='Clothing',  linewidth=5)
plt.plot([], [], color='cyan', label='Electronics', linewidth=5)

plt.stackplot(month_sales, Books, Food, Clothing, Electronics, colors=['pink', 'blue', 'red', 'cyan'])
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Area Chart for sales of different categories')
plt.legend()

#Displaying the chart
plt.show()