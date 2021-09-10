val_a = float(input('Insira o primeiro valor: '))
val_b = float(input('Insira o segundo valor: '))
val_c = float(input('Insira o terceiro valor: '))

if (val_a + val_b > val_c) or (val_a + val_c > val_b) or (val_b + val_c > val_a):
    print('É um triângulo')
    if (val_a == val_b == val_c):
        print('É um triângulo equilátero')
    elif (val_a == val_b) or (val_a == val_c) or (val_b == val_c):
        print('É um triângulo isósceles')
    elif (val_a != val_b != val_c):
        print('É um triângulo escaleno')
else:
    print('Não é um triângulo')
