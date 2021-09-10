nota1 = input('Insira a primeira nota: ')
nota2 = input('Insira a seguda nota: ')

nota1_float = float(nota1)
nota2_float = float(nota2)

if (nota1_float >= 0 and nota1_float <= 10) and (nota2_float >= 0 and nota2_float <= 10):
    media = (nota1_float + nota2_float)/2
    print (f'A média entre as notas é {media}')
else:
    print('Impossivel de calcular a média pois foi digitado um número inválido')
