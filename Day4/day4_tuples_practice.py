## TUPLES

num=(1,2,3,4,5)
print("tuple:",num)


### SLICING

print("First:",num[0])
print("sclice 1...3:",num[1:4])


### METHODS

letters=("a","b","a","c","a")
print("Count of 'a':",letters.count("a"))
print("index of 'b':",letters.index("b"))


### UNPACKING

point=(3,7)
x,y=point
print("Unpacking:",x,y)


### MULTIPLE VALUES FROM FUNCTION
def min_max_sum(values):
    return min(values),max(values),sum(values)
mn=min_max_sum(num)
print("min_max_total:",mn)



###PRACTICE###
my_list=[1,2,3]
my_tuple=tuple(my_list)
print(my_tuple)


mn,mx,total=min_max_sum(num)
print("Min:",mn)
print("Max:",mx)
print("Total:",total)
