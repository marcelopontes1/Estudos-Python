num = input('Insira aqui o seu número: ')

num_convert = float(num)

soma = 0

if num_convert > 0:
    for digit in num:
        soma = soma + int(digit)
    print(f'A soma de todos os algarismos é {soma}')
else:
    print('Número inválido')
