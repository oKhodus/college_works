def main():
    user_word = input('Enter a word: ')
    lower_word = user_word.lower()
    if lower_word == lower_word[::-1]:
        print(f"Yeah {lower_word} is palindrome")
    else:
        print(f"Nope {lower_word} is not palindrome")
main()