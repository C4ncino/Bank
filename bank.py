from account import Account

class Bank:
    def __init__(self) -> None:
        self.accounts = {}
        self.movements = []

    
    def search_account(self, account) -> bool:
        try:
            self.accounts[account]
            
        except Exception:
            return False

        return True
    
    def get_account(self, account) -> Account:
        return self.accounts[account]

    def add_account(self) -> Account:
        account = Account()
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