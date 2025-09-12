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

    def apply_interest(self):
        self._balance += (self._balance * self.interest_rate)
        return self._balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount: float):
        self._balance += amount

    def withdraw(self, amount: float):
        if amount > self._balance:
            print("Insufficient funds")
            return
        self._balance -= amount


acc1 = BankAccount(140568, "Anna", "Smith", -7)
acc2 = BankAccount(222222, "Ben", "Lee", 2)

acc1.deposit(1000)
acc2.deposit(500)

BankAccount.interest_rate = 0.01  # 1%
acc1.apply_interest()  # 1010.0
acc2.apply_interest()  # 505.0
print(acc1.get_balance(), acc2.get_balance())