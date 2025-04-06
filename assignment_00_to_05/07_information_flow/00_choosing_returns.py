ADULT_AGE = 18

def is_adult(age):
    """
    Determines if a person is an adult based on their age.
    """
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    if is_adult(age):
        print("You are an adult!")
    else:
        print("You are not an adult yet.")

if __name__ == "__main__":
    main()