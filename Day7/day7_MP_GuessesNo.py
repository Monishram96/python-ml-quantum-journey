import random

def player_guesses():
    number=random.randint(1,100)
    attempts=0
    print("\n--- player guesses the number(1-100)---")
    while True:
        try:
            guess=int(input("your  guess:"))
            attempts+=1
            if guess < number:
                print("too low")
            elif guess > number:
                print("too high")
            else:
                print(f"correct in {attempts} atttempts!")
                break
        except ValueError:
            print("enter the valid number")
def computer_guesses():
    low,high = 1,100
    attempts =0
    print("\n---Computer guesses your number")
    input("Think of a number betweeen 1 and 100.press Enter when ready...")
    while low<=high:
        attempts += 1
        guess=(low+high)//2
        print(f"computer guesses:{guess}")
        feedback = input("is it (h)igh, (l)ow, or (c)orrect?").lower()
        if feedback == "c":
            print(f"computer got it in {attempts} attempts")
            break
        elif feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
        else:
            print("invalid input,use h/l/c")
def main():

    print("choose Mode: 1. you guess  2. computeer guess  3.exit :")
    while True:
        choice=input("enter 1/2/3:").strip()
        if choice=="1":
            player_guesses()
        elif choice=="2":
            computer_guesses()
        elif choice=="3":
            print("exit")
            break
        else:
            print("invalid choice")

if __name__=="__main__":
    main()
