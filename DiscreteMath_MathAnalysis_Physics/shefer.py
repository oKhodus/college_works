def notand(a, b):
    return not (a and b)

def draw_table():
    print("~" * 13)
    print("| A | B |A↑B|")
    print("~" * 13)
    for a in [True, False]:
        for b in [True, False]:
            result = notand(a, b)
            print(f"| {int(a)} | {int(b)} | {int(result)} |")
            print("~" * 13)

draw_table()