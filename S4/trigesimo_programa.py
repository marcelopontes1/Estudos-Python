valor_real = input('Digite o valor em real: ')
valor_real_float = float(valor_real)

cotacao_dolar = input('Digite a cotação do dólar: ')
cotacao_dolar_float = float(cotacao_dolar)

valor_dolares = valor_real_float/cotacao_dolar_float

print(f'O valor correspondente em dólar é de {valor_dolares} dólares')
