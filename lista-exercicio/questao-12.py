# entrada de dados
nota_1 = float(input('Digite o valor da primeira nota: '))
nota_2 = float(input('Digite o valor da segunda nota: '))
# calculo da média
media = (nota_1 + nota_2)/2
print('media = ',media)
# logica condicional da questao
if (media >= 7):
    print('Aprovado!')
else:
    print('Reprovado!')