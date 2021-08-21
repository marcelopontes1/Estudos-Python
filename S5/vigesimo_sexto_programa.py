distancia = float(input('Insira a distância em km: '))
litros = float(input('Insira a quantidade de litros: '))

consumo = distancia / litros

print(f'Seu carro faz {consumo} km/l')

if consumo <= 8:
    print('Venda o carro!')
elif consumo >= 8 and consumo <= 12:
    print('Econômico!')
else:
    print("Super econômico")
