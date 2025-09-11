##creating SETS

a={1,2,3,2,3}
b={3,4,5}
print("a:",a)
print("b:",b)


### ADDING AND DISCARDING ELEMENTS

a.add(10)
a.discard(2)
print("a after:",a)


#### SET OPERATION

print("Union:", a|b)
print("Intersection", a&b)
print("Difference:", a-b)
print("Symmetric:", a^b)


### RREMOVING DUPLICATE ELEMENTS IN LIST

nums=[1,1,2,2,3,4,4,4,5,5,5,5,]
unique=list(set(nums))
print("Unique:",unique)



##PRACTICE##

"""UNIQUE DETECTION"""

nums=[1,1,2,2,3,4,4,4,5,5,5,5,]
unique_sorted=sorted(set(nums))
print("Unique & Sorted:",unique_sorted)

"""INCERTIION OF TWO NO"""

a={1,2,3,4}
b={3,4,5,6}
print("Set A:",a)
print("Set B:",b)
print("Intersetion:",a&b)

"""SET COMPREHENSION"""
squares={x*x for x in [1,2,3,4]}
print("Squares:",squares)
