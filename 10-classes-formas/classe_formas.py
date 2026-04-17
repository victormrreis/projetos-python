class Forma:
    def area(self):
        pass
    
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado
    
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14159 * self.raio ** 2

formas = [Quadrado(5), Retangulo(4, 8), Circulo(3)]
for forma in formas:
    print(f'Área: {forma.area():.2f}')
