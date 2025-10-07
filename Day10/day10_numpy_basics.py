import numpy as np

## ARRAY ATTRIBUTES
arr1=np.array([1,2,3,4,5])
print("1D array:",arr1)

arr2=np.array([[1,2,3],[4,5,6]])
print("2D array:\n",arr2)

print("shape of arr2:",arr2.shape)
print("Number of dimensions:",arr2.ndim)
print("Data type:",arr2.dtype)

##INDEXING AND SLICING

#INDEXING
print("arr1[0]:",arr1[0])
print("arr1[-1]:",arr1[-1])

#SLICING
print("arr1[1:4]:",arr1[1:4])

#2D INDEXING
print("arr2[0,1]:",arr2[0,1])
print("arr2[:,2]:",arr2[:,2])

## BASIC OPERATIONS
arr3=np.array([10,20,30,40,50])

print("arr3 + 5:",arr3 + 5)
print("arr3 * 2:",arr3 * 2)
print("arr3 ** 2:",arr3 ** 2)

arr4=np.array([1,2,3,4,5])
print("arr3+arr4:",arr3 + arr4)

## USEFUL FUNCTION

print("sum:",arr3.sum())
print("mean:",arr3.mean())
print("max:",arr3.max())
print("min:",arr3.min())
print("standard deviation:",arr3.std())
