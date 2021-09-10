import os

clear = lambda: os.system('cls')
clear()

qtd_par = 0
vetor = []
vetor_pares = []

for i in range(10):
    valor = float(input('Insira aqui um valor: '))
    vetor.append(valor)
    if valor % 2 == 0:
        qtd_par += 1
        vetor_pares.append(valor)
    else:
        pass

print(vetor_pares)
print(f'O vetor tem {qtd_par} números pares')
