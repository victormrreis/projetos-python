class Pagamento:
    def processar(self):
        pass

class Pix(Pagamento):
    def __init__(self, valor):
        self.valor = valor
    
    def processar(self):
        return (f'Pix de R${self.valor:.2f} enviado instantaneamente!')
    
class Cartao(Pagamento):
    def __init__(self, valor, parcelas):
        self.valor = valor
        self.parcelas = parcelas

    def processar(self):
        return (f'R${self.valor:.2f} parcelado em {self.parcelas} vezes de R${self.valor / self.parcelas:.2f}')

class Boleto(Pagamento):
    def __init__(self, valor):
        self.valor = valor

    def processar(self):
        return (f'Boleto de R${self.valor:.2f} gerado. Vencimento em 3 dias.')
    
pagamentos = [Pix(50), Cartao(900, 3), Boleto(200)]
for pagamento in pagamentos:
    print(pagamento.processar())
