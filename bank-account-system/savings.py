from account import Account

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
        print(f"Savings account created for {self.name} with interest rate of {self.interest_rate}%.")

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Applied interest of Rs.{interest}. New balance is Rs.{self.balance}")


if __name__ == "__main__":
    # Create savings account with 5% interest
    saver = SavingsAccount("Alice", 1000, 5) 
    
    saver.deposit(500)       # Works (Inherited)
    saver.apply_interest()   # Works (New feature)
    saver.withdraw(200)      # Works (Inherited)