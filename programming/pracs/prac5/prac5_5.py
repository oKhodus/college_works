# def main():
#     cents = int(input("Enter the number of cents: "))
#     euros = cents // 100
#     euros_remainder = cents % 100
#     if euros > 0 and euros_remainder > 0:
#         print(f"{euros} euro{'s' if euros > 1 else ''} and {euros_remainder} cent{'s' if euros_remainder > 1 else ''}")
#     elif euros > 0:
#         print(f"{euros} euro{'s' if euros > 1 else ''}")
#     elif euros_remainder > 0:
#         print(f"{euros_remainder} cent{'s' if euros_remainder > 1 else ''}")
#     else:
#         print("0 cents")
# main()
phrase = "No man is an island"
for a in phrase:
    print(a)