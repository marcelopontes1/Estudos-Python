num = input('Insira um número inteiro: ')

num_int = int(num)

if num_int >= 0:
    raiz = num_int ** 0.5
    print(f'A raiz quadrada do número é {raiz}')
else:
    print('O número é inválido')
