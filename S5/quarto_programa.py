num = input('Insira um número aqui: ')

num_int = int(num)

if num_int >= 0:
    num_quadrado = num_int ** 2
    num_raiz = num_int ** 0.5
    print(f'O resultado do número ao quadrado é {num_quadrado}')
    print(f'A raiz quadrada do número é {num_raiz}')
else:
    print('O número não é positivo')
    