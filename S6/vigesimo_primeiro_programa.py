import os

clear = lambda: os.system('cls')
clear()

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma = 0
multiplicacao = 1

if num1 > num2:
    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            soma = soma + i
        else:
            multiplicacao = multiplicacao * i
elif num1 < num2:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            soma = soma + i
        else:
            multiplicacao = multiplicacao * i
else:
    print('Não existe intervalo')

print(f'O valor da soma dos números pares é {soma}')
print(f'O valor da multiplicação dos números ímpares é {multiplicacao}')
