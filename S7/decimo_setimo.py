import os

clear = lambda: os.system('cls')
clear()

vetor = []

for i in range(10):
    num = int(input('Insira um número: '))
    if num < 0:
        vetor.append(0)
    else:
        vetor.append(num)

print(vetor)
