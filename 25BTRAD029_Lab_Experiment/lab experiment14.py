class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


account = BankAccount("Rahul", 5000)

account.display()
account.deposit(2000)
account.withdraw(1000)
account.display()
