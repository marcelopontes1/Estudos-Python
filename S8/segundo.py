import os

clear = lambda: os.system('cls')
clear()

def convert_date(date):

    data_split = date.split('/')

    if int(data_split[1]) == 1:
        return print(f'{int(data_split[0])} de Janeiro de {int(data_split[2])}')
    elif int(data_split[1]) == 2:
        return print(f'{int(data_split[0])} de Fevereiro de {int(data_split[2])}')
    elif int(data_split[1]) == 3:
        return print(f'{int(data_split[0])} de Março de {int(data_split[2])}')
    elif int(data_split[1]) == 4:
        return print(f'{int(data_split[0])} de Abril de {int(data_split[2])}')
    elif int(data_split[1]) == 5:
        return print(f'{int(data_split[0])} de Maio de {int(data_split[2])}')
    elif int(data_split[1]) == 6:
        return print(f'{int(data_split[0])} de Junho de {int(data_split[2])}')
    elif int(data_split[1]) == 7:
        return print(f'{int(data_split[0])} de Julho de {int(data_split[2])}')
    elif int(data_split[1]) == 8:
        return print(f'{int(data_split[0])} de Agosto de {int(data_split[2])}')
    elif int(data_split[1]) == 9:
        return print(f'{int(data_split[0])} de Setembro de {int(data_split[2])}')
    elif int(data_split[1]) == 10:
        return print(f'{int(data_split[0])} de Outubro de {int(data_split[2])}')
    elif int(data_split[1]) == 11:
        return print(f'{int(data_split[0])} de Novembro de {int(data_split[2])}')
    elif int(data_split[1]) == 12:
        return print(f'{int(data_split[0])} de Dezembro de {int(data_split[2])}')
    else:
        pass

data_usuario = input('Insira a data desejada: ')

convert_date(data_usuario)
