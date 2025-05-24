
class BankAccount:


    def __init__(self, new_balance):
        self.__balance = 0  # private variable
        self.__balance += new_balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount

ban_account_akanksha = BankAccount(1500)
ban_account_akanksha.deposit(200)
print(ban_account_akanksha.get_balance())
# ban_account_akanksha.new_balance
ban_account_akanksha.withdraw(100)
print(ban_account_akanksha.get_balance())


bank_account_atish = BankAccount(500)
print(bank_account_atish.get_balance())