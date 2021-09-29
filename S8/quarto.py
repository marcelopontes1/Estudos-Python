import os

clear = lambda: os.system('cls')
clear()

def quadrado_perfeito(num):
    raizQ = int(num ** (1/2))

    if ((raizQ ** 2) == num):
        return print(f'O número {num} é um quadrado perfeito')
    else:
        return print(f'O número {num} não é um quadrado perfeito')

num_user = int(input('Insira um número para saber se ele é um quadrado perfeito: '))

quadrado_perfeito(num_user)
