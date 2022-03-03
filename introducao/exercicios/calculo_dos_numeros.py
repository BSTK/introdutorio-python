# Exercicio 4 - Cálculo dos Números

print('\n')
print('\t▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ▄ █ ▄')
print('\t▀ * Cálculo dos Números    *  ▀')
print('\t▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
print('\n')

numero_float = float(input('\tInforme o número float: '))
numero_inteiro_A = int(input('\tInforme o número inteiro A: '))
numero_inteiro_B = int(input('\tInforme o número inteiro B: '))

produto_do_dobro = (numero_inteiro_A * 2) * (numero_inteiro_B / 2)
soma_do_triplo = (numero_inteiro_A * 3) + numero_float
terceiro_elevado = numero_float ** 3

print('\n')
print(f'\t◉ Produto do dobro = { produto_do_dobro }')
print(f'\t◉ Soma do triplo   = { soma_do_triplo }')
print('\t◉ Terceiro elevado = {:.2f}'.format(terceiro_elevado))
print('\n')
