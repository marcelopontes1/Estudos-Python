import os

clear = lambda: os.system('cls')
clear()

soma = 0
qtd_positivos = 0

while qtd_positivos < 10:
    num = float(input('Digite um número: '))
    if num >= 0:
        soma = soma + num
        qtd_positivos = qtd_positivos + 1
    else:
        pass

media = soma / 10

print(f'A média dos números é {media}')
