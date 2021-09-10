idade = int(input('Insira aqui a sua idade: '))
tempo_servico = int(input('Insira aqui o seu tempo de serviço: '))

if idade >= 65:
    print('Pode se aposentar')
else:
    if tempo_servico >= 30:
        print('Pode se aposentar')
    else:
        if idade >= 60 and tempo_servico >= 25:
            print('Pode se aposentar')
        else:
            print('Não pode se aposentar')
            