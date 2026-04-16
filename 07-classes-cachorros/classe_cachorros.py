class Cachorro:
    def __init__(self, nome, raca, idade=0, fome=0):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.fome = fome

    def latir(self):
        print(f'Au au! Eu sou o {self.nome}!')

    def aniversario(self):
        self.idade += 1
        print(f'{self.nome} fez aniversário! Agora tem {self.idade} anos!')

    def comer(self):
        if self.fome >= 3:
            self.fome -= 3
        else:
            self.fome = 0
    
        if self.fome == 0:
            print(f'{self.nome} está satisfeito!')
        else:
            print(f'{self.nome} comeu. Nível de fome: {self.fome}')

    def brincar(self):
        if self.fome + 2 > 10:
            self.fome = 10
        else:
            self.fome += 2

        if self.fome == 10:
            print(f'{self.nome} está esgotado! Seu nível de fome é {self.fome}.')
        else:
            print(f'{self.nome} brincou. Nível de fome: {self.fome}')

    def status(self):
        print(f'{self.nome} está com o nível de fome {self.fome}/10')

class Dono:
    def __init__(self, nome):
        self.nome = nome
        self.cachorros = []

    def adotar(self, cachorro):
        self.cachorros.append(cachorro)
        print(f'{self.nome} adotou o {cachorro.nome}')
    
    def listar_cachorros(self):
        for cachorro in self.cachorros:
            print(cachorro.nome)

    def alimentar_todos(self):
        for cachorro in self.cachorros:
            cachorro.comer()

    def passear(self):
        for cachorro in self.cachorros:
            cachorro.brincar()

victor = Dono('Victor')
duke = Cachorro('Duke', 'Labrador', 5, 8)
bela = Cachorro('Bela', 'Poodle', 3, 6)

victor.adotar(duke)
victor.adotar(bela)
victor.listar_cachorros()
victor.alimentar_todos()
victor.passear()

