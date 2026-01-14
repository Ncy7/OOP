class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"The account for {self.name} has been created with a balance of Rs.{self.balance}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount Rs.{amount}. New balance is Rs.{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn amount Rs.{amount}. Remaining balance is Rs.{self.balance}")
        elif amount > self.balance:
            print("Error: Insufficient amount")
        else:
            print("Withdrawal amount must be positive.")

    def show_balance(self):
        print(f"{self.name}'s balance is Rs.{self.balance}")

    def money_transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred Rs.{amount} form {self.name} to {target_account.name}. ")
        else:
            print("Transfer amount must be positive and less than or equal to the balance.")

if __name__ == "__main__":
    acc1 = Account("Nageshwor", 1000)
    acc2 = Account("Ramesh", 2000)
    acc1.deposit(500)
    acc2.withdraw(300)

    acc1.show_balance()
    acc2.show_balance() 
    acc1.money_transfer(acc2, 400)
    