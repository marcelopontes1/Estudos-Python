import datetime

numero = input('Insira um número inteiro: ')

numero_int = int(numero)

print (f'O valor disso em hh:mm:ss é de {datetime.timedelta(seconds=numero_int)}')
