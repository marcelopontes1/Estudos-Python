import os

clear = lambda: os.system('cls')
clear()

lista_num = []
maior = 0
menor = 0

for i in range(0, 10):
    lista_num.append(int(input(f'Digite um número: ')))
    if i == 0:
        maior = menor = lista_num[i]
    else:
        if lista_num[i] > maior:
            maior = lista_num[i]
        if lista_num[i] < menor:
            menor = lista_num[i]

print('=-' * 30)
print(f'Você digitou os os valores {lista_num}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
