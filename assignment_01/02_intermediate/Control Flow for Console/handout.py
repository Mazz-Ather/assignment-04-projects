import random

NUM_ROUNDS = 5

def main():
    """
    Welcome to high low level game
    """
    print("------------------------------------------------")
    print("Welcome to the high low level game")
    print("You have to guess a number between 1 and 100")
    print("You have 5 rounds")
    print("Good luck!")
    print("------------------------------------------------")

    score = 0
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        
        computer_guess = random.randint(1, 100)
        user_guess = random.randint(1, 100)
        print("your guess is : ", user_guess)

        while True:
            guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if guess not in ["higher", "lower"]:
                print("Invalid input. Please enter 'higher' or 'lower'.")
            else:
                break

        if (guess == "higher" and user_guess > computer_guess) or (guess == "lower" and user_guess < computer_guess):
            print("----------------------------------------------------------------------")
            print("Correct! You win this round.")
            print("----------------------------------------------------------------------")
            
            score += 1

        else:
            print("----------------------------------------------------------------------")
            print("Sorry, you lose this round. The computer's number was", computer_guess)
            print("----------------------------------------------------------------------")

    print("------------------------------------------------")
    print("Game over! Your score is:", score)
    print("------------------------------------------------")

    if score == NUM_ROUNDS:
        print("Congratulations! You played perfectly!")
    elif score > NUM_ROUNDS // 2:
        print("You played well! Keep up the good work!")

    else:
        print("You played poorly. Better luck next time!")

if __name__ == "__main__":
    main()