salario = float(input('Digite o salário: '))
aumento = float(input('Digite o aumento: '))

valor_aumento = salario*aumento
valor_aumento = round(valor_aumento, 2)
salario_final = salario + valor_aumento
salario_final = round(salario_final,2)

print('Aumento: ', valor_aumento)
print('Salario Final: ', salario_final)