#Program to shows relational operators on multidimensional array
import numpy as np
mymultarray12 = np.array([[115,123,120],[130,117,281]], int)
mymultarray13 = np.array([[111,153,111],[162,130,153]], int)

#Using greater than or equal to (>=) relational operator
print("Are elements of first array >= corresponding elements of secon array?\n", mymultarray12 >= mymultarray13)

#Using less than or equal to (<=) relational operator
print("Are elements of first array <= corresponding elements of secon array?\n", mymultarray12 <= mymultarray13)

#Using equals (==) relational operator
print("Are elements of first array = corresponding elements of secon array?\n", mymultarray12 == mymultarray13)

#Using not equal to (!=) relational operator
print("Are elements of first array != corresponding elements of secon array?\n", mymultarray12 != mymultarray13)