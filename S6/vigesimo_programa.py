import os

clear = lambda: os.system('cls')
clear()

contador = 0
num_pares = 0

while True:
    num = int(input('Digite aqui um número: '))
    if num == 1000:
        contador = contador + 1
        break
    elif num % 2 == 0:
        num_pares = num_pares + 1
        contador = contador + 1
        print(f'O número {num} é par')
    else:
        contador = contador + 1
        print(f'O número {num} é ímpar')

print(f'A quantidade de números pares é {num_pares}')
print(f'Foram lidos {contador} números no total')
