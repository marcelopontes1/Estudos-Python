import os

clear = lambda: os.system('cls')
clear()

valor_n = int(input('Digite o valor de N: '))

soma = 0

for i in range(0, valor_n + 1):
    print(i)
    soma = soma + i

print(f'O valor da soma é {soma}')
