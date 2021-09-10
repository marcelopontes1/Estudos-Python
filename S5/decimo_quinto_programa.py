def week(i):
    switcher = {
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday',
    }
    return switcher.get(i, "Invalid day of week")

num = input('Insira um número para saber o dia da semana equivalente: ')

num_convert = int(num)

dia_da_semana = week(num_convert)

print(dia_da_semana)
