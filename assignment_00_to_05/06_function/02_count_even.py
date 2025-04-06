def count_even():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            lst.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer or press enter to stop.")

    even_count = sum(1 for num in lst if num % 2 == 0)
    
    print("The number of even integers in the list is:", even_count)
    # return lst

if __name__ == "__main__":
    count_even()