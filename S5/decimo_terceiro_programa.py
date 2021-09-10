nota1 = input('Insira aqui a primeira nota: ')
nota2 = input('Insira aqui a segunda nota: ')
nota3 = input('Insira aqui a terceira nota: ')

nota1_convert = float(nota1)
nota2_convert = float(nota2)
nota3_convert = float(nota3)

media_ponderada = ((nota1_convert * 1) + (nota2_convert * 1) + (nota3_convert * 2))/4

print(f'A média final é de {media_ponderada}')

if media_ponderada >= 6:
    print('O aluno foi aprovado!')
else:
    print('O aluno não foi aprovado')
