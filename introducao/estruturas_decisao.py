x = int(input('Valor de X: '))
y = int(input('Valor de Y: '))

if x == y:
    print('X e Y são iguais!')
elif x > y:
    print('X é maior que Y!')
else:
    print('Y é maior que X!')

meu_saldo = float(input('Quanto tenho de saldo? '))
nome_produto = input('Qual nome do produto? ')
valor_produto = float(input('Qto custa o produto? '))

if meu_saldo >= valor_produto:
    print(f'Estou comprando um {nome_produto} novo!!')

else:
    dinheiro_emprestado = float(input('Dinheiro emprestado: '))

    if (meu_saldo + dinheiro_emprestado) >= valor_produto:
        print(f'Estou comprando um {nome_produto} novo com dinheiro emprestado!!')

    else:
        print(f'Deixarei para comprar o/a {nome_produto} mês que vme!!')

dado_verdadeiro = bool(input('Valor True/False'))

if not dado_verdadeiro:
    print('False')
