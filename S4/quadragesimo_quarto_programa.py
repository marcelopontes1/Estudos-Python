from typing import AsyncIterable


altura_degrau = input('Insira a altura do degrau (cm): ')
altura_desejada = input('Insira qual altura desejada (cm): ')

altura_degrau_convert = float(altura_degrau)
altura_desejada_convert = float(altura_desejada)

numero_degraus = altura_desejada_convert/altura_degrau_convert

print(f'Será necessário subir {numero_degraus} degraus')
