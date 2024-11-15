import numpy as np

def bublik():
    name_list = [5, 2, 1, 4, 3]
    for i in range(len(name_list)):
        for j in range(i+1):
            if name_list[j] > name_list[i]:
                temp = name_list[i]
                name_list[i] = name_list[j]
                name_list[j] = temp
    print(name_list, "\n")


def matrix():
    row = 0
    
    m = [[5, 6, 7], [8, 9, 10]]

    for line in m:
        print(f"row {row}:", *line)
        row +=1

    print("\n")

    col = 0
    t = np.transpose(m)

    for line in t:
        print(f"col {col}:", *line)
        col +=1


def dimension_mt():
    m = [[1, 2], [3, 4]]
    empty = []
    empty2= []
    total = []
    row = 0
    m2 = [[5, 6, 7], [8, 9, 10]]

    # calc_1 = m[0][0] * m2[0][0] + m[0][1] * m2[1][0]
    # calc_2 = m[1][0] * m2[0][0] + m[1][1] * m2[1][0]
    
    # calc_3 = m[0][0] * m2[0][1] + m[0][1] * m2[1][1]
    # calc_4 = m[1][0] * m2[0][1] + m[1][1] * m2[1][1]
    
    # calc_5 = m[0][0] * m2[0][2] + m[0][1] * m2[1][2]
    # calc_6 = m[1][0] * m2[0][2] + m[1][1] * m2[1][2]
    
    # empty.extend([calc_1, calc_2, calc_3,])
    # total.append(empty)

    # empty2.extend([calc_4, calc_5, calc_6])
    # total.append(empty2)

    if len(m[0]) != len(m2):
        raise ValueError("It's impossible")
    
    total = np.matmul(m, m2)
    for line in total:
        print(f"row {row}:", *line)
        row +=1
    


def main():
    while True:
        choice = input("\nEnter a number of task (range is in [1 - 3])\
        \nor enter [stop] if you wanna stop program : ")
        tasks = {
    '1': bublik, '2': matrix, '3': dimension_mt

}
        if choice == "stop":
            print("Program was stopped///...\n")
            break
        elif choice in tasks:
            print("\n")
            tasks[choice]()
        else:
            print(f"Your input |{choice}| isn't correct, please enter a number in range [1 - 3]\n")

if __name__ == "__main__":
    main()