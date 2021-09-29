import os

clear = lambda: os.system('cls')
clear()

def dobro(a):
    resultado = a * a
    return resultado

numero = int(input('Insira um número para calcular o dobro: '))

calc_num = dobro(numero)

print(f'O dobro do número é {calc_num}')
