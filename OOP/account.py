import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        return utc_time

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = []
        print("Account created for " + name)
        self._transaction_list.append((Account._current_time(), balance))

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_list.append((Account._current_time(), amount))
        self.show_balance()

    def withdraw(self, amount):
        if self._balance >= amount > 0:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Invalid Transaction.")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print("{:6} {} on {} (local time {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    shivam = Account("Shivam", 0)

    shivam.deposit(1000)
    shivam.withdraw(500)
    shivam.deposit(3000)
    shivam.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    # steph._balance = 200  # This caused the balance to differ from transaction.
    # steph.__balance = 200  # 2 underscores at start of attribute name mangles it. Balance will not differ from trans.
    steph.show_balance()
    steph.show_transactions()

