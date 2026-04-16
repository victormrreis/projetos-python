class Veiculo:
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 20
        print(f'Seu {self.modelo} está acelerando.\nSua velocidade atual é de {self.velocidade}Km/h')

    def frear(self):
        if self.velocidade - 10 < 0:
            self.velocidade = 0
            print(f'Seu {self.modelo} acaba de frear.')
        else:
            self.velocidade -= 10
            print(f'Seu {self.modelo} está freando.\nSua velocidade atual é de {self.velocidade}Km/h')
    
    def status(self):
        print(f'Seu {self.modelo} está a {self.velocidade}Km/h')

class Carro(Veiculo):
    def buzinar(self):
        print('Biii biii! 📢')
    
    def acelerar(self):
        print('Cinto afivelado!')
        super().acelerar()
    
class Moto(Veiculo):
    def empinar(self):
        if self.velocidade > 0:
            print('Olha o grau! 🏍️💨')
        else:
            print('Não dá pra empinar parado! 🐢')

    def frear(self):
        super().frear()
        if self.velocidade == 0:
            print('Moto estacionada')
            

carro = Carro('Toyota', 'Corolla')
carro.acelerar()
carro.acelerar()
carro.buzinar()
carro.frear()
carro.status()

moto = Moto('Honda', 'CG 160')
moto.empinar()       
moto.acelerar()
moto.empinar()       
moto.frear()
moto.frear()
moto.frear()         
moto.status()