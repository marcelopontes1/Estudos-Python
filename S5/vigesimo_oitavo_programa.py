def geometrica(x, y, z):
    media = (x * y *z) ** (1/3)
    return media

def ponderada(x, y, z):
    media = (x + (2 * y) + (3 * z))/6
    return media

def harmonica(x, y, z):
    media = 1/((1/x) + (1/y) + (1/z))
    return media

def aritmetica(x, y, z):
    media = (x + y + z)/3
    return media

print('1- Geométrica')
print('2- Ponderada')
print('3- Harmônica')
print('4- Aritmética')

opcao = int(input('Escolha a opção desejada: '))

if opcao >= 1 and opcao <= 4:
    if opcao == 1:
        x = int(input('Insira aqui um número inteiro para "x": '))
        y = int(input('Insira aqui um número inteiro para "y": '))
        z = int(input('Insira aqui um número inteiro para "z": '))
        valor_media = geometrica(x, y, z)
        print(f'O valor da média é {valor_media}')
    elif opcao == 2:
        x = int(input('Insira aqui um número inteiro para "x": '))
        y = int(input('Insira aqui um número inteiro para "y": '))
        z = int(input('Insira aqui um número inteiro para "z": '))
        valor_media = ponderada(x, y, z)
        print(f'O valor da média é {valor_media}')
    elif opcao == 3:
        x = int(input('Insira aqui um número inteiro para "x": '))
        y = int(input('Insira aqui um número inteiro para "y": '))
        z = int(input('Insira aqui um número inteiro para "z": '))
        valor_media = harmonica(x, y, z)
        print(f'O valor da média é {valor_media}')
    elif opcao == 4:
        x = int(input('Insira aqui um número inteiro para "x": '))
        y = int(input('Insira aqui um número inteiro para "y": '))
        z = int(input('Insira aqui um número inteiro para "z": '))
        valor_media = aritmetica(x, y, z)
        print(f'O valor da media é {valor_media}')
else:
    print('Opção inválida')