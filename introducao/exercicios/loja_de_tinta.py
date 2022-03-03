# Exercicio 3 - Loja de Tintas

print('\n')
print('\t▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ▄ █ ▄')
print('\t▀   *    Tintas & Cores    *  ▀')
print('\t▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
print('\n')

preco_lata_18_litros = 80.00
quantidade_litros_lata_padrao = 18
quantidade_metro_quadrado_litro = 3

metros_quadrados = float(input('\tQuantos metros² deseja: '))
quantidade_litros = metros_quadrados / quantidade_metro_quadrado_litro

valor_total = 0

if quantidade_litros > quantidade_litros_lata_padrao:
    valor_total = (quantidade_litros / quantidade_litros_lata_padrao) * preco_lata_18_litros
else:
    valor_total = preco_lata_18_litros

print('\tValor total: R$ {:.2f}'.format(valor_total))
print('\n')

