inches_in_foot = 12
def main():
    feet : float = float(input("Enter number in feet : "))
    inches : float = feet * inches_in_foot
    print('--------------------------------------------')
    print(feet , " feet is equal to" , inches , 'inches')
    print('--------------------------------------------')

if __name__ == '__main__':
    main()