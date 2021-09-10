import os

clear = lambda: os.system('cls')
clear()

print('##### 100 primeiros números com a estrutura de repetição FOR #####')

for i in range(1, 100 + 1):
    print(i)

print('##### 100 primeiros números com a estrutura de repetição WHILE #####')

i = 0

while i < 100:
    i = i + 1
    print(i)
