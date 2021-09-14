import os

clear = lambda: os.system('cls')
clear()

vetor = []

for i in range(20):
    vetor.append(int(input('Insira um número: ')))

new_vetor = list(dict.fromkeys(vetor))

print(vetor)
print(new_vetor)
