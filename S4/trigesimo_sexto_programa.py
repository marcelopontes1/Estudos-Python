altura_cilindro = input('Insira aqui a altura do cilindro: ')
raio_cilindro = input('Insira aqui o raio do cilindro: ')
valor_pi = 3.141592

altura_cilindro_convert = float(altura_cilindro)
raio_cilindro_convert = float(raio_cilindro)

volume_cilindro = valor_pi * (raio_cilindro_convert ** 2) * altura_cilindro_convert

print(f'O valor do volume do cilindro é de {volume_cilindro} m³')
