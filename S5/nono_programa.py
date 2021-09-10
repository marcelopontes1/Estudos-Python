salario = input('Insira aqui o seu salário: ')
prestacao = input('Insira aqui o valor da prestação: ')

salario_float = float(salario)
prestacao_float = float(prestacao)

if prestacao_float > (salario_float * 0.2):
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
    