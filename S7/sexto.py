import os

clear = lambda: os.system('cls')
clear()

vetor = []
maior = 0
menor = 0

for i in range(10):
    vetor.append(float(input('Insira um valor: ')))
    if i == 0:
        maior = menor = vetor[i]
    else:
        if vetor[i] > maior:
            maior = vetor[i]
        if vetor[i] < menor:
            menor = vetor[i]

print(maior)
print(menor)
