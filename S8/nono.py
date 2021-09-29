import os

clear = lambda: os.system('cls')
clear()

def volume_cilindro(altura, raio):
    volume = 3.141592 * (raio ** 2) * altura
    return volume

altura_user = float(input('Insira o valor da altura: '))
raio_user = float(float('Insira o valor do raio: '))

volume_total = volume_cilindro(altura_user, raio_user)

print(f'O volume total do cilindro é de {volume_total}')
