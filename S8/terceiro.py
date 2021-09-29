import os

clear = lambda: os.system('cls')
clear()

def check_number(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    return 1

num_user = float(input('Insira um número: '))

if check_number(num_user) == -1:
    print('O número é negativo')
elif check_number(num_user) == 0:
    print('O número é zero')
else:
    print('O número é positivo')
