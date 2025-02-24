class BankAccount:
    def __init__(self, owner_name, balance: float = 0.0):
        """Initializing the owner_name and balance

        Args:
            owner_name (str): Account owner name for example - (Vasya Pupkin)
            balance (float): Initial balance, default is: 0.0
        """
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, value: float):
        """Function which deposit (add) value of money to balance

        Args:
            value (float): Value of money which you want to deposit for example - 100.0 ($)
        """
        if value > 0:
            self.balance += value
            print(f"You've deposited $ {value:,} \nNew balance: $ {self.balance:,}\n")
        else:
            print(f"You've tried to deposit: $ {value:,}\n  *Incorrect value of deposit, be sure it's not a negative\n")

    def withdraw(self, value: float):
        """Function which withdraw (takes away) value of money from balance

        Args:
            value (float): Value of money which you want to withdraw for example - 100.0 ($)
        """
        if value <= self.balance:
            self.balance -= value
            print(f"You've withdrawed $ {value:,} \nNew balance: $ {self.balance:,}\n")
        else:
            print(f"You've tried to withdraw: $ {value:,}\nBut you don't have enough funds to withdraw\n")

    def get_balance(self) -> float:
        """Returns the current account balance

        Returns:
            float: The current balance
        """

        print(f"\nCurrent balance of {self.owner_name}: $ {self.balance:,}\n")
        return self.balance


customer1 = BankAccount("Oleksii Khodus", 100)

customer1.get_balance()

customer1.withdraw(10**8)
customer1.deposit(10**8)

customer1.withdraw(10)


customer1.deposit(-1)
customer1.deposit(1)
