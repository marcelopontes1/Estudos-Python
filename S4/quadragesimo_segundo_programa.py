salario_base = input('Insira o seu salário base: ')

salario_base_convert = float(salario_base)
gratificacao = salario_base_convert * 0.05
imposto = salario_base_convert * 0.07

valor_total = salario_base_convert + gratificacao - imposto

print(f'O salário a receber tem o valor de {valor_total}')
