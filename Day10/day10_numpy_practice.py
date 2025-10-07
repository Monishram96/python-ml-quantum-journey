import numpy as np

#Create an array of numbers from 0 to 19 and reshape it to 4x5
arr=np.arange(20).reshape(4,5)
print("4x5 array:\n",arr)

#Slice the 2nd row and 3rd column
print("2nd row:",arr[1,:])
print("3rd column:",arr[:2])

#Multiply all elements by 10
print("Array * 10:\n",arr*10)\n

#Find sum, mean
print("sum:",arr.sum())
print("mean:",arr.mean())

#Create 2 arrays and add them element-wise
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print("Elementwise sum:",arr1+arr2)
