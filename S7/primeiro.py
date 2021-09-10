import os

clear = lambda: os.system('cls')
clear()

vetor_A = [1, 0, 5, -2, -5, 7]

soma = vetor_A[0] + vetor_A[1] + vetor_A[5]

vetor_A[4] = 100

for i in vetor_A:
    print(i)
