class Funcionario:
    def __init__(self, nome, salario=0):
        self.nome = nome
        self.salario = salario

    def apresentar(self):
        print(f'Meu nome é {self.nome} e ganho R${self.salario:.2f}')

    def aumento(self, percentual):
        self.salario += self.salario * (percentual / 100)
        print(f'{self.nome} teve um aumento de {percentual}% no salário. Agora seu salário é de R${self.salario:.2f}')

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.equipe = []
    
    def adicionar_funcionario(self, funcionario):
        self.equipe.append(funcionario)

    def listar_equipe(self):
        for funcionario in self.equipe:
            print(funcionario.nome)
    
    def apresentar(self):
        super().apresentar()
        print(f'Sou gerente de {len(self.equipe)} pessoas')
    
func1 = Funcionario('Ana', 3000)
func2 = Funcionario('Bruno', 2500)

gerente = Gerente('Victor', 5000)
gerente.adicionar_funcionario(func1)
gerente.adicionar_funcionario(func2)
gerente.apresentar()
gerente.listar_equipe()
gerente.aumento(10)
gerente.apresentar()
