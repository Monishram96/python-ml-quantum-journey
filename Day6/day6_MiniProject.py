import random
import os

BASE = os.path.dirname(__file__)
BEST_FILE = os.path.join(BASE, "guess_best.txt")

def read_best():
    if not os.path.exists(BEST_FILE):
        return None
    try:
        with open(BEST_FILE, "r") as f:
            return int(f.read().strip())
    except:
        return None

def write_best(attempts):
    with open(BEST_FILE, "w") as f:
        f.write(str(attempts))

def play_game(max_number):
    target = random.randint(1, max_number)
    attempts = 0
    print(f"\nI picked a number between 1 and {max_number}. Start guessing!")
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < target:
                print("Too low ")
            elif guess > target:
                print("Too high ")
            else:
                print(f"Correct! You guessed in {attempts} attempts 🎉")
                return attempts
        except ValueError:
            print("Enter a valid integer.")

def choose_difficulty():
    print("Choose difficulty: 1.Easy(1-50) 2.Medium(1-100) 3.Hard(1-200)")
    ch = input("Enter 1/2/3: ").strip()
    if ch == "1":
        return 50
    elif ch == "2":
        return 100
    else:
        return 200

def main():
    best = read_best()
    if best:
        print(f"Best score so far (least attempts): {best}")
    while True:
        max_num = choose_difficulty()
        attempts = play_game(max_num)
        if best is None or attempts < best:
            print("New best score! Saving...")
            write_best(attempts)
            best = attempts
        print("\nPlay again? (y/n)")
        if input().strip().lower() != "y":
            print("Thanks for playing — goodbye!")
            break

if __name__ == "__main__":
    main()
