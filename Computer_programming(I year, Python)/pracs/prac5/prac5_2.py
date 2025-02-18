def main():
    user_inp = input("Enter a personal number: ")
    if int(user_inp[0]) % 2 == 0:
        print("Congrats you are a woman")
    else:
        print("Congrats you are a man")
main()
# GYYMMDDSSSC
# where G shows gender (odd numbers for a male, even numbers for a female)