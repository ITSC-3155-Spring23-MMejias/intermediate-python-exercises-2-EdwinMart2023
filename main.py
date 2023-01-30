from BankAccount import BankAccount
if __name__ == "__main__":
    # create the instance of BankAccount class
    account = BankAccount("Eddy",2000)
    # call the deposit() function
    account.deposit(575)
    # call the withdraw() function
    account.withdraw(800)
    # call get_balance() function
    # display the result
    print(account.get_balance())
