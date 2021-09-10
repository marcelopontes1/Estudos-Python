valor1 = input('Digite o primeiro valor: ')
valor2 = input('Digite o segundo valor: ')
valor3 = input('Digite o terceiro valor: ')

valor1_convert = int(valor1)
valor2_convert = int(valor2)
valor3_convert = int(valor3)

valor1_quadrado = valor1_convert ** 2
valor2_quadrado = valor2_convert ** 2
valor3_quadrado = valor3_convert ** 2

soma = valor1_quadrado + valor2_quadrado + valor3_quadrado

print(f'O resultado da soma do quadrado dos números é {soma}')
