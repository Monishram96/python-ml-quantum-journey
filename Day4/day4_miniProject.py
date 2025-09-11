students={}
while True:
    print("\n---Student Grade Management---")
    print("1.add the students name:")
    print("2.view all students name:")
    print("3.search students name:")
    print("4.update student marks:")
    print("5.delete student:")
    print("6.exit:")

    choice=input("enter the choice (1-6):")

    if choice=="1":
        name=input("Enter the students name:")
        marks=int(input("Enter the student marks:"))
        students[name]=marks
        print(f"{name}added succesfully:")

    elif choice=="2":
        if students:
            for name,marks in students.items():
                print(f"{name}:{marks}")
        else:
            print(" No student found")

    elif choice=="3":
        name=input("enter student name to search:")
        print(f"{name}:{students.get(name,'not found')}")

    elif choice=="4":
        name=input("Enter the student name:")
        if name in students:
            new_marks=float(input("enter the new marks:"))
            students[name]=new_marks
            print(f"{name} is updated succesfully:")
        else:
            print("student is not found")

    elif choice=="5":
        name=input("enter the student name:")
        if name in students:
            del students[name]
            print(f"{name} is deleted")
        else:
            print("student not found")

    elif choice=="6":
        print("exiting the process:")
        break

    else:
        print("invalid choice.try again.")
