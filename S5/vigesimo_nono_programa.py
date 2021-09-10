import random, os

clear = lambda: os.system('cls')
clear()

num1 = random.randint(1,100)
num2 = random.randint(1,100)

print(num1, num2)

pergunta1 = int(input(f'Qual é a soma de {num1} + {num2}? '))
pergunta2 = float(input(f'Qual é a subtração de {num1} - {num2}? '))
pergunta3 = int(input(f'Qual é a multiplicação de {num1} * {num2}? '))
pergunta4 = float(input(f'Qual é a divisão de {num1} / {num2}? '))
pergunta5 = int(input(f'Qual o sucessor de {num1}? '))

resposta1 = num1 + num2
resposta2 = num1 - num2
resposta3 = num1 * num2
resposta4 = num1 / num2
resposta5 = num1 + 1

print(f'Resposta 1: {num1 + num2}')
print(f'Resposta 2: {num1 - num2}')
print(f'Resposta 3: {num1 * num2}')
print(f'Resposta 4: {num1 / num2}')
print(f'Resposta 5: {num1 + 1}')

respostas_corretas = 0

if pergunta1 == resposta1:
    respostas_corretas += 1
else:
    respostas_corretas = respostas_corretas

if pergunta2 == resposta2:
    respostas_corretas += 1
else:
    respostas_corretas = respostas_corretas

if pergunta3 == resposta3:
    respostas_corretas += 1
else:
    respostas_corretas = respostas_corretas

if pergunta4 == resposta4:
    respostas_corretas += 1
else:
    respostas_corretas = respostas_corretas

if pergunta5 == resposta5:
    respostas_corretas += 1
else:
    respostas_corretas = respostas_corretas

if respostas_corretas == 0:
    print('Você não acertou nenhuma questão')
elif respostas_corretas == 1:
    print(f'Você acertou {respostas_corretas} questão')
else:
    print(f'Você acertou {respostas_corretas} questões!')
