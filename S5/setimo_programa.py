num1 = input('Insira o primeiro número: ')
num2 = input('Insira o segundo número: ')

num1_int = int(num1)
num2_int = int(num2)

if num1_int > num2_int:
    print(f'O número {num1_int} é maior do que {num2_int} e a diferença entre eles é de {num1_int - num2_int}')
elif num1_int == num2_int:
    print('Números iguais')
else:
    print(f'O número {num2_int} é maior do que {num1_int} e a diferença entre eles é de {num2_int - num1_int}')