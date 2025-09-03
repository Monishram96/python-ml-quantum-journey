## FIBONACCI SEQUENCE
def fibonacci(n):
    sequence=[]
    a,b=0,1
    for _ in range(n):
        sequence.append(a)
        a,b=b,a+b
    return sequence
n=10
print(f"first {n} Fibonacci numbers:{fibonacci(n)}")



## CALCULATOR
def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def diviide (a,b):
    if b!=0:
        return a/b
    else:
        return "error in the no."
print("select operator: 1.Add 2.Subtract 3.Multiply 4.Divide")
choice=int(input("enter the choice(1/2/3/4):"))

x=float(input("enter the first no:"))
y=float(input("enter the second no:"))

if choice==1:
    print("result:",add(x,y))
elif choice==2:
    print("result:",subtract(x,y))
elif choice==3:
    print("result:",multiply(x,y))
elif choice==2:
    print("result:",divide(x,y))
else:
    print("Invlid choice:")
