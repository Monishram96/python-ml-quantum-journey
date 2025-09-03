## CREATING A LIST AND SQUAREING THEM
numbers=[2,4,6,8,10,15,96]
def print_squares(nums):
    for num in nums:
        print(f"Square of {num} is {num**2}")
print_squares(numbers)



## GREETING NAMES
names=["Ram" , "Monish" , "Mram" ,"Moam"]
def greet_people(name_list):
    for name in name_list:
        print(f"hello, {name}!")
greet_people(names)



## MIN MAX SUM
numbers=[5,12,7,3,9]

maximum=max(numbers)
minimum=min(numbers)
total=sum(numbers)

print("Maximum:",maximum)
print("Minimum:",minimum)
print("Sum:",total)
