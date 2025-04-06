def get_user_number():
    """
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number or press enter to stop: ")
        if user_input == "":
            break
        user_numbers.append(user_input)
    return user_numbers

def count_nums(numbers):
    """
    Count the number of numbers in a list.
    """
    num_dict = {}
    for num in numbers:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict


def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")
 
def main():
    user_numbers = get_user_number()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()