import os

clear = lambda: os.system('cls')
clear()

soma = 0
vetor = []
vetor_negativos = []
vetor_positivos = []

for i in range(10):
    num = float(input('Insira um número: '))
    vetor.append(num)
    if num < 0:
        vetor_negativos.append(num)
    else:
        soma = soma + num
        vetor_positivos.append(num)

print(f'A soma dos números positivos é {soma}')
print(f'O vetor possui {len(vetor_negativos)} números negativos')
