import os

clear = lambda: os.system('cls')
clear()

valor_n = int(input('Digite o valor de N: '))

valor_n_somado = valor_n + 1

print(f'Os {valor_n} primeiros números naturais em ordem decrescente são: ')

while valor_n_somado > 0:
    valor_n_somado = valor_n_somado - 1
    print(valor_n_somado)
