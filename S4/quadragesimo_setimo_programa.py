numero = input('Insira aqui um número de quatro digitos (1000 a 9999):  ')

numero_int = int(numero)

x = [int(a) for a in str(numero_int)]

print(x[0])
print(x[1])
print(x[2])
print(x[3])