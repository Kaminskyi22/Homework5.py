def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

word = input("Enter a word: ")
if palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
    