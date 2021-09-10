altura = input('Altura (m): ')
sexo = input('Sexo (Masculino ou Feminino): ')

altura_float = float(altura)
sexo_formated = sexo.title()

good_answer = 'Masculino'

if sexo_formated == good_answer:
    peso_ideal = (72.7 * altura_float) - 58
    print(f'Peso ideal: {peso_ideal}')
else:
    peso_ideal = (62.1 * altura_float) - 44.7
    print(f'Peso ideal: {peso_ideal}') 
