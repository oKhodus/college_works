from req import converter_currency, total_currs
from sys import argv

if len(argv) == 2 and argv[1] == "-help":
    print(total_currs())

else:
    amount = float(input("Enter an amount of money you wanna converted: "))
    from_currency = input("Enter base currency (e.g., USD): ").upper()
    to_currency = input("Enter target currency (e.g., EUR): ").upper()

    print(converter_currency(amount, from_currency, to_currency))
