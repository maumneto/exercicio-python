# entrada de dados 
salario = float(input('Digite o valor do salario: '))
aumento = int(input('Digite o valor do aumento (%): '))
# calculo dos valores
valor_aumento = salario*(aumento/100)
novo_salario = salario + valor_aumento
novo_salario = round(novo_salario, 2)
# saida de dados
print('O valor do aumento é: ', valor_aumento)
print('O valor do novo salario é: ', novo_salario)