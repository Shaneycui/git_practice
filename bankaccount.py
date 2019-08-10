class BankAccount(object):
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%s's account. Balance: $%.2f" % self.name % self.banlance

    def show_balance(self):
        print
        "%s's account. Balance: $%.2f" % self.name % self.banlance

    def deposit(amout):
        if amount <= 0:
            print
            "Some error message here"
            return
        else:
            print
            "The deposited amount is: %d" % amount
            self.balance += amount  # remember the space & use self.balance insteade of balance
            show_balance()

    def withdraw(amount):
        if amount >= self.balance:
            print
            "Some error message here"
            return
        else:
            print
            "The withdraw amount is: %d" % amount
            self.balance -= amount  # remember the space & use self.balance insteade of balance
            show_balance()


my_account = BankAccount("Shane")
# __repr__(my_account)
# show_balance(my_account)
my_account = deposit(2000)
my_account = withdraw(1000)
print
my_account

