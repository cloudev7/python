import admin
from color import Color 
from transaction import Transaction

class Account:

    def __init__(self, accno):
        self._accno = accno
        self._currency = '$ '
        self._balance = 0.0 
        admin.addAccount(self)

    def getAccount(self):
        return self._accno

    def getBalance(self):
        return self._currency + str(self._balance)

    def withdraw(self, wAmt):
        status = "Declined"
        tran = Transaction(self._accno, "W", wAmt, self._balance)

        if wAmt > self._balance:
            print Color.RED + "\nOops! sorry, requested amount is greater than available in account" + Color.END
        else:
            status = "Approved"
            self._balance -= wAmt

        tran.setStatus(status)
        admin.addTransaction(tran)

        print "\n%-20s: %s" %("Account", self.getAccount())
        print "%-20s: %s" %("Tran.Type", "W")
        print "%-20s: %s" %("Amount", wAmt)
        print "%-20s: %s" %("Balance", self.getBalance())

    def deposit(self, dAmt):
        status = "Approved"
        tran = Transaction(self._accno, "D", dAmt, self._balance)
        tran.setStatus(status)
        admin.addTransaction(tran)
        self._balance += dAmt

        print "\n%-20s: %s" %("Account", self.getAccount())
        print "%-20s: %s" %("Tran.Type", "D")
        print "%-20s: %s" %("Amount", dAmt)
        print "%-20s: %s" %("Balance", self.getBalance())

    def printStatement(self):
        print "%-20s|%s" %(self._accno, self.getBalance())

