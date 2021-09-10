import os

clear = lambda: os.system('cls')
clear()

vetor = []

def soma(a, b):
    resultado = a + b
    return resultado

for i in range(0, 8):
    valor = float(input('Insira aqui um valor: '))
    vetor.append(valor)

x = int(input("Digite um valor inteiro para 'x' entre 1 e 8: "))
y = int(input("Digite um valor inteiro para 'y' entre 1 e 8: "))

calculo = soma(vetor[x - 1], vetor[y - 1])

print(calculo)