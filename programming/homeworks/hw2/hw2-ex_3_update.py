def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main(inp="Enter the number of a month (1-12): ", inp2="Enter a year: "):
    try:
        list_month = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        month_input = int(input(inp))
        year_input = int(input(inp2))
        if 12 >= month_input >= 1:
            if month_input == 2 and leap_year(year_input):
                print(f"In {year_input} year, February has 29 days (a leap year).")
            else:
                print(f"In {year_input} year, that month has {list_month[month_input]} days (a common year).")
        else:
            print("The number of a month must be in range [1-12]")
            main()
    except ValueError:
        incorrect_inp = "Invalid input, please enter a valid number: "
        main(inp=incorrect_inp)
main()
