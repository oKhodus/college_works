def main(amount): 
    try:
        name_of_currency_before = input("Current currency: ").lower()
        name_of_currency_after = input("Exchange into: ").lower()
        amount = float(amount)
        
        if name_of_currency_before == "dollar" and name_of_currency_after == "euro":
            eur = float(amount) / 1.17
            print(eur)     
        elif name_of_currency_before == "euro" and name_of_currency_after == "dollar":
            dollar = float(amount) * 1.17
            print(dollar)
        else:
            print("Invalid currency or something goes wrong///")
    except:
        print("I don't understand you")
amount_of_money = input("The Amount of money to convert: ")

main(amount_of_money)

# made by Oleksii Khodus




