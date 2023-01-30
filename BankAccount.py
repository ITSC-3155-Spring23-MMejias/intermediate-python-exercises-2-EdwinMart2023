class BankAccount:
    # create the constructor to initialize instance variable
    def __init__(self,account_name,starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    # the method for depositing amount
    def deposit(self,amount):
        # addingt into balance
        self.balance = self.balance+amount

    # the method to withdraw amount
    def  withdraw(self,amount):
        #  withdraw amount from account if balance is greater than or equal to amount
        if self.balance >= amount:
        # subtracting amount from balance
            self.balance = self.balance-amount
        # if not enough display the message
        else:
            print("not enough in the account to withdraw")

    # the getter methods to return balance
    def get_balance(self):
        return str(self.account_name)+" has a balance of $"+str(self.balance)
