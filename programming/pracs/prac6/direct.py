def main():
    with open("text.txt", "r") as text:
        total_count = 0
        line_number = 1
        for line in text:
            line = line.strip()
            if line.isdigit():
                num = int(line)
                stars = "*" * num
                total_count += num
                print(f"{line_number}.{stars}")
            else:
                print(f"{line_number}.")
            line_number += 1

    
    print(f"Counted: {total_count}")


main()