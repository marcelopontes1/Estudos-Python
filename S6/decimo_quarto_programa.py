import os

clear = lambda: os.system('cls')
clear()

valor_n = int(input('Digite o valor de N: '))

valor_n_somado = valor_n + 2

if valor_n % 2 == 0:
    while valor_n_somado > 0:
        valor_n_somado = valor_n_somado - 2
        print(valor_n_somado)
else:
    pass
