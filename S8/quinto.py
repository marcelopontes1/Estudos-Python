import os

clear = lambda: os.system('cls')
clear()

def volume_esfera(raio):
    volume = (4/3) * 3.1415 * (raio ** 3)
    return volume

valor_raio = float(input('Insira o valor do raio da esfera: '))

vol_total = volume_esfera(valor_raio)

print(f'O volume da esfera de raio {valor_raio} é {vol_total}')
