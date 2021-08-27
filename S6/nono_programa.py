import os

clear = lambda: os.system('cls')
clear()

qtd = 0
x = 0

valor_n = int(input('Digite o valor de N: '))

print(f'Os {valor_n} primeiros números naturais ímpares são: ')

while qtd < valor_n:
    x = x + 1
    if (x % 2) == 0:
        pass
    else:
        print(x)
        qtd = qtd + 1
