import os

clear = lambda: os.system('cls')
clear()

soma = 0

for i in range(10):
    num = float(input('Digite um número: '))
    soma = soma + num

print(f'A soma de todos os números é {soma}')
