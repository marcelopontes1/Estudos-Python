import os

clear = lambda: os.system('cls')
clear()

def media_aluno(nota1, nota2, nota3, tipo_media):
    if tipo_media == 'A':
        media = (nota1 + nota2 + nota3) / 3
        return media
    elif tipo_media == 'P':
        media = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10
        return media

nota1_user = float(input('Insira o valor da nota: '))
nota2_user = float(input('Insira o valor da nota: '))
nota3_user = float(input('Insira o valor da nota: '))
tipo_media = input('Insira o tipo da média (A ou P): ')

media_final = media_aluno(nota1_user, nota2_user, nota3_user, tipo_media)

print(f'A méda final do aluno é {media_final}')
