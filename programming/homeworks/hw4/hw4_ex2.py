def number_of_days():
    list_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    month_input = input("Enter the number of a month (1-12) or word |done| to quit: ")

    while month_input.lower().strip() != "done":

        try:

            month_input = int(month_input)

            if 12 >= month_input >= 1:
                print(f"In this month {list_month[month_input]} days.")
            else:
                print("The number of a month must be in range [1-12]")

        except ValueError:
            incorrect_inp = "Invalid input, please enter a valid number"
            print(incorrect_inp)
        month_input = input("Enter the number of a month (1-12) or word |done| to quit: ")

    print(f"Your program was stopped, because your last input was |{month_input.strip()}|.")

number_of_days()