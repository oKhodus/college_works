def price_difference(init_price, month_payment, num_of_month):
    total_payment = month_payment * num_of_month
    difference = total_payment - init_price
    return difference

def main():
    message_month_payment = "What is the monthly payment on the {} installment plan? "
    message_num_month = "How many months does the {} installment plan last? "
    this_better = "The {} installment is better!"

    init_price = float(input("What is the price of the product? "))

    month_payment_inp1 = float(input(message_month_payment.format("first")))
    num_of_month_inp1 = int(input(message_num_month.format("first")))

    month_payment_inp2 = float(input(message_month_payment.format("second")))
    num_of_month_inp2 = int(input(message_num_month.format("second")))

    res1 = price_difference(init_price, month_payment_inp1, num_of_month_inp1)
    res2 = price_difference(init_price, month_payment_inp2, num_of_month_inp2)

    if res1 < res2:
        print(this_better.format("first"))
    elif res1 > res2:
        print(this_better.format("second"))
    else:
        print("Both installments are equal.")

main()