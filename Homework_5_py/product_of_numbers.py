def product_of_numbers():
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    
    if lower > upper:
        lower, upper = upper, lower

    product = 1
    for i in range(lower, upper + 1):
        product *= i
    
    return product

result = product_of_numbers()
print(f"The product of numbers in range is: {result}")
