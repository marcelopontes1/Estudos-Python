from datetime import date, datetime, time, timedelta

# Recebendo os dados do usuário

data_inicio = input('Insira a hora de início (hh:mm:ss): ')
intervalo = input('Insira a duração da experiência em segundos: ')

# Processando a hora, minutos e segundos e jogando dentro de um vetor

x = data_inicio.split(":")

hora = x[0]
minuto = x[1]
segundo = x[2]

# Convertendo de string para inteiro

hora_int = int(x[0])
minuto_int = int(x[1])
segundo_int = int(x[2])

# Convertendo string para inteiro do intervalo

intervalo_int = int(intervalo)

# Somando os valores e printando a hora final

dt = datetime.combine(date.today(), time(hora_int, minuto_int, segundo_int)) + timedelta(seconds=intervalo_int)
print(f'A experiência terminará na hora {dt.time()}')
