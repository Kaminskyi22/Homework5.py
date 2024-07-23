def draw_square():
    side_length = int(input("Enter the side length of the square: "))
    symbol = input("Enter the symbol to use: ")
    filled = input("Enter True for a filled square or False for an empty square: ").lower() == 'true'
    
    for i in range(side_length):
        if filled:
            print(symbol * side_length)
        else:
            if i == 0 or i == side_length - 1:
                print(symbol * side_length)
            else:
                print(symbol + ' ' * (side_length - 2) + symbol)


draw_square()
