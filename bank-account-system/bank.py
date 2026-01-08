class Bank:
    def __init__(self):
        self.accounts = []  # An empty list to store account objects

    def add_account(self, account):
        """Add an account object to the bank's list"""
        self.accounts.append(account)
        print(f"Added account for {account.name} to the system.")

    def show_all_accounts(self):
        """Loop through all accounts and show their details"""
        print("\n--- All Bank Accounts ---")
        for acc in self.accounts:
            # We can call methods on the objects inside the list!
            acc.show_balance()
        print("-------------------------")
        
    def calculate_total_assets(self):
        """Sum the balance of all accounts"""
        total = 0
        for acc in self.accounts:
            total += acc.balance
        print(f"Total Money in Bank: Rs.{total}")

