def valor_final(valor, imposto):
    preco_final = valor * (1 + (imposto/100))
    return preco_final

print('Escolha qual o estado:')
print('1 - MG (7%)')
print('2 - SP (12%)')
print('3 - RJ (15%)')
print('4 - MS (8%)')

num_estado = int(input('Insira aqui a opção: '))

if num_estado == 1:
    valor = float(input('Insira o valor do produto: '))
    prod_final = valor_final(valor, 7)
    print(f'O valor final do produto é {prod_final}')
elif num_estado == 2:
    valor = float(input('Insira o valor do produto: '))
    prod_final = valor_final(valor, 12)
    print(f'O valor final do produto é {prod_final}')
elif num_estado == 3:
    valor = float(input('Insira o valor do produto: '))
    prod_final = valor_final(valor, 15)
    print(f'O valor final do produto é {prod_final}')
elif num_estado == 4:
    valor = float(input('Insira o valor do produto: '))
    prod_final = valor_final(valor, 8)
    print(f'O valor final do produto é {prod_final}')
else:
    print('Opção inválida')
    