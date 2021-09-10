import os

clear = lambda: os.system('cls')
clear()

qtd_mult = 0
x = 0
soma = 0

while qtd_mult < 50:
    x = x + 1
    if x % 2 == 0:
        soma = soma + x
        qtd_mult = qtd_mult + 1
    else:
        pass

print(f'A soma dos 50 primeiros números pares é {soma}')