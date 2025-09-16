## ERROR HANDLING ##
""" ERROR HANDLING means writing code in a way that your program doesn't crash when something goes WROMG instead it catches the error and give frindly message"""
try:
    num = int(input("Enter the number:"))
    print("100 divided by your number is :",100/num)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter the valid integer.")
finally:
    print("Execution finished.")
    
