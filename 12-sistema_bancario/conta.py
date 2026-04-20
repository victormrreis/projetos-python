class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor <= 0:
            return False
        self.saldo += valor
        return True
    
    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        return True
    
    def extrato(self):
        return f'{self.titular}, seu saldo é de R${self.saldo:.2f}'