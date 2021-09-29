import os

clear = lambda: os.system('cls')
clear()

def hipotenusa(a, b):
    valor = (((a ** 2) + (b ** 2))) ** 0.5
    return valor

a_user = float(input('Insira o valor de a: '))
b_user = float(input('Insira o valor de b: '))

valor_hipotensa = hipotenusa(a_user, b_user)

print(f'O valor da hipotenusa é {valor_hipotensa}')
