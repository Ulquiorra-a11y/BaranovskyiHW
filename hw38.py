class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
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
account.deposit(-5)
account.show_balance()
account.withdraw(500)
account.show_balance()
account.withdraw(100)
account.show_balance()

print("Operation history:")
for record in account.history:
    print(f"\t{record}")
