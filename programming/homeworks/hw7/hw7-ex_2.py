def num_dm(file_inp):

    monthToDay = {1: 31, 2: 28, 3: 31, 4: 30,
                 5: 31, 6: 30, 7: 31, 8: 31, 
                 9: 30, 10: 31, 11: 30, 12: 31}
    
    with open(file_inp, "r") as file:
        
        elems = file.readlines()

        for val in elems:
            l = val.split("\n")
            l = "".join(l)
            out = l.split(".")
            index_1 = int(out[1])
            print(f"In this month will be: {monthToDay[index_1]} days")

num_dm(input("Enter name of file: "))