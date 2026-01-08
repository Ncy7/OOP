from bank import Bank
from account import Account
from savings import SavingsAccount
from current import CurrentAccount


if __name__ == "__main__":
    print("Welcome to the Bank Account System")
    print("----------------------------------")

    my_bank = Bank()

    john_acc = SavingsAccount("John Doe", 1500, 4)
    jane_acc = CurrentAccount("Jane Smith", 500, 300)

    my_bank.add_account(john_acc)
    my_bank.add_account(jane_acc)

    print("\n---- Transactions ----")
    
    john_acc.deposit(200)
    jane_acc.withdraw(300)

    john_acc.apply_interest()

    my_bank.show_all_accounts()
    my_bank.calculate_total_assets()

    print("\nThank you for using the Bank Account System!")
    

