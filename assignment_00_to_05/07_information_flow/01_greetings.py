def main():
    name : str = input("Enter your name: ")
    print(greet(name))

def greet(name: str) -> str:
    return f" Greetings, {name}!"

if __name__ == "__main__":
    main()