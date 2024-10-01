def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    occupation = input("Enter your occupation: ")

    full_name_email = f"{first_name} {last_name} - {email}"
    frame_width = max(len(full_name_email), len(occupation) + 6)

    # padding = " " * (frame_width - len(full_name_email) - 2)

    print("+" + "-" * (frame_width + 2) + "+")
    print("|" + " " * (frame_width + 2) + "|")

    print("| " + full_name_email.center(frame_width) + " |")

    print("|" + " " * (frame_width + 2) + "|")

    print("| " + occupation.center(frame_width) + " |")

    print("|" + " " * (frame_width + 2) + "|")
    print("+" + "-" * (frame_width + 2) + "+")

main()