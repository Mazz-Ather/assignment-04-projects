def main():
    curr_val = int(input("Enter a positive integer: "))
    while curr_val < 100:
        curr_val = curr_val * 2
        print(curr_val , end=' ')

if __name__ == '__main__':
    main()