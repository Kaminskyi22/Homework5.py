
def amount_of_numbers(n):
    num_str = str(n).replace('.', '').replace('-', '').replace('+', '')
    return len(num_str)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

amount_input = input("Enter a number: ")

if is_number(amount_input):
    amount = float(amount_input)
    if amount.is_integer():
        amount = int(amount)
    print(f"The amount of digits in {amount} is: {amount_of_numbers(amount)}")
else:
    print("Please enter a valid number")

