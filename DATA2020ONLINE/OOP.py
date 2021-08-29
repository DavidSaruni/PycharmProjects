
# A bank object

class Account:

    def __init__(self):
        self.name = 'David Badshah'
        self.branch = 'Waiyiaki way'
        self.age = 10
        self.accno = 10000000050
        self.balance = 50
        # we define the attributes of states of your account


    # Behaviour deposit, withdraw, buyairtime, checkbalance, takeloan
    def deposit(self, amount):
        print('Welcome ', self.name)
        print('Your Current balance is ', self.balance)
        self.balance = self.balance + amount
        print('You deposited ', amount)
        print('Your New balance is ', self.balance)
        print('Thank you')

    def withdraw(self, amount):
        print('Welcome ', self.name)
        print('Your current balance is ', self.balance)
        if amount > self.balance:
            print('You cannot withdraw more than your balance')
        elif amount <= 0:
            print('You cannot withdraw a zero')
        else:
            print('Your Withdrawal of ', amount, 'was successful')
            self.balance = self.balance - amount
            print('Your New Balance is ', self.balance)
            print('Thank You')

    def CheckBalance(self):
        print('Your current Balance is Kshs.', self.balance )

object = Account()
object.deposit(2000)
object.deposit(2000)
object.withdraw(8000)
object.withdraw(0)
object.withdraw(800)
object.CheckBalance()

