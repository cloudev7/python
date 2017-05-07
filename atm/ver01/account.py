
from color import * 

accounts = []

class Account:

    def __init__(self, accno):
        global accounts
        self._accno = accno
        self._currency = '$ '
        self._balance = 0.0 
        accounts.append(self)

    def getAccount(self):
        return self._accno

    def getBalance(self):
        return self._currency + str(self._balance)

    def withdraw(self, wAmt):
        if wAmt > self._balance:
            print color.RED + "\nOops! sorry, requested amount is greater than available in account" + color.END
            return

        self._balance -= wAmt
        print "\nAccount: {3}\ntransaction: {0}\nAmount: {1}\nBalance: {2}".format("Withdraw", wAmt, self.getBalance(), self.getAccount())

    def deposit(self, dAmt):
        self._balance += dAmt
        print "\nAccount: {3}\ntransaction: {0}\nAmount: {1}\nBalance: {2}".format("Deposit", dAmt, self.getBalance(), self.getAccount())

    def printStatement(self):
        print "%-20s|%s" %(self._accno, self.getBalance())


def listAccounts():
    print "\nAll accounts"
    for acc in accounts:
        print acc.getAccount()

def printAccountSummary():
    print color.BOLD + "\nAccount Summary" + color.END
    print "%-20s|%s" %("Account", "Balance")
    print "-"*40
    for acc in accounts:
        acc.printStatement()
