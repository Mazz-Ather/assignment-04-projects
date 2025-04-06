def main():
    """
    Write a function that takes two numbers and finds the average between the two.
    """
    print('This program will find the average of two numbers.')
    num1 = int(input('Enter a number : '))
    num2 = int(input('Enter another number : '))
    print(f'The average of {num1} and {num2} is {(num1+num2)/2}')

if __name__ == '__main__':
    main()