import os

clear = lambda: os.system('cls')
clear()

num = int(input('Digite um número entre 100 e 999: '))

for i in str(num):
    print(i)
