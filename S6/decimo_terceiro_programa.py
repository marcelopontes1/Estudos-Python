import os

clear = lambda: os.system('cls')
clear()

valor_n = int(input('Digite o valor de N: '))

if valor_n % 2 == 0:
    for i in range(0, valor_n + 2, 2):
        print(i)
else:
    pass
