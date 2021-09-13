import os

clear = lambda: os.system('cls')
clear()

menor = 0
maior = 0
vetor = []

for i in range(5):
    vetor.append(float(input('Insira um número: ')))
    if i == 0:
        maior = menor = vetor[i]
    else:
        if vetor[i] > maior:
            maior = vetor[i]
        if vetor[i] < menor:
            menor = vetor[i]

soma = sum(vetor)
media = soma / len(vetor)

print(vetor)
print(f'A média é {media}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
