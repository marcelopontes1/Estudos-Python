import os

clear = lambda: os.system('cls')
clear()

soma = 0

def divisores(num):
    for i in range(1, num // 2 + 1):
        if num % i == 0: 
            yield i
    yield num

num = int(input('Insira um número: '))

for d in divisores(num):
    soma = soma + d

soma = soma - num
print(f'A soma dos dividores do número {num} é {soma}')
