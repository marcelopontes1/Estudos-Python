import os

clear = lambda: os.system('cls')
clear()

def operacoes(valor1, valor2, simbolo):
    if simbolo == '+':
        operacao = valor1 + valor2
        return print(f'O resultado é {operacao}')
    elif simbolo == '-':
        operacao = valor1 - valor2
        return print(f'O resultado é {operacao}')
    elif simbolo == '/':
        operacao = valor1 / valor2
        return print(f'O resultado é {operacao}')
    elif simbolo == '*':
        operacao = valor1 * valor2
        return print(f'O resultado é {operacao}')
    else:
        return print('Operação inválida')

valor1_user = float(input('Insira o primeiro valor: '))
valor2_user = float(input('Insira o segundo valor: '))
simbolo_user = input('Insira a operação desejada: ')

operacoes(valor1_user, valor2_user, simbolo_user)
