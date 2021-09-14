import os

clear = lambda: os.system('cls')
clear()

vetor = []

for i in range(5):
    vetor.append(float(input('Insira um número: ')))

print('---SELECIONE A OPÇÃO---')
print('0 - Finalizar o programa')
print('1 - Mostrar o vetor na ordem direta')
print('2 - Mostrar o vetor na ordem reversa')

opcao = int(input('Insira o valor desejado: '))

if opcao == 0:
    print('Finalizando programa')
elif opcao == 1:
    print(vetor)
elif opcao == 2:
    vetor.reverse()
    print(vetor)
else:
    print('Opção inválida')
