FILENAME="students.txt"
def add_student(name,marks):
    try:
        marks =int(marks)
        with open(FILENAME,"a") as f:
            f.write(f"{name},{marks}\n")
        print(" Added {name} with marks{marks}")
    except ValueError:
        print("Error : marks must be in a number.")
def view_students():
    try:
        with open(FILENAME,"r") as f:
            lines = f.readlines()
            if not lines:
                print("NO records found.")
            else:
                print("\n student records:")
                for line in lines :
                    try:
                        name,marks=line.strip().split(",")
                        print(f" - {name}:{marks}")
                    except ValueError:
                        print(f" skipped invalid line:{line.strip()}")
    except FileNotFoundError:
        print("no records file found yet.")
if __name__ == "__main__":
    while True:
        print("\n1.add student\n2.view student\n3.exit")
        choice=input("enter choice")

        if choice == "1":
            name=input("enter the name:")
            marks=int(input("enter the marks:"))
            add_student(name,marks)

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("exit")
            break
        else:
            print("invalid coice:try again later")
            
