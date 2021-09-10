import os

clear = lambda: os.system('cls')
clear()

valor_n = int(input('Digite o valor de N: '))

print(f'Os {valor_n} primeiros números naturais em ordem crescente são: ')

for i in range(0, valor_n + 1):
    print(i)

