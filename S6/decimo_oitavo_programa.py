import os

clear = lambda: os.system('cls')
clear()

lista_num = []
maior = 0
menor = 0
qtd_maior = 0

valor_n = int(input('Digite o valor de N: '))

for c in range(0, valor_n):
    lista_num.append(int(input(f'Digite um número: ')))
    if c == 0:
        maior = menor = lista_num[c]
    else:
        if lista_num[c] > maior:
            maior = lista_num[c]
        if lista_num[c] < menor:
            menor = lista_num[c]

print('=-' * 30)
print(f'Você digitou os os valores {lista_num}')
print(f'O maior valor digitado foi {maior} ', end='')
for i, v in enumerate(lista_num):
    if v == maior:
        qtd_maior = qtd_maior + 1
        
print(f'e foi digitado {qtd_maior} vezes', end='')
