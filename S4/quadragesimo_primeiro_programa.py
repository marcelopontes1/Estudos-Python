valor_hora = input('Insira o valor da hora de trabalho: ')
horas_mes = input('Insira o número de horas trabalhadas: ')

valor_hora_convert = float(valor_hora)
horas_mes_convert = float(horas_mes)

valor_total = (valor_hora_convert * horas_mes_convert) * 1.10

print(f'O valor a ser pago para o funcionário é de {valor_total} reais')
