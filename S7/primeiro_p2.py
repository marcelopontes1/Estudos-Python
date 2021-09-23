import os

clear = lambda: os.system('cls')
clear()

qtd_maior_dez = 0
matrix = [] 
  
for i in range(4):
    a = [] 
    for j in range(4):
        num = int(input())
        a.append(num)
        if num > 10:
            qtd_maior_dez += 1
        else:
            pass
    matrix.append(a) 
  
for i in range(4): 
    for j in range(4): 
        print(matrix[i][j], end = " ") 
    print() 

print(qtd_maior_dez)
