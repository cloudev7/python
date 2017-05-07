#!/usr/local/bin/python

from account import Account 
import admin

def main():
    print "creating new account with id 0001"
    a1 = Account("0001")
    a1.deposit(float(10000))
    a1.withdraw(float(13000))
    a1.withdraw(float(1000))
    a1.withdraw(float(5000))
    a1.withdraw(float(2000))

    a2 = Account("0002")
    a2.deposit(float(10000))
    a2.withdraw(float(3000))

    a3 = Account("0003")

    admin.listAccounts()
    admin.printAccountSummary()
    admin.printTransactions()

if __name__ == "__main__":
    main()
