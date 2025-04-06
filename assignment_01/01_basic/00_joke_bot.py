PROMPT = "What do you want to say? "
JOKE = "Here is a joke for you: \nSophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'."
SORRY = "Sorry, I only tell jokes."

def main():
    """Returns a joke if the input is 'joke', else returns an apology message."""
    
    # Get user input
    user_input = input(PROMPT).strip().lower()

    # Check the input and return the appropriate message
    if user_input == "joke":
        print(JOKE)
    else:
        print(SORRY)

# Run the program
if __name__ == "__main__":
    main()
