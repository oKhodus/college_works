def num_lines(file_inp):
    count = 0
    try:
        if file_inp == "names.txt":
            
            with open(file_inp, "r") as file:
                lines = file.readlines()

                for line in lines:

                    l = line.split("\n")
                    x = "".join(l)
                    count += 1
                    print(f"{count}. {x}")
        else:
            print(f"Your input |{file_inp}| isn't correct,")
            num_lines(input("please enter name of file, again: "))
    except ValueError:
        pass

num_lines(input("Enter name of file: "))

# name of file should be |names.txt|