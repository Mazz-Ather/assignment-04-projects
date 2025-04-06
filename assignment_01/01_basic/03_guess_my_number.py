import random

def main():
    number = random.randint(1, 100)
    guess = 0
    # print("Guess a number between 1 and 100:")
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")

    print("You guessed it right!")

if __name__ == "__main__":
    main()