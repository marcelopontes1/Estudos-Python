import os

clear = lambda: os.system('cls')
clear()

def convert(hora, minutos, segundos): 
    hora_convertida = hora * 3600
    minuto_convertido = minutos * 60
    tempo_total = hora_convertida + minuto_convertido + segundos
    return tempo_total

hora_user = int(input('Insira o valor da hora: '))
minuto_user = int(input('Insira o valor dos minutos: '))
segundos_user = int(input('Insira o valor dos segundos: '))

hora_total = convert(hora_user, minuto_user, segundos_user)

print(f'O valor em segundos é de {hora_total}')
