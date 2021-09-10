import math

num = input('Insira um número: ')

num_convert = int(num)

if num_convert >= 0:
    log = math.log(num_convert)
    print(f'O logaritmo natural de {num_convert} é {log}')
else:
    print('Número inválido')
