import os

clear = lambda: os.system('cls')
clear()

soma = 0

for i in range(10):
    num = int(input('Digite um número: '))
    soma = soma + num

media = soma / 10

print(f'A média dos números é {media}')
