def number_of_days(month):
    list_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return list_month.get(month, None)

print(number_of_days(3))
print(number_of_days(9))

# def main():
#     month_inp = int(input("Enter the month: "))
#     days = number_of_days(month_inp)
#     if days != None:
#         print(days)
#     else:
#         print("Incorrect input")
# main()