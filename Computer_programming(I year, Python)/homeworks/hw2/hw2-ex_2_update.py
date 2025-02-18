def main(inp="Enter the number of a month (1-12): "):
    list_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    try:
        month_input = int(input(inp))

    except ValueError:
        incorrect_inp = "Invalid input, please enter a valid number: "
        main(inp=incorrect_inp)

    if 12 >= month_input >= 1:
        print(f"In this month {list_month[month_input]} days.")
    else:
        print("The number of a month must be in range [1-12]")
main()