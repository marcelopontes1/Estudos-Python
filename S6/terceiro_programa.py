import os

clear = lambda: os.system('cls')
clear()

i = 10

print('##### COMEÇANDO A CONTAGEM REGRESSIVA #####')

while i >= 0:
    print(i)
    i = i - 1
    
print('FIM!')
