def soma(a, b):
    result = a + b
    return result

def subtracao(a, b):
    result = a - b
    return result

def divisao(a, b):
    result = a/b
    return result

def multiplicacao(a, b):
    result = a * b
    return result

print('Escolha a opção:')
print('1- Soma de 2 números.')
print('2- Diferença entre 2 números (maior pelo menor).')
print('3- Produto entre 2 números.')
print('4- Divisão entre 2 números (o denominador não pode ser zero).')
opcao = int(input('Opção: '))

if opcao == 1:
    num1 = input('Digite o primeiro valor: ')
    num2 = input('Digite o segundo número: ')
    num1_convert = float(num1)
    num2_convert = float(num2)
    resultado = soma(num1_convert, num2_convert)
    print(f'O resultado da operação é {resultado}')
elif opcao == 2:
    num1 = input('Digite o primeiro valor: ')
    num2 = input('Digite o segundo número: ')
    num1_convert = float(num1)
    num2_convert = float(num2)
    resultado = subtracao(num1_convert, num2_convert)
    print(f'O resultado da operação é {resultado}')
elif opcao == 3:
    num1 = input('Digite o primeiro valor: ')
    num2 = input('Digite o segundo número: ')
    num1_convert = float(num1)
    num2_convert = float(num2)
    resultado = multiplicacao(num1_convert, num2_convert)
    print(f'O resultado da operação é {resultado}')
elif opcao == 4:
    num1 = input('Digite o primeiro valor: ')
    num2 = input('Digite o segundo número: ')
    num1_convert = float(num1)
    num2_convert = float(num2)
    resultado = divisao(num1_convert, num2_convert)
    print(f'O resultado da operação é {resultado}')
else:
    print('Opcação inválida')
