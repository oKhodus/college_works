from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, balance=0.0):
        self._balance = float(balance)

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @property
    def balance(self):
        return self._balance


class SavingsAccount(Account):
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False


class CheckingAccount(Account):
    def __init__(self, balance=0.0, overdraft_limit=0.0):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self._balance - amount >= -self.overdraft_limit:
            self._balance -= amount
            return True
        return False
