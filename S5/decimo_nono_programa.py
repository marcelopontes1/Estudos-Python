num1 = int(input('Insira um número: '))

if num1 % 3 == 0 or num1 % 5 == 0:
    print('O número é divisível por 3 OU 5')
    if num1 % 3 == 0 and num1 % 5 == 0:
        print('O número é divisível por 3 E 5 ao mesmo tempo')
    else:
        print('O número não é divisível por 3 E 5 ao mesmo tempo')
else:
    print('O núero não é divisível por 3 OU 5')