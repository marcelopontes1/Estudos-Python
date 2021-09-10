valor_dia = 30

qnt_dias = input('Insira o número de dias trabalhados: ')

qnt_dias_convert = int(qnt_dias)

valor_bruto = qnt_dias_convert * 30

valor_liquido = valor_bruto - (valor_bruto * 0.08)

print(f'O valor líquido pelos {qnt_dias_convert} dias trabalhados é de {valor_liquido}')
