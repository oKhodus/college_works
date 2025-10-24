class CardPayment:
    def pay(self, amount):
        return f"CARD: paid {amount}"


class CashPayment:
    def pay(self, amount):
        return f"CASH: paid {amount}"


def process(payments, amounts):
    for p, a in zip(payments, amounts):
        print(p.pay(a))


payments = [CardPayment(), CashPayment(), CardPayment()]
amounts = [12.5, 7, 3]
process(payments, amounts)
