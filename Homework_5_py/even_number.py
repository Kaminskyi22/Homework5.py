def even():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    print(f"The even numbers between {a} and {b} are:", end=" ")
    
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")
    
even()
