from account import Account


class Movement:
    def __init__(self, type, origin: Account, amount, destiny: Account = 0 ):
        self.type = type
        self.origin = origin
        self.amount = amount
        self.destiny = destiny
    
    def __str__(self) -> str:
        string = "\nInformación del movimiento"
        
        string += "\nTipo: "
        if self.type == 1:
            string += "Deposito"
        elif self.type == 2:
            string += "Retiro"
        elif self.type == 3:
            string += "Transferencia"

        if self.type == 3:
            string += "\nOrigen: "
        else:
            string += "\nCuenta: "

        string += self.origin.get_account()

        string += f"\nCantidad: {self.amount}"
        
        if self.type == 3:
            string += f"\nDestino: {self.destiny.get_account()}"
        
        return string