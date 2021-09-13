import os

clear = lambda: os.system('cls')
clear()

menor = 0
maior = 0
vetor = []

for i in range(10):
    vetor.append(int(input('Insira um número: ')))
    if i == 0:
        maior = menor = vetor[i]
    else:
        if vetor[i] > maior:
            maior = vetor[i]
        if vetor[i] < menor:
            menor = vetor[i]

print(vetor)
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for i, v in enumerate(vetor):
    if v == maior:
        print(f'{i}...', end='')
