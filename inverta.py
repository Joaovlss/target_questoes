texto = input('Digite uma palavra ou frase para reverter: ')


def inverter():
    return texto[::-1]

print(f'Texto invertido:  {inverter()}')