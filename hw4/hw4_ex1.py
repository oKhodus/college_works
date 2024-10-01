def main():
    inp = int(input("Please enter a number: "))
    n = 1
    while n <= 9:
        result = inp * n
        print(f"{inp} * {n} = {result}" )
        n += 1
main()