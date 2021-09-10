num = input('Insira um número: ')

num_float = float(num)

if num_float >= 0:
    raiz = num_float ** 0.5
    print(f'O número é positivo, portanto sua raiz é {raiz}')
else:
    quadrado_num = num_float ** 2
    print(f'O número é negativo, portanto seu valor ao quadrado é {quadrado_num}')
