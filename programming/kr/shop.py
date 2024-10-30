# My work of shop_oKhodus:
# I decided to use {open()} to read a lines inside of file prices.txt and to write inside of new_prices.txt
# difference is "w" and "r"
# then I write a variable {x} to return all lines in the file, as a list and variable {index} which I will use later.
# I push the loop while which {strip()} every pair of elements in lines
# and define try and except, where magic is working.
# In try I am converting str of price to float (of course if price is digit) then doing calculation -0.01
# and write to a new_file. And if product was coverted it will be output: {prdct} OK!
# but if it can't be converted I raise ValueError and print: Could not to covert the price of '{prdct}'.
#  And that's all :)




def shop_oKhodus():
    with open("prices.txt", "r") as file, open("new_prices.txt", "w") as new_file:
        x = file.readlines()
        
        index = 0
        while index < len(x):
            prdct = x[index].strip()
            price_str = x[index+1].strip()
            index += 2 
            # increase index to +2, to go to the next pair
            try:
                price = float(price_str)
                nwprice = price - 0.01
                new_file.write(f"{prdct}\n{nwprice}")
                print(f"{prdct} OK!")
            except ValueError:
                print(f"Could not to covert the price of '{prdct}'.")
                # There is maybe a mistake in technical task is "covert" but I sure it should be "convert"

shop_oKhodus()


