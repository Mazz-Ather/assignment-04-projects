"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""
import random
num_sides  = 6 

def roll_dice():
    """
    Simulate two dice and prints their total
    """
    die1 :int = random.randint(1 , num_sides)
    die2 : int = random.randint(1 , num_sides)
    total : int = die1 + die2 
    print('Die 1 is : ' , die1 , "Die 2 is : " , die2)
    print('Total of two dice : ' , total)

def main():
    die1 : int = 10
    print('die in main is ' , die1 ) 

    for _ in range(3):
        print('--------------------------------------')
        roll_dice()
        print('--------------------------------------')

if __name__ == '__main__':
    main()