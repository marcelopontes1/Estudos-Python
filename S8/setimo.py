import os

clear = lambda: os.system('cls')
clear()

def convert_temp(temp_celsius):
    temp_fah = temp_celsius * (9.0/5.0) + 32.0
    return temp_fah

temp_user = float(input('Insira o valor da temperatura em graus Celsius: '))

temp_convertida = convert_temp(temp_user)

print(f'O valor da temperatura em graus Fahrenheit é de {temp_convertida}')
