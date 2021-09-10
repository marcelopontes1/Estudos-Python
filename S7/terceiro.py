import os

clear = lambda: os.system('cls')
clear()

numeros = []
numeros_quadrado = []

for i in range(1, 11):
    valor = float(input('Insira aqui um valor: '))
    valor_quadrado = valor ** 2
    numeros.append(valor)
    numeros_quadrado.append(valor_quadrado)

print(numeros)
print(numeros_quadrado)
