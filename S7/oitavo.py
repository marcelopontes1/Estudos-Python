import os

clear = lambda: os.system('cls')
clear()

vetor = []

for i in range(6):
    vetor.append(int(input('Insira um número: ')))

vetor.reverse()

print(vetor)
