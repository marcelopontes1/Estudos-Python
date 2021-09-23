import os

clear = lambda: os.system('cls')
clear()

qtd_maior_dez = 0
matrix = []

for i in range(5):
    a = [] 
    for j in range(5):
        if i == j:
            a.append(1)
        else:
            a.append(0)
    matrix.append(a) 

for i in range(5): 
    for j in range(5): 
        print(matrix[i][j], end = " ") 
    print()
