import os

clear = lambda: os.system('cls')
clear()

vetor = []
i = 0

while i < 6:
    valor = float(input('Insira aqui um valor: '))
    i += 1
    vetor.append(valor)

print(vetor)
