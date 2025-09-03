## EVEN OR ODD
def check_O_E(number):
    if number%2==0:
        return "EVEN"
    else:
        return "ODD"
num=int(input("Enter the number:"))
print(f"{num} is {check_O_E(num)}")




## FACTORIAL OF NO
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
num=int(input("Enter the factorial no:"))
print(f"Factorial of {num} is {factorial(num)}")
