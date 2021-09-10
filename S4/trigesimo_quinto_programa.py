cateto_a = input('Insira o valor do cateto A: ')
cateto_b = input('Insira o valor do cateto B: ')

cateto_a_convert = float(cateto_a)
cateto_b_convert = float(cateto_b)

hipotenusa = ((cateto_a_convert ** 2) + (cateto_b_convert ** 2)) ** 0.5

print(f'O valor da hipotenusa é de {hipotenusa}')
