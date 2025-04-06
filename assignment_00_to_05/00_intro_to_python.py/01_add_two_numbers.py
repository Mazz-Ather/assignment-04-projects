def main():
    print('This Program Adds Two Numbers')
    num1 : str = input("Enter First Number : ")
    num1 : int = int(num1)
    num2 :str = input("Enter Second Number : ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print('*******************************************')
    print(f"The total is {total}")
    print('*******************************************')

if __name__ == '__main__':
    main()