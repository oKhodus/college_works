from datetime import datetime

class BankAccount:
    def __init__(
        self,
        account_number: int,
        first_name: str,
        last_name: str,
        preferred_time_zone_offset: int,
    ):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.preferred_time_zone_offset = preferred_time_zone_offset
        self._balance = 0.0

    interest_rate = 0.005
    id = 0

    def apply_interest(self):
        self._balance += (self._balance * self.interest_rate)
        self.id += 1
        current_time = datetime.today().strftime('%Y%m%d%H%M%S')
        transaction_id = "{:03d}".format(self.id)
        return f"I-{self.account_number}-{current_time}-{transaction_id}"
        # return self._balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount: float):
        self._balance += amount
        self.id += 1
        current_time = datetime.today().strftime('%Y%m%d%H%M%S')
        transaction_id = "{:03d}".format(self.id)
        return f"D-{self.account_number}-{current_time}-{transaction_id}"

    def withdraw(self, amount: float):
        self.id += 1
        current_time = datetime.today().strftime('%Y%m%d%H%M%S')
        transaction_id = "{:03d}".format(self.id)

        if amount > self._balance:
            print("Insufficient funds")
            return f"X-{self.account_number}-{current_time}-{transaction_id}"
        
        self._balance -= amount
        return f"W-{self.account_number}-{current_time}-{transaction_id}"


acc1 = BankAccount(140568, "Anna", "Smith", -7)
acc2 = BankAccount(222222, "Ben", "Lee", 2)

print(acc1.deposit(1000))
print(acc1.withdraw(1100))
print(acc1.apply_interest())
print(acc1.withdraw(100))
print(acc1.get_balance())