a = float(input('Insira o valor de "a": '))
b = float(input('Insira o valor de "b": '))
c = float(input('Insira o valor de "c": '))

if a > 0:
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('Não existe raiz')
    elif delta == 0:
        x1 = (((b * -1) + (delta) ** 0.5))/2 * a
        x2 = (((b * -1) - (delta) ** 0.5))/2 * a
        print('Raiz única')
        print(x1, x2)
    elif delta >= 0:
        x1 = (((b * -1) + (delta) ** 0.5))/2 * a
        x2 = (((b * -1) - (delta) ** 0.5))/2 * a
else:
    print('Não é equação de segundo grau')
    