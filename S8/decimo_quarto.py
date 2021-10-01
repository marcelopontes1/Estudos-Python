import os

clear = lambda: os.system('cls')
clear()


def consumo_carro(distancia, litros):
    consumo = distancia / litros
    if consumo < 8:
        return print('Venda o carro!')
    elif consumo >= 8 and consumo < 12:
        return print('Ecônomico!')
    else:
        return print('Super econômico')

dist_user = float(input('Insira aqui a distância: '))
litros_user = float(input('Insira qui a quantidade de litros: '))

consumo_carro(dist_user, litros_user)
