# Exercicio 5 - Notas dos alunos

print('\n')
print('\t▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █ ▄ █ ▄ █ ▄')
print('\t▀   *    Escola do Saber   *  ▀')
print('\t▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
print('\n')

nota_corte = 7
nota_distincao = 10
resultado_final = None

nota_A = float(input('\tInforme a nota 1: '))
nota_B = float(input('\tInforme a nota 2: '))

nota_media = (nota_A + nota_B) / 2

if nota_media >= nota_distincao:
    resultado_final = '\t◉ Aluno aprovado com distinção!'

elif nota_media >= nota_corte:
    resultado_final = '\t◉ Aluno aprovado!'

elif nota_media < nota_corte:
    resultado_final = '\t◉ Aluno reprovado!'

print(resultado_final)
print('\n')
