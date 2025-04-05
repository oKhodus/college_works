from requests import get

def converter_currency(amount, from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = get(url)

    if response.status_code != 200:
        return "\nOioi, error to fetch data. Please try again later... (◔◡◔)\nOr maybe was invalid currency code, please check `Total available currencies` - enter command `python main.py -help`"

    if amount <= 0:
        return f"\nOioi, error amount of money is very small, please enter only a positive(+) value"

    data = response.json()
    converted_amount = data["rates"].get(to_currency)

    if converted_amount:
        base_currency = {
            "USD": "$",
            "EUR": "€",
            "GBP": "£"
        }

        label_from = base_currency.get(from_currency, from_currency)
        label_to = base_currency.get(to_currency, to_currency)

        return f"\n{amount} {label_from} = {converted_amount} {label_to}"

    else:
        return f"Invalid currency code, please check ~Total available currencies~ - enter command `python main.py -help`"

def total_currs():
    url = f"https://api.frankfurter.app/latest"
    response = get(url)

    if response.status_code != 200:
        return "Oioi, error to fetch data. Please try again later... (◔◡◔)"

    data = response.json()
    currs = " ".join(data["rates"].keys())
    return f"Total available currencies: \n{currs}"
