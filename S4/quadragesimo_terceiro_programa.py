valor_total_produto = input('Insira o valor total do produto: ')

valor_total_produto_convert = float(valor_total_produto)

desconto = valor_total_produto_convert * 0.1

valor_com_desconto = valor_total_produto_convert - desconto

print(f'O valor total a pagar com desconto de 10% é de {valor_com_desconto}')
print(f'O valor de cada parcela para o parcelamento em 3x sem juros é de {valor_total_produto_convert/3}')
print(f'A comissão do vendedor para venda a vista é de {valor_com_desconto * 0.05}')
print(f'A comissão do vendedor para venda parcelada é de {valor_total_produto_convert * 0.05}')
