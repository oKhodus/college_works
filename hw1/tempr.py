def tempr():
    celsium = input("Temperature in C = ")
    cel_float = float(celsium)
    fahr = (cel_float * 1.8) + 32
    print(f"Temperature in F = {fahr}")
tempr()