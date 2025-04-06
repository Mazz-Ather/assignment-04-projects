import random
DONE_LIKELIHOOD = 0.2

def done():
    return random.random() < DONE_LIKELIHOOD

def caotic_counting():
    """Counts from 1 to 10, but stops randomly when done() returns True."""
    for i in range(1, 11):
        if done():
            return
        print(i , end = ' ')

def main():
    """Runs caotic_counting() until it returns a value."""
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    caotic_counting()
    print("\nI'm done.")  # This prints once chaotic_counting() is finished

# Run the main function
if __name__ == '__main__':
    main()