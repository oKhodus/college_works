def notor(a, b):
    return not (a or b)

def draw_table():
    print("~" * 13)
    print("| A | B |A↓B|")
    print("~" * 13)
    for a in [False, True]:
        for b in [False, True]:
            result = notor(a, b)
            print(f"| {int(a)} | {int(b)} | {int(result)} |")
            print("~" * 13)

draw_table()