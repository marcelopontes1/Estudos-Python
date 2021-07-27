temp_fahrenheit = input('Digite a temperatura em graus Fahrenheit: ')

temp_fahrenheit_real = float(temp_fahrenheit)

temp_celsius = 5.0 * (temp_fahrenheit_real - 32.0)/9.0

print(f'A temperatura em Fahrenheit é {temp_fahrenheit_real} e a temperatura em Celsius é {temp_celsius}')
