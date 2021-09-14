import os
from collections import Counter

clear = lambda: os.system('cls')
clear()

vetor = []

for i in range(10):
    vetor.append(int(input('Insira um número: ')))
 
d = Counter(vetor)
 
new_list = list([item for item in d if d[item] > 1])
print(new_list)
