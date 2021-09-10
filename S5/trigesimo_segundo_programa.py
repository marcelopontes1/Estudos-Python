import os

clear = lambda: os.system('cls')
clear()

codigo = int(input('Insira o código do produto: '))
quantidade = int(input('Insira a quantidade desejada: '))

if codigo == 100:
    preco_pedido = quantidade * 1.20
    print(f'O valor do seu pedido é {preco_pedido} reais')
elif codigo == 101:
    preco_pedido = quantidade * 1.30
    print(f'O valor do seu pedido é {preco_pedido} reais')
elif codigo == 102:
    preco_pedido = quantidade * 1.50
    print(f'O valor do seu pedido é {preco_pedido} reais')
elif codigo == 103:
    preco_pedido = quantidade * 1.20
    print(f'O valor do seu pedido é {preco_pedido} reais')
elif codigo == 104:
    preco_pedido = quantidade * 1.70
    print(f'O valor do seu pedido é {preco_pedido} reais')
elif codigo == 105:
    preco_pedido = quantidade * 2.20
    print(f'O valor do seu pedido é {preco_pedido} reais')
elif codigo == 106:
    preco_pedido = quantidade * 1.00
    print(f'O valor do seu pedido é {preco_pedido} reais')
else:
    print('Código inválido')
