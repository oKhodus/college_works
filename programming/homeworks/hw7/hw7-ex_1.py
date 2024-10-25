import statistics as st

def conv_celsfahr(file_inp):
    count = 0
    empt = []
    with open(file_inp) as file:
        elems = file.readlines()
        for val in elems:
            l = val.split("\n")
            base = "".join(l)

            fl_base = float(base)
            

            out = fl_base * 1.8 + 32
            empt.append(out)
            count += 1

            print(f"Value number {count}:\nIn celsius it was: {fl_base:.1f} (°C) \
            \nIn Fahrenheit it will be: {out:.1f} (°F)\n")

        avg = st.mean(empt)
        mn = min(empt)
        mx = max(empt)
        print(f"The average temperature is: {avg:.1f} (°F)\
              \nThe minimum is: {mn} (°F)\nThe maximum is: {mx} (°F)")

conv_celsfahr("temps.txt")


# Цельсий х 1,8 + 32 = Фаренгейт /  формула