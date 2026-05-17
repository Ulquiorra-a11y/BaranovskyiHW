class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Not enough funds.")

        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

    @property
    def history(self):
        return list(self.__history)

account = BankAccount("Oleksandr", 0)

account.deposit(150)
account.show_balance()
try:
    account.deposit(-5)
except ValueError as e:
    print(f"Error: {e}")
account.show_balance()
try:
    account.withdraw(500)
except ValueError as e:
    print(f"Error: {e}")
account.show_balance()
try:
    account.withdraw(100)
except ValueError as e:
    print(f"Error: {e}")
account.show_balance()

print("Operation history:")
for record in account.history:
    print(f"\t{record}")
