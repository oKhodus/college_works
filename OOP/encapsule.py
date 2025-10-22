class AccountProfile:
    def __init__(self, first_name, last_name, timezone_offset):
        self.first_name = first_name
        self.last_name = last_name
        self._balance = 0
        self.timezone_offset = timezone_offset

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def balance(self):
        return float(self._balance)

    def deposit(self, amount):
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Deposit must be a number")
        if amt <= 0:
            raise ValueError("Deposit must be > 0")
        self._balance += amt
        return True

    def withdraw(self, amount):
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Withdraw must be a number")
        if amt <= 0:
            raise ValueError("Withdraw must be > 0")
        if self._balance - amt < 0:
            return False
        self._balance -= amt
        return True


    @property
    def timezone_offset(self):
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, value):
        if isinstance(value, int) and value in range(-12, 15):
            self._timezone_offset = value
        else:
            raise ValueError("Invalid timezone offset")