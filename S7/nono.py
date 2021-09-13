import os

clear = lambda: os.system('cls')
clear()

vetor = []

qtd_pares = 0

while qtd_pares < 6:
    num = int(input('Insira um número: '))
    if num % 2 == 0:
        vetor.append(num)
        qtd_pares += 1
    else:
        pass

print(vetor)
