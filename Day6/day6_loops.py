import math

def multiplication_table():
    n = int(input("Enter number for table: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def sum_first_n_for():
    n = int(input("Enter N: "))
    total = 0
    for i in range(1, n+1):
        total += i
    print(f"Sum using for: {total}")

def sum_first_n_while():
    n = int(input("Enter N: "))
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print(f"Sum using while: {total}")

def factorial():
    n = int(input("Enter n for factorial: "))
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"{n}! = {fact}")

def skip_even_demo():
    print("Printing odd numbers from 1 to 20 (skip even):")
    for i in range(1, 21):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()

def is_prime():
    n = int(input("Enter number to check prime: "))
    if n <= 1:
        print(n, "is not prime")
        return
    if n <= 3:
        print(n, "is prime")
        return
    if n % 2 == 0:
        print(n, "is not prime")
        return
    r = int(math.sqrt(n))
    for i in range(3, r+1, 2):
        if n % i == 0:
            print(n, "is not prime")
            return
    print(n, "is prime")

    if __name__ == "__main__":
        print("Choose: 1.Table 2.Sum(for) 3.Sum(while) 4.Factorial 5.Skip-even 6.Prime 7.Exit")
        ch = input("Enter choice (1-7): ").strip()
        if ch == "1":
            multiplication_table()
        elif ch == "2":
            sum_first_n_for()
        elif ch == "3":
            sum_first_n_while()
        elif ch == "4":
            factorial()
        elif ch == "5":
            skip_even_demo()
        elif ch == "6":
            is_prime()
        elif ch == "7":
            print("Exite")
        else:
            print("Invalid choice")
