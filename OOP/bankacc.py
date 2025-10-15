from datetime import *
from dataclasses import dataclass


class BankAccount:
    interest_rate = 0.005
    _transaction_counter = 0

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

    def _next_transaction_id(self) -> str:
        BankAccount._transaction_counter += 1
        return "{:03d}".format(BankAccount._transaction_counter)

    def _make_code(self, type_code: str) -> str:
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        transaction_id = self._next_transaction_id()
        return f"{type_code}-{self.account_number}-{timestamp}-{transaction_id}"

    def apply_interest(self) -> str:
        self._balance += self._balance * self.interest_rate
        return self._make_code("I")

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> str:
        self._balance += amount
        return self._make_code("D")

    def withdraw(self, amount: float) -> str:
        if amount > self._balance:
            print("Insufficient funds")
            return self._make_code("X")
        self._balance -= amount
        return self._make_code("W")

    @staticmethod
    def parse_confirmation(confirmation_code, timezone_offset):
        code_arr = confirmation_code.split("-")
        type_code, account_num, timestamp, trans_id = code_arr

        utc_dt = datetime.strptime(timestamp, "%Y%m%d%H%M%S")

        local_dt = utc_dt + timedelta(hours=timezone_offset)

        @dataclass
        class ParsedConfirmation:
            transaction_code: str
            account_number: int
            transaction_id: int
            time_utc: str
            time: str

        return ParsedConfirmation(
            transaction_code=type_code,
            account_number=int(account_num),
            transaction_id=int(trans_id),
            time_utc=utc_dt.strftime("%Y-%m-%dT%H:%M:%S"),
            time=local_dt.strftime("%Y-%m-%d %H:%M:%S"),
        )
