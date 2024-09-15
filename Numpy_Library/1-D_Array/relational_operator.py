#Program to shows relational operators on array
import numpy as np
myarray22 = np.array([215,323,520,636,717,281,162,411], int)
myarray23 = np.array([311,453,711,362,230,453,672,891], int)

#Using greater than or equal to (>=) relational operator
print("Are elements of first array >= corresponding elements of second array?\n", myarray22 >= myarray23)

#Using less than or equal to (<=) relational operator
print("Are elements of first array <= corresponding elements of second array?\n", myarray22 <= myarray23)

#Using equal to (==) relational operator
print("Are elements of first array = corresponding elements of second array?\n", myarray22 == myarray23)

#Using not equal to (!=) relational operator
print("Are elements of first array!= corresponding elements of second array?\n", myarray22!=myarray23)