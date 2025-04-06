def main():
    fruits = {'apple': 1.5, 'banana': 0.5, 'orange': 0.75, 'pear': 0.25, 'kiwi': 0.5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print("Your total is $" + str(total_cost))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()