import os
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    status = input('Deseja iniciar o carrinho de compras? [S/N] ').strip().casefold()
    if status == 's':
        break
    elif status == 'n':
        print('Até mais!')
        exit()
    
lista = []

produtos = {
    'a': {'nome': 'Arroz 5kg', 'preco': 22.90},
    'b': {'nome': 'Feijão 1kg', 'preco': 8.50},
    'c': {'nome': 'Macarrão 500g', 'preco': 4.99},
    'd': {'nome': 'Leite 1L', 'preco': 6.30},
    'e': {'nome': 'Café 500g', 'preco': 15.70},
    'f': {'nome': 'Açúcar 1kg', 'preco': 5.40},
    'g': {'nome': 'Óleo 900ml', 'preco': 7.89},
    'h': {'nome': 'Sal 1kg', 'preco': 3.20},
    'i': {'nome': 'Farinha de trigo 1kg', 'preco': 6.10},
    'j': {'nome': 'Manteiga 200g', 'preco': 9.99},
}
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Carrinho de compras')
    status = input(' [1] Ver itens no carrinho\n [2] Adicionar itens ao carrinho\n [3] Desistir da compra\n [4] Remover item do carrinho\n').strip().casefold()
    if status == '1' and not lista:
        print('Seu carrinho está vazio')
        input('\nPressione Enter para continuar...')
    elif status == '1' and lista:
        print('Itens no carrinho:')
        for item in lista:
            print(f'  - {item["nome"]} | R${item["preco"]:.2f}')
        print('Total: R${:.2f}'.format(sum(item['preco'] for item in lista)))
        input('\nPressione Enter para continuar...')
    elif status == '2':
        while True:
            print('\nProdutos disponíveis:')
            print('  [A] Arroz 5kg - R$22,90')
            print('  [B] Feijão 1kg - R$8,50')
            print('  [C] Macarrão 500g - R$4,99')
            print('  [D] Leite 1L - R$6,30')
            print('  [E] Café 500g - R$15,70')
            print('  [F] Açúcar 1kg - R$5,40')
            print('  [G] Óleo 900ml - R$7,89')
            print('  [H] Sal 1kg - R$3,20')
            print('  [I] Farinha de trigo 1kg - R$6,10')
            print('  [J] Manteiga 200g - R$9,99\n')
            print('  [S] Sair do catálogo')
            escolha = input('\n Escolha um produto: ').strip().casefold()
            if escolha in produtos:
                item = produtos[escolha]
                lista.append(item)
                print(f'{item["nome"]} adicionado! (R${item["preco"]:.2f})')
            elif escolha == 's':
                break
            else:
                print('Produto não encontrado!')
    elif status == '3':
        print('Volte sempre!')
        exit()
    elif status == '4':
        if not lista:
            print('Seu carrinho está vazio')
        else:
            print('Itens no carrinho:')
            for item in lista:
                print(f'  - {item["nome"]}')
            item_remover = input('Digite o nome do item que deseja remover: ').strip().casefold()
            encontrado = False
            for item in lista:
                if item['nome'].casefold() == item_remover:
                    lista.remove(item)
                    print(f'{item["nome"]} removido!')
                    encontrado = True
                    break
            if not encontrado:
                print('Item não encontrado no carrinho.')
        input('\nPressione Enter para continuar...')
    else:
        print('Opção inválida, tente novamente.')
        input('\nPressione Enter para continuar...')