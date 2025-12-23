class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    acc = Account()
    acc.deposit(100)
    acc.withdraw(50)
    print(f"Balance: {acc.balance}")


if __name__ == "__main__":
    main()