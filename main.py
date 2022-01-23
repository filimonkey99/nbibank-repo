import customer
import account
import bank

a = account.Account(1111)
print(a.get_account_info())
print(a.deposit(1000))
print(a.withdraw(500))