from database import DB


class Account:
    def __init__(self, account: str, balance: float, db: DB) -> None:
        self.account = account
        self.balance = balance
        self.db = db
        
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

            self.db.update_balance(self.account, self.balance)

            return True
        
        return False

    def deposit(self, amount: int) -> bool:
        self.balance += amount
        
        self.db.update_balance(self.account, self.balance)
        
        return True

