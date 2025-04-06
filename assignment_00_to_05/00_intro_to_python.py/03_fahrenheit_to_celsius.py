def main():
    print('This program will convert Fahrenheit To Celsius')
    while True:
        user_input = input('Enter temperature in Fahrenheit .')
        try:
            fahrenheit = float(user_input)
            break
        except ValueError:
            print('invalid conversion , please enter a numerical value : ')
        
    degrees_celsius = (fahrenheit - 32) * 5.0/9.0
    print('------------------------------------------------------------------')
    print(fahrenheit , " Fahrenheit is equal to " , degrees_celsius  , "celsius")
    print('------------------------------------------------------------------')
    
if __name__ == '__main__':
    main()