import json

def task1():
    dict = {}
    while True:
        inp = input("Enter a a word (done to quit): ")

        if inp == "done":
            print(f"All records in dictionary: {dict}")
            break

        elif inp not in dict:
            new_inp = input(f"There is no info for {inp},\nWhat does it mean? ")
            dict.update({inp: new_inp})

        else:
            print(dict[inp])
    

def task2():
    try:
        with open("dict.json", "r") as file:
            content = file.read().strip()
            if content:
                dict = json.loads(content)
            else:
                dict = {}
            # the same as read .txt
    except FileNotFoundError:
        dict = {}

    while True:
        inp = input("Enter a word (done to quit): ")

        if inp == "done":
            print(f"All records in dictionary: {dict}")

            with open("dict.json", "w") as file:
                json.dump(dict, file)
                # convert into json
            break

        elif inp not in dict:
            new_inp = input(f"There is no info for {inp},\nWhat does it mean? ")
            dict[inp] = new_inp

        else:
            print(dict[inp])



def main():
    while True:
        choice = input("\nEnter a number of task (range is in [1 - 2])\
        \nor enter [stop] if you wanna stop program : ")
        tasks = {
    '1': task1, '2': task2

}
        if choice == "stop":
            print("Program was stopped///...\n")
            break
        elif choice in tasks:
            print("\n")
            tasks[choice]()
        else:
            print(f"Your input |{choice}| isn't correct, please enter a number in range [1 - 2]\n")

if __name__ == "__main__":
    main()