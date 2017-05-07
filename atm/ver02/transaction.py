class Transaction:

    def __init__(self, accno, ttype, amount, balance):
        self._accno = accno
        self._ttype = ttype
        self._amount = amount
        self._balance = balance

    def getAccount(self):
        return self._accno

    def getType(self):
        return self._ttype

    def getAmount(self):
        return self._amount

    def getBalance(self):
        return self._balance

    def setStatus(self, status):
        self._status = status

    def getStatus(self):
        return self._status
