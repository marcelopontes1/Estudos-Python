import os

clear = lambda: os.system('cls')
clear()

qtd_mult = 0
x = 0

print('Os cinco primeiros múltiplos de 3 são:')

while qtd_mult < 5:
    x = x + 1
    if not (x % 3):
        print(x)
        qtd_mult = qtd_mult + 1
    else:
        pass
    