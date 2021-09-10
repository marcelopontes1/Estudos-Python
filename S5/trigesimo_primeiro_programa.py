import os

clear = lambda: os.system('cls')
clear()

altura = int(input('Insira aqui sua altura (cm): '))
peso = int(input('Peso (kg): '))

if altura < 120:
    if peso <= 60:
        print('Você está na categoria A')
    elif peso > 60 and peso <= 90:
        print('Você está na categoria D')
    else:
        print('Você está na categoria G')

elif altura >= 120 and altura <= 170:
    if peso <= 60:
        print('Você está na categoria B')
    elif peso > 60 and peso <= 90:
        print('Você está na categoria E')
    else:
        print('Você está na categoria H')

else:
    if peso <= 60:
        print('Você está na categoria C')
    elif peso > 60 and peso <= 90:
        print('Você está na categoria F')
    else:
        print('Você está na categoria I')
