from random import randint


class Account:
    def __init__(self) -> None:
        self.account = ""
        self.balance = 0

        for i in range(5):
            self.account += str(randint(0,9))
        
    def __str__(self) -> None:
        string = f"\nNúmero de cuenta: {self.account}"
        string += f"\nSaldo Actual: {self.balance}"

        return string
    
    def get_account(self) -> str:
        return self.account
    
    
    def get_balance(self):
        return self.balance

    def whitdrawal(self, amount: int) -> bool:
        if(amount < self.balance):
            self.balance -= amount
            return True
        
        return False

    def deposit(self, amount: int) -> bool:
        self.balance += amount
        return True

