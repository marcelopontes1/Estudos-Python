def area_trapezio(base_maior, base_menor, altura):
    area = ((base_maior + base_menor) * altura)/2
    return area

base_menor = input('Insira o valor da base menor: ')
base_maior = input('Insira o valor da base maior: ')
altura = input('Insira o valor da altura: ')

base_menor_convert = float(base_menor)
base_maior_convert = float(base_maior)
altura_convert = float(altura)

area_total = area_trapezio(base_maior_convert, base_menor_convert, altura_convert)

print(f'O valor da área do trapézio é de {area_total}')
