from account import Account

class CurrentAccount(Account):
    def __init__(self, name, balance, overdrawth_limit):
        super().__init__(name, balance)
        self.overdrawth_limit = overdrawth_limit
        print(f"Current account created for {self.name} with overdraft limit of Rs.{self.overdrawth_limit}.")   

    def withdraw(self, amount):
        total_funds = self.balance + self.overdrawth_limit
        if 0 < amount <= total_funds:
            self.balance -= amount
            print(f"Withdrawn amount Rs.{amount}. Remaining balance is Rs.{self.balance}")
        elif amount > total_funds:
            print("Error: Insufficient amount including overdraft limit")
        else:
            print("Withdrawal amount must be positive.")

if __name__ == "__main__":
    # Create account with $100 balance and $500 overdraft limit
    current = CurrentAccount("Bob", 100, 500)
    
    current.withdraw(300)   # Should work! Balance becomes -$200
    current.withdraw(800)   # Should fail (Too much)