# entrada de dados
nota_1 = float(input('Digite o valor da primeira nota: '))
nota_2 = float(input('Digite o valor da segunda nota: '))
nota_3 = float(input('Digite o valor da terceira nota: '))
# calculo da média
media = (nota_1 + nota_2 + nota_3)/3
media = round(media, 2)
# saída da informação da média
print('A media das notas é: ', media)