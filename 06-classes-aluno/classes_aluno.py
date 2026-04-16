class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_nota(self, valor):
        self.notas.append(valor)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def situacao(self):
        if self.calcular_media() >= 6:
            return 'Aprovado'
        else:
            return 'Reprovado'

aluno1 = Aluno('Victor')
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7)

aluno2 = Aluno('Ana')
aluno2.adicionar_nota(10)

print(f'{aluno1.nome}: {aluno1.notas} - Situação: {aluno1.situacao()}')
print(f'{aluno2.nome}: {aluno2.notas} - Situação: {aluno2.situacao()}')