def get_user_info():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    age = int(input('Enter your age: '))
    return name, age , email

def main():
    name, age, email = get_user_info()
    print(f'Hello {name}, your email is {email} and you are {age} years old.')

if __name__ == "__main__":
    main()