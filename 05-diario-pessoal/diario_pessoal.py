import subprocess
from datetime import datetime

while True:
    subprocess.run(['cls' if subprocess.os.name == 'nt' else 'clear'], shell=True)
    
    print('DIÁRIO PESSOAL')
    entrada = input('\n[1] Nova entrada\n[2] Ler entradas anteriores\n[3] Apagar todas as entradas\n[4] Editar entrada\n[5] Apagar uma entrada\n[6] Sair\n')

    if entrada == '1':
        agora = datetime.now()
        with open('meu_diario.txt', 'a') as arquivo:
            diario = input('Escreva sua entrada:\n')
            if diario:
                arquivo.write(f'{agora.strftime("%d/%m/%Y às %H:%M:%S")} - {diario}\n')
            else:
                print('Entrada inválida, tente novamente.')
                input('\nPressione Enter para continuar...')
    elif entrada == '2':
        try:
            with open('meu_diario.txt', 'r') as arquivo:
                conteudo = arquivo.read()
                if not conteudo.strip():
                    print('Nenhuma entrada encontrada.')
                else:
                    print('ENTRADAS\n')
                    print(conteudo)
        except FileNotFoundError:
            print('Nenhuma entrada encontrada.')
        input('\nPressione Enter para continuar...')
    elif entrada == '6':
        print('O diário foi encerrado')
        exit()
    elif entrada == '3':
        with open('meu_diario.txt', 'w') as arquivo:
            arquivo.write('')
            print('Todas as entradas foram apagadas!')
            input('\nPressione Enter para continuar...')
    elif entrada == '4':
        try:
            with open('meu_diario.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            if not linhas:
                print('Nenhuma entrada para editar.')
            else:
                print('ENTRADAS\n')
                for i, linha in enumerate(linhas):
                    print(f'[{i + 1}] {linha.strip()}')
                try:
                    indice = int(input('Digite o número da entrada que deseja editar: ')) - 1
                    if 0 <= indice < len(linhas):
                        nova_entrada = input('Digite a nova entrada:\n')
                        if nova_entrada:
                            agora = datetime.now()
                            linhas[indice] = f'{agora.strftime("%d/%m/%Y às %H:%M:%S")} - {nova_entrada}\n'
                            with open('meu_diario.txt', 'w') as arquivo:
                                arquivo.writelines(linhas)
                            print('Entrada editada com sucesso!')
                        else:
                            print('Entrada inválida, tente novamente.')
                    else:
                        print('Número de entrada inválido, tente novamente.')
                except ValueError:
                    print('Entrada inválida, tente novamente.')
            input('\nPressione Enter para continuar...')
        except FileNotFoundError:
            print('Nenhuma entrada encontrada.')
            input('\nPressione Enter para continuar...')
    elif entrada == '5':
        try:
            with open('meu_diario.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            if not linhas:
                print('Nenhuma entrada para apagar.')
            else:
                print('ENTRADAS\n')
                for i, linha in enumerate(linhas):
                    print(f'[{i + 1}] {linha.strip()}')
                try:
                    indice = int(input('Digite o número da entrada que deseja apagar: ')) - 1
                    if 0 <= indice < len(linhas):
                        removida = linhas.pop(indice)
                        with open('meu_diario.txt', 'w') as arquivo:
                            arquivo.writelines(linhas)
                        print('Entrada apagada com sucesso!')
                    else:
                        print('Número de entrada inválido.')
                except ValueError:
                    print('Entrada inválida.')
            input('\nPressione Enter para continuar...')
        except FileNotFoundError:
            print('Nenhuma entrada encontrada.')
            input('\nPressione Enter para continuar...')
    else:
        print('Entrada inválida, tente novamente')
        input('\nPressione Enter para continuar...')