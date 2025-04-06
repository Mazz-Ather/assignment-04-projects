def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high  # Uses chained comparison for better readability

def main():
    # Get user input
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    # Check if the number is in range and print result
    if in_range(n, low, high):
        print(f"{n} is in the range [{low}, {high}].")
    else:
        print(f"{n} is NOT in the range [{low}, {high}].")

# Run the main function
if __name__ == "__main__":
    main()
