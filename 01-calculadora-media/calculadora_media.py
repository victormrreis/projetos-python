nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

def media(x, y, z):
    return((x + y + z) / 3)

media_geral = media(nota1, nota2, nota3)

print(f'Sua média é {media_geral:.2f}')

def situacao(media):
    if media >= 7:
        return('Aprovado')
    else:
        return('Reprovado')

print(f'Situação: {situacao(media_geral)}')