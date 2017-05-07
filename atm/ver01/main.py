#!/usr/local/bin/python

from account import *

def main():
    print "creating new account with id 0001"
    a1 = Account("0001")
    a2 = Account("0002")
    a3 = Account("0003")

    listAccounts()

    a1.deposit(float(10000))
    a1.withdraw(float(13000))

    printAccountSummary()

if __name__ == "__main__":
    main()
