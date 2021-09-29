import os

clear = lambda: os.system('cls')
clear()

def maior_numero(a, b):
    maior = 0
    if a > b:
        return a
    return b

num_a = float(input('Insira o valor para a: '))
num_b = float(input('Insira o valor para b: '))

maior_valor = maior_numero(num_a, num_b)

print(f'O maior número entre os digitados é {maior_valor}')
