import os

clear = lambda: os.system('cls')
clear()

vetor = []
soma = 0

for i in range(15):
    nota = int(input('Insira a nota: '))
    vetor.append(nota)
    soma = soma + nota

media = soma / 15

print(media)
