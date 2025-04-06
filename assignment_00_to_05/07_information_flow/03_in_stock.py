def main():
    fruit = input('Enter a fruit: ')
    stock = num_in_stock(fruit)
    if stock:
        print(f'There are {stock} {fruit}s in stock')
    else:
        print(f'{fruit} is not in stock')

def num_in_stock(fruit):
    if fruit == 'banana':
        return 5
    elif fruit == 'orange':
        return 10
    elif fruit == 'apple':
        return 3
    elif fruit == 'pear':
        return 6
    else:
        return None

if __name__ == "__main__":
    main()