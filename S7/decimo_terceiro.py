import os

clear = lambda: os.system('cls')
clear()

vetor = []
maior = 0
menor = 0

for i in range(5):
    vetor.append(int(input('Insira um número: ')))
    if i == 0:
        maior = menor = vetor[i]
    else:
        if vetor[i] > maior:
            maior = vetor[i]
        if vetor[i] < menor:
            menor = vetor[i]

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(vetor):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(vetor):
    if v == menor:
        print(f'{i}...', end='')
print()
