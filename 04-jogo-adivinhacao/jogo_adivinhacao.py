import random

print('Jogo de Adivinhação')

numero = random.randint(1, 20)
tentativas = 3
acertou = False
minimo = 1
maximo = 20

while tentativas > 0:
    try:
        palpite = int(input(f'Diga um número entre {minimo} e {maximo}: '))

        if palpite < minimo or palpite > maximo:
            print(f'Número inválido! Escolha entre {minimo} e {maximo}.')
            continue

        if palpite == numero:
            print(f'Parabéns! O número era "{numero}"')
            acertou = True
            break

        tentativas -= 1

        if palpite > numero:
            print('Tente um número menor!')
            maximo = palpite - 1
        else:
            print('Tente um número maior!')
            minimo = palpite + 1

        print(f'Agora o número está entre {minimo} e {maximo}')
        
        if minimo == maximo:
            print(f'Agora não tem mais dúvida… é {minimo}.')
            print(f'Parabéns! O número era "{numero}"')
            acertou = True
            break

        if tentativas == 1:
            print('Última tentativa, boa sorte!')
        else:
            print(f'Você ainda tem {tentativas} tentativa(s)')

    except ValueError:
        print('Erro: Digite um número válido!')

if not acertou:
    print(f'Game Over! O número era "{numero}"')