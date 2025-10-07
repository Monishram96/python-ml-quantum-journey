## LAMBDA BASICS
square = lambda x: x**2
print("square of 5:",square(5))

add=lambda a,b:a+b
print("sum of 10+7:", add(10,7))

print("cube of 3:",(lambda x: x**3)(3))


## LAMBDA WITH MAP
numbers=[1,2,3,4,5]

squared=list(map(lambda x: x**2,numbers))
print("Squared nmbers:",squared)

multiplied= list(map(lambda x: x*10, numbers))
print("numbers * 10:",multiplied)


## LAMBDA WITH FILTER
filtered = list(filter(lambda x: x > 3,numbers))
print("Numbers>3:",filter)

evens=list(filter(lambda x: x%2 == 0,numbers))
print("even numbers",evens)


## LAMBDA WITH REDUCE
from functools import reduce

#sum of all num
total=reduce(lambda a,b:a+b,numbers)
print("sum of numbers:",total)

#multiply all numbers
product = reduce(lambda a,b: a*b,numbers)
print("product of numbers:",product)
