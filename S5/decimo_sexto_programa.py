def year(i):
    switcher = {
        1:'Janeiro',
        2:'Fevereiro',
        3:'Março',
        4:'Abril',
        5:'Maio',
        6:'Junho',
        7:'Julho',
        8:'Agosto',
        9:'Setembro',
        10:'Outubro',
        11:'Novembro',
        12:'Dezembro',
    }
    return switcher.get(i, "Número de mês inválido")

num = input('Insira um número para saber o dia da semana equivalente: ')

num_convert = int(num)

mes_do_ano = year(num_convert)

print(mes_do_ano)
