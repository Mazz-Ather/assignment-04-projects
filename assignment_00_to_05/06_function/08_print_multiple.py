def print_multiple(message , repeats):
    """
    Prints multiple messages .
    """
    print((message + " ") * repeats)

def main():
    message = input("Enter a message: ")
    repeats = int(input("How many times should I print it? "))
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()