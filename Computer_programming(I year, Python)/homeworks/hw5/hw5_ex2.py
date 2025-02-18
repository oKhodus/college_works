def main():
    inp = input("Please enter url: ")

    # base_url = "https://oigus.ut.ee/et/tootaja/#"

    pos_sharp = inp.find("-")
    pos_off = inp.find("ja/")

    surname = inp[pos_sharp + 1:].capitalize()
    firstname = inp[pos_off + 3:pos_sharp].capitalize()
    fullname = firstname + " " + surname

    info = (
        f"Fullname is {fullname}\n"
        f"Firstname is {firstname}\n"
        f"Surname is {surname}\n"
    )

    print(info)


main()
