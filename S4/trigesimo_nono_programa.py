valor_total = 780000

primeiro_premio = valor_total * 0.46
segundo_premio = valor_total * 0.32
terceiro_premio = valor_total - primeiro_premio - segundo_premio

print(f'O primeiro ganhador receberá o valor de {primeiro_premio} reais')
print(f'O segundo ganhador receberá o valor de {segundo_premio} reais')
print(f'O terceiro ganhador receberá o valor de {terceiro_premio} reais')
