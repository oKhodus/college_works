def price_difference(init_price, month_payment, num_of_month):
    total_payment = month_payment * num_of_month
    res = total_payment - init_price
    print(res)
price_difference(200, 20, 12)