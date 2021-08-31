import os

clear = lambda: os.system('cls')
clear()

def divisores(num):
    for i in range(1, num // 2 + 1):
        if num % i == 0: 
            yield i
    yield num

num = int(input('Insira um número: '))

print(list(divisores(num)))
