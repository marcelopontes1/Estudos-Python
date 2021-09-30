import os

clear = lambda: os.system('cls')
clear()

def soma_algarismos(num):
    if num > 0:
        soma = 0
        for i in str(num):
            soma += int(i)
        return print(f'A soma dos algarismos é {soma}')
    return print('Número inválido')

num_user = int(input('Insira um número: '))

soma_algarismos(num_user)
