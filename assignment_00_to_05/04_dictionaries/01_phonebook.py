def read_phone_numbers():
    phone_book = {}
    while True:
        name = input("Enter the name: ")
        if name == "":
            break
        number = input("Enter the phone number: ")
        phone_book[name] = number
    return phone_book

def print_phonebook(phone_book):
    for name, number in phone_book.items():
        print(f"{name}: {number}")

def lookup_number(phone_book):
    name = input("Enter the name to look up: ")
    if name in phone_book:
        print(f"The phone number for {name} is {phone_book[name]}")
    else:
        print(f"{name} is not in the phone book")

def main():
    phone_book = read_phone_numbers()
    print_phonebook(phone_book)
    lookup_number(phone_book)

if __name__ == "__main__":
    main()