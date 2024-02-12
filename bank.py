from random import randint
from account import Account
from database import DB

class Bank:
    def __init__(self) -> None:
        self.accounts = {}

        self.db = DB()
        db_accounts = self.db.get_accounts()

        for account in db_accounts:
            self.accounts[account[0]] = Account(account[0], account[1], self.db)

    
    def search_account(self, account) -> bool:
        try:
            self.accounts[account]
            
        except Exception:
            return False

        return True
    
    def get_account(self, account) -> Account:
        return self.accounts[account]
    
    def get_accounts(self):
        return self.accounts

    def add_account(self) -> Account:
        accountN = ""
        for i in range(5):
            accountN += str(randint(0,9))

        account = Account(accountN, 0, self.db)
        self.db.add_account(accountN)

        self.accounts[account.get_account()] = account

        return account
    
    def transfer(self, origin: str, destiny: str, amount) -> bool:
        if self.search_account(origin) and self.search_account(destiny):
            acc_origin = self.get_account(origin)
            acc_destiny = self.get_account(destiny)

            if acc_origin.whitdrawal(amount):
                acc_destiny.deposit(amount)
            else:
                return False

            return True
        
        return False