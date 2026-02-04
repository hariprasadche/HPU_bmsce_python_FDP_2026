class Bankacc:
    def __init__(self, name, balance, pin):
        self.name = name
        self._balance = balance   #protected
        self.__pin = pin #private

    def show_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Balance is balance is {self._balance}")
        #print(f"pin": {self.__pin}"")

acct = Bankacc("", 20000, 1234)
acct.show_balance()

