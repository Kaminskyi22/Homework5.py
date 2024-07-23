def find_minimum():
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    return min(numbers)

result = find_minimum()
print(f"The minimum number is: {result}")
