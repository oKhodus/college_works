def screen_diagonal(dist_btw_scr_and_eyes):
    screen_diagonal_in_inches = float(dist_btw_scr_and_eyes) * 100 * 0.39 / 2.5
    x = round(screen_diagonal_in_inches)
    return x

userinp_dist = input("Enter the distance from the screen in meters: ")

try:
    res = screen_diagonal(userinp_dist)
    print(f"Screen diagonal should be {res} inches long.")
except ValueError:
    print("Enter a valid distance!")
    

# made by Oleksii Khodus