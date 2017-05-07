from color import Color 

accounts = []
transactions = []

def addAccount(acc):
    accounts.append(acc)

def addTransaction(tran):
    transactions.append(tran)

def printTransactions():
    print Color.BOLD + "\nAll transactions" + Color.END
    print "%-20s%-20s%-20s%-20s%s" %("Account", "Type", "Amount", "Balance", "Status")
    print "-"*90
    for tran in transactions:
        print "%-20s%-20s%-20s%-20s%s" %(tran.getAccount(), tran.getType(), tran.getAmount(), tran.getBalance(), tran.getStatus())

def listAccounts():
    print Color.BOLD + "\nAll accounts" + Color.END
    for acc in accounts:
        print acc.getAccount()

def printAccountSummary():
    print Color.BOLD + "\nAccount Summary" + Color.END
    print "%-20s|%s" %("Account", "Balance")
    print "-"*40
    for acc in accounts:
        acc.printStatement()

