def main(num_cust="Enter the number of customers: "):
    try:
        num_customers = int(input(num_cust))
        if num_customers <= 0:
            raise ValueError

        total_flowers = 0
        current_customer = 1

        while current_customer <= num_customers:
            if current_customer % 2 != 0:
                total_flowers += current_customer
            current_customer += 1

        print(f"You will need to give away {total_flowers} flowers")

    except ValueError:
        incorrect_inp = "Invalid input. Please enter a positive integer: "
        main(num_cust=incorrect_inp)
main()
