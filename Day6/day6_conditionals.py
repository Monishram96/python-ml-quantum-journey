
def even_or_odd():
    n=int(input("enter the integer:"))

    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")

def largest_of_three():
    print("enetr the three no:")
    a,b,c= map(float,input().split())
    if a>=b and a>=c:
        largest=a
    elif b>=a and b>=c:
        largest=b
    else:
        largest=c
    print("Largest is:",largest)

def grade_from_marks():
    marks=float(input("eneter the marks(0-100): "))
    if marks >= 90:
        grade = "A"
    elif marks >= 70:
        grade="B"
    elif marks >=50:
        grade="C"
    else:
        grade="FAIL"
    print("Grade:",grade)

if __name__== "__main__":
    print("choice 1.even/odd 2.largest 3.grade")
    ch=input("eneter the choice(1/2/3):")
    if ch=="1":
        even_or_odd()
    elif ch=="2":
        largest_of_three()
    elif ch=="3":
        grade_from_marks()
    else:
        print("invalid choice")
