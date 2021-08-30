import os

clear = lambda: os.system('cls')
clear()

valor_n = int(input('Digite o valor de N: '))

if valor_n % 2 != 0:
    for i in range(valor_n + 1):
        if i != 0:
            print(i)
        elif i == 0:
            pass
else:
    pass
