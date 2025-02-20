# import os.path

def min_price(pr, rests):
    min_price = min(pr)
    min_index = pr.index(min_price)
    min_rest = rests[min_index]
    print(f"Minimum price is {min_price} EUR is in {min_rest}")

def avg_price(pr):
    avg = sum(pr) / len(pr)
    return avg

def price_range(pr):
    diff = avg_price(pr) - min(pr)
    return diff

def open_file():
    try:
        with open("food.txt") as file:
            lines = file.readlines()
    except FileNotFoundError as nf:
        print(f"{nf} \
              \nMake sure that your file has a correct name")
        return
    
    rests = []
    prices = []
    dish = input("What dish would you like to have? ")

    for line in lines:
        try:
            rest, rest_info = line.strip().split(" - ")
            rest_dish, price = rest_info.split(", ")
            if rest_dish.lower() == dish:
                rests.append(rest)
                prices.append(float(price))
                print(f"You can have {dish} in {rest} for {price} EUR")

        except ValueError as v:
            continue

    if not rests:
        print(f"This dish is not served in restaurants of Narva")
        return
    
    diff = price_range(prices)
    avg = avg_price(prices)
    
    print(f"\nDifference between min and avg prices is {diff:.1f} EUR")
    min_price(prices, rests)
    print(f"Average price is {avg:.1f} EUR")
    
open_file()