import os

clear = lambda: os.system('cls')
clear()

soma = 0
media = 0
num_elementos = 0

while True:
    nota = float(input('Digite aqui sua nota: '))
    if nota >= 10 and nota <= 20:
        soma = soma + nota
        num_elementos = num_elementos + 1
    else:
        break

if soma == 0:
    print('Não foram inseridos dados suficientes')
else:
    media = soma / num_elementos
    print(f'A média é igual a {media}')
