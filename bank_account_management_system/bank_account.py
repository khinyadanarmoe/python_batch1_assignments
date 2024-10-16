class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited: ${self.balance}. New balance: ${self.balance}')
        else:
            print(f'Negative amount ${amount} cannot be deposited')
            

    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            print(f'Withdrew: ${amount}. New balance: ${self.balance}.')

        else:
            print(f'${amount} cannot be withdrawn from your account.')

    def check_balance(self):
        print(f'Account balance: ${self.balance}')

    def transfer(self, amount, other_account):
        if amount > 0 and amount < self.balance:
            self.withdraw(amount)
            other_account.deposit(amount)
            print(f'Transferred ${amount} to {other_account.account_holder}.')

        else:
            print('Process failed. Invalid amount.')