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

print('De acordo com o menu, escolha sua operação: ')
print('1: Somar')
print('2: Subtrair')
print('3: Multiplicar')
print('4: Dividir')

opcao_escolhida = input('Escolha a sua operação: ')

opcao_escolhida_converted = int(opcao_escolhida)

if opcao_escolhida_converted == 1:
    num1 = input('Digite o primeiro valor: ')
    num2 = input('Digite o segundo número: ')
    num1_convert = float(num1)
    num2_convert = float(num2)
    resultado = soma(num1_convert, num2_convert)
    print(f'O resultado da operação é {resultado}')
elif opcao_escolhida_converted == 2:
    num1 = input('Digite o primeiro valor: ')
    num2 = input('Digite o segundo número: ')
    num1_convert = float(num1)
    num2_convert = float(num2)
    resultado = subtracao(num1_convert, num2_convert)
    print(f'O resultado da operação é {resultado}')
elif opcao_escolhida_converted == 3:
    num1 = input('Digite o primeiro valor: ')
    num2 = input('Digite o segundo número: ')
    num1_convert = float(num1)
    num2_convert = float(num2)
    resultado = multiplicacao(num1_convert, num2_convert)
    print(f'O resultado da operação é {resultado}')
elif opcao_escolhida_converted == 4:
    num1 = input('Digite o primeiro valor: ')
    num2 = input('Digite o segundo número: ')
    num1_convert = float(num1)
    num2_convert = float(num2)
    resultado = divisao(num1_convert, num2_convert)
    print(f'O resultado da operação é {resultado}')
else:
    print('Opcação inválida')
