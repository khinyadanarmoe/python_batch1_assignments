from bank_account import BankAccount

alice_account = BankAccount('Alice', 3000)
bob_account = BankAccount('Bob', 2000)

alice_account.check_balance()
bob_account.check_balance()

alice_account.deposit(-200)
alice_account.deposit(200)
alice_account.check_balance()

bob_account.withdraw(3000)
bob_account.withdraw(500)
bob_account.check_balance()

alice_account.transfer(500, bob_account)
alice_account.check_balance()
bob_account.check_balance()




