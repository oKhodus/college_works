def find_name(url):
    f = url.strip().split("/")
    fullname = f[-1]
    return fullname

def exported(file_inp):
    with open(file_inp, "r") as file:
        urls = file.readlines()
    for url in urls:
        surname = find_name(url)
        pos = surname.find("-")
        print(surname[pos+1:])

exported("urls.txt")

#  https://oigus.ut.ee/et/tootaja/