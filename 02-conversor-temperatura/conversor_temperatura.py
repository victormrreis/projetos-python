valor1 = float(input("Digite o valor do termômetro: "))
tipo = input('Como deseja converter o termômetro? "C para F"[C] ou "F para C"[F] ').strip().casefold()

def temperatura(x, tipo):
    if tipo == 'c':
        return (x * 9/5) + 32
    elif tipo == 'f':
        return (x - 32) * 5/9
    else:
        return 'Opção inválida!'
    
temp_convertida = temperatura(valor1, tipo)
if tipo == 'c':
    print(f'Sua temperatura em Fahrenheit é {temp_convertida:.2f}°F')
else:
    print(f'Sua temperatura em Celsius é {temp_convertida:.2f}°C')